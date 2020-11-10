# VFD Dataset (Japanese)

We propose a visually-grounded first-person dialogue (VFD) dataset with verbal and non-verbal responses.
The VFD dataset provides manually annotated (1) first-person images of agents, (2) utterances of human speakers, (3) eye-gaze locations of the speakers, and (4) the agents' verbal and non-verbal responses.
All utterances and responses are represented in Japanese.
The images with eye-gaze locations are available at [GazeFollow (MIT)](http://gazefollow.csail.mit.edu/index.html).

## Annotation Format

The annotations are stored in a single TSV file.
The description of each field of the file is as follows:
* `utterance`: an utterance (text) of the person in the image
* `image_path`: an image file path in the GazeFollow dataset
* `gfid`: an annotation ID of the GazeFollow dataset 
* `verbal_response`: a verbal response (text) of the agent
* `non_verbal_response`: a non-verbal response (text) of the agent

## Dataset for selection task

First, please download image data from [Download GazeFollow (MIT)](http://gazefollow.csail.mit.edu/download.html).

Then, the train/val/test data will be output by running this script.
```bash
$ python prepare_data_for_selection_task.py
```

### Requirement
  
* Python 3.8.5
* pandas 1.1.3

## License

[Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/legalcode)

### Citation

```
@inproceedings{kamezawa-etal-2020-visually,
    title = "A Visually-grounded First-person Dialogue Dataset with Verbal and Non-verbal Responses",
    author = "Kamezawa, Hisashi  and
      Nishida, Noriki  and
      Shimizu, Nobuyuki  and
      Miyazaki, Takashi  and
      Nakayama, Hideki",
    booktitle = "Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.emnlp-main.267",
    pages = "3299--3310",
}
```
