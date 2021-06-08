# FaceRecognition


Create an end to end face recognition pipeline with Docker for [this dataset](https://www.kaggle.com/rawatjitesh/avengers-face-recognition/download) (56.61 MB).

Dataset structure is below:

- → cropped_images
    - → chris_evans
    - → chris_hemsworth
    - → mark_ruffalo
    - → robert_downey_jr
    - → scarlett_johansson

Selected AlexNetpretrained face recognition model with least memory footprint, and train it on using 80% of the dataset, and test on the remaining 20%.

- Trained a face recognition model with the smallest memory footprint and fast inference (testing accuracy ~ 95%).

- Training script utilizes one GPU, which we can run inside the docker container bash as:

    `$ python train.py`

-= Testing script which utilizes one GPU, which we can run inside the docker container bash as:

    `$ python test.py`
    
