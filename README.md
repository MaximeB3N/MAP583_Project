# MAP583_Project

## DL-DIY potential project ideas
- check out challenge description [[here](http://dcase.community/challenge2021/task-acoustic-scene-classification#subtask-a)]
- take into consideration information of different sensors during training, e.g. [[residual normalization](https://dcase.community/documents/challenge2021/technical_reports/DCASE2021_Kim_36_t1.pdf)]
- train a larger network and then compress it into a smaller one with pruning, distillation or lottery ticket hypothesis, [[example](https://dcase.community/documents/challenge2021/technical_reports/DCASE2021_Yang_124_t1.pdf)]
- train over multiple domaines using adversarial domain adaptation [[ref](https://dcase.community/documents/challenge2021/technical_reports/DCASE2021_Koutini_112_t1.pdf)]
- train network in a multi-task manner, e.g., adding new granularity of classes [[ref](https://dcase.community/documents/challenge2021/technical_reports/DCASE2021_Heo_30_t1.pdf)]

-----------------
## Separable convolutions and test-time augmentations for low-complexity and calibrated acoustic scene classification (DCASE21 Challenge)

[**SEPARABLE CONVOLUTIONS AND TEST-TIME AUGMENTATIONS FOR LOW-COMPLEXITY AND CALIBRATED ACOUSTIC SCENE CLASSIFICATION**]() 

[*Gilles Puy*](https://sites.google.com/site/puygilles/home),
[*Himalaya Jain*](https://himalayajain.github.io/),
[*Andrei Bursuc*](https://abursuc.github.io/)  
*valeo.ai, Paris, France*

This repo contains the code to reproduce the results of the systems we submitted to the Task1a of the DCASE21 challenge. 
Please refer to [link1](http://dcase.community/challenge2021/task-acoustic-scene-classification#subtask-a) and 
[link2](https://arxiv.org/abs/2105.13734) for more information about the challenge.


If you find this code useful, please cite our [technical report]():
```
@techreport{vai21dcase,
  title={Separable convolutions and test-time augmentations for low-complexity and calibrated acoustic scene classification},
  author={Puy, Gilles and Jain, Himalaya and Bursuc, Andrei},
  institution={{DCASE2021 Challenge}},
  year={2021},
}
```
## Preparation

### Environment
* Python == 3.7
* CUDA >= 10.2
```bash
$ pip install torch===1.7.1 torchvision===0.8.2 torchaudio===0.7.2 -f https://download.pytorch.org/whl/torch_stable.html
$ pip install tqdm scikit-learn tensorboard pandas pyaml torchlibrosa
$ apt install -y libsndfile1
```

To help you re-create this environment, we also provide the dockerfile used to run the experiments in 
```/path/to/SP4ASC/Dockerfile```.
 
### DCASE21 Datasets
If not already done, please download the development and evaluation datasets from
[here](http://dcase.community/challenge2021/task-acoustic-scene-classification#download). 

We subsampled the whole dataset to select a smaller one and balanced over all classes. For our project we provide a notebook to do it step by step or a script file usable after downloading and unzipping the [TAU Urban Acoustic Scenes 2020 Mobile, Development dataset](https://zenodo.org/record/3819968#.Yidm-BOZOrM). For that you can use the following lines in a terminal :
```bash
pip install zenodo-get
zenodo_get -d 10.5281/zenodo.3819968
```
 Then you unzip by hands or using a bash script. 
