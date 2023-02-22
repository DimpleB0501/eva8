import albumentations as A
from albumentations.pytorch import ToTensorV2
import copy
import random
import matplotlib.pyplot as plt
import numpy as np

import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as

batchsize = 512

cuda = torch.cuda.is_available()

classes = ('plane', 'car', 'bird', 'cat',
           'deer', 'dog', 'frog', 'horse', 'ship', 'truck')

# Get the mean and std deviation of dataset
def data_param ():
    cifar_trainset = torchvision.datasets.CIFAR10(root='./data', train=True, download=True)
    data = cifar_trainset.data / 255 # data is numpy array
    mean = data.mean(axis = (0,1,2))
    std = data.std(axis = (0,1,2))
    return mean, std

# Implement transforms on train set - (RandomCrop 32, 32 (after padding of 4) >> FlipLR >> Followed by CutOut(8, 8))
def train_transform_func(mean, std):
    train_transform = A.Compose(
      [
      #RandomCrop 32, 32 (after padding of 4)
      #FlipLR -pytorch library similar present as horizontal flip
      #CutOut(8x8)
      # Pad 4
      A.PadIfNeeded(min_height=32+4, min_width=32+4),
      A.RandomCrop(height = 32, width = 32, always_apply=False, p=1.0),
      A.HorizontalFlip(p = 0.1),
      A.Cutout(num_holes=1, max_h_size=8, max_w_size=8,  fill_value=tuple(mean)),
      A.Normalize(mean=mean, std=std),
      ToTensorV2(),
      ]
    )
    return lambda img:train_transform(image=np.array(img))["image"]

# Implement test transforms (normalize the dataset and convert to tensor)
def test_transform_func(mean, std):
    test_transform = transforms.Compose([
                                        transforms.ToTensor(),
                                        transforms.Normalize(mean=mean, std=std)
                                        ])
    return test_transform
