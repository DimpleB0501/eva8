# Assignment 
Design a network CIFAR 10 dataset 

# Solution
### Using albumentation library and apply on training dataset:
- horizontal flip
- shiftScaleRotate
- coarseDropout (max_holes = 1, max_height=16px, max_width=1, min_holes = 1, min_height=16px, min_width=16px, fill_value=(mean of your dataset), mask_fill_value = None)

### Model
- change the architecture to C1C2C3C40 (No MaxPooling, but 3 3x3 layers with stride of 2 instead) (If you can figure out how to use Dilated kernels here instead of MP or strided convolution, then 200pts extra!)
- one of the layers must use Depthwise Separable Convolution
- one of the layers must use Dilated Convolution
- use GAP (compulsory):- add FC after GAP to target #of classes (optional)

##### Model parameters
Desired specifications
- Receptive field more than 44 
- Total Params to be less than 200k.

### Training log
##### Plot train and test accuracies


### CIFAR10 class performance 
