import random
import pandas as pd

random.seed(0)

def split_df(df, val_size, test_size):
    train_df = df[:len(df) - (val_size + test_size)]
    val_df = df[len(df) - (val_size + test_size):len(df) - test_size]
    test_df = df[len(df) - test_size:len(df)]

    return train_df, val_df, test_df

def add_gaze(df):
    df_ann = pd.read_csv('data_new/train_annotations.txt', delimiter=',', header=None)
    gaze = {}
    for _, r in df_ann.iterrows():
        gaze[r[1]] = [r[6], r[7], r[8], r[9]]

    data = []
    for _, r in df.iterrows():
        data.append([r['utterance'], r['image_path'], gaze[r['gf_id']][0], gaze[r['gf_id']][1], \
                     gaze[r['gf_id']][2], gaze[r['gf_id']][3], r['verbal_response'], r['non_verbal_response']])

    return pd.DataFrame(data)

def export_csv(df, verbal_type, split_name):
    utterance_response_pairs = []
    for _, r in df.iterrows():
        response = r[6] if verbal_type == 'verbal' else r[7]
        utterance_response_pairs.append([r[0], response])

    data = [['utterance', 'image_path', 'eye_x', 'eye_y', 'gaze_x', 'gaze_y', verbal_type + '_response', 'label']]
    for _, r in df.iterrows():
        response = r[6] if verbal_type == 'verbal' else r[7]
        data.append([r[0], r[1], r[2], r[3], r[4], r[5], response, 1])

        while True:
            t = random.choice(utterance_response_pairs)
            if t[0] != r[0]:
                data.append([r[0], r[1], r[2], r[3], r[4], r[5], t[1], 0])
                break

    pd.DataFrame(data).to_csv(verbal_type + '_' + split_name + '.csv', index=False, header=False)

def export_extra_test_csv(df, verbal_type):
    utterance_response_pairs = []
    for _, r in df.iterrows():
        response = r[6] if verbal_type == 'verbal' else r[7]
        utterance_response_pairs.append([r[0], response])

    data = [['utterance', 'image_path', 'eye_x', 'eye_y', 'gaze_x', 'gaze_y', 'ground_truth', 'negative_1', \
             'negative_2', 'negative_3', 'negative_4', 'negative_5', 'negative_6', 'negative_7', 'negative_8', 'negative_9']]

    for _, r in df.iterrows():
        while True:
            samples = random.sample(utterance_response_pairs, 9)
            flag = True
            negatives = []
            for s in samples:
                if s[0] != r[0] and s[1].strip('。') not in [n.strip('。') for n in negatives]:
                    negatives.append(s[1])
                else:
                    flag = False

            if flag == True:
                response = r[6] if verbal_type == 'verbal' else r[7]
                data.append(sum([[r[0]], [r[1]], [r[2]], [r[3]], [r[4]], [r[5]], [response], negatives], []))
                break

    pd.DataFrame(data).to_csv(verbal_type + '_test_with_negative.csv', index=False, header=False)

df = pd.read_csv('vfd.tsv', delimiter='\t')
verbal_df = df.dropna(subset=['verbal_response'])
train_verbal, val_verbal, test_verbal = split_df(verbal_df, 12000, 12000)
train_verbal, val_verbal, test_verbal = add_gaze(train_verbal), add_gaze(val_verbal), add_gaze(test_verbal)
export_csv(train_verbal, 'verbal', 'train')
export_csv(val_verbal, 'verbal', 'val')
export_csv(test_verbal, 'verbal', 'test')
export_extra_test_csv(test_verbal, 'verbal')

non_verbal_df = df.dropna(subset=['non_verbal_response'])
train_non_verbal, val_non_verbal, test_non_verbal = split_df(non_verbal_df, 3000, 3000)
train_non_verbal, val_non_verbal, test_non_verbal = add_gaze(train_non_verbal), add_gaze(val_non_verbal), add_gaze(test_non_verbal)
export_csv(train_non_verbal, 'non_verbal', 'train')
export_csv(val_non_verbal, 'non_verbal', 'val')
export_csv(test_non_verbal, 'non_verbal', 'test')
export_extra_test_csv(test_non_verbal, 'non_verbal')
