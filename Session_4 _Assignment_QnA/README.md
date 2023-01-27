# Code 0 - Skeleton code
Following is my network architecture <br/>
![model](images/model.png)

The **results** of my model are <br/>
- Number of parameters **26,520**,
- Max training accuracy **99.78 %** at 13 epoch,
- Max test accuracy **99.39 %** at 15 epoch. <br/>

The receptive field caculation for the model is as follows <br/>
| Layer         		| Description    	        					|
|:---------------------:|:---------------------------------------------:|
| Convolution  32x32x1        		| 28x28x6                	|
| RELU activation    |                                           	|
| Pooling 28x28x6    |14x14x6                                               |
| Convolution  14x14x6        		| 10x10x16                	|
| RELU activation    |                                           	|
| Pooling 10x10x16    |5x5x16                                               |
| Flatten 5x5x16   | 400                                           	|
| Fully connected		| 400 input, 120 output     					|
| Flatten           |                                               |
| Fully connected		| 120 input, 84 output     					|
| Output         		| 84 input, 43 output     				     	|


# Code 1 - Lighter weight model (base code)
My network (from skeleton code) has 
- batch normalization, 
- GAP layer, 
- convolutional layer after gap to increase the capacity of the network, and
- A max pooling layer after receptive field of 5
- 
### **Target**
- Reduce the number of parameters in the network by reducing the number of layers in the network 
### **Results**
- Parameters - 9,752
- Best training accuracy - 99.58 %
- Best test accuracy - 99.31% at 15th Epoch
### **Analysis**
- Number of parameters is within the desired range (< 10k).
- Overfitting is observed. Model's training accuracy increases consistently however the test accuracy remains in the range of 99.28-99.3 %.


# Code 2 - Adding dropout layer
### **Target**
Adding dropout layers (dropout value = 0.1) to handle overfitting
### **Results**
- Parameters -  9,752
- Best training accuracy - 99.08 % (consistent after epoch 11)
- Best test accuracy - 99.32 % (at 11th epoch)
### **Analysis**
- Adding dropout layer has introduced stability in the training dataset. However the test dataset accuracy stops increasing after 11th epoch and toggles between 99.25-99.32%. Thus adding dropout layer doesn't have a significant effect on the test accuracy. 


# Code 3 - Adding data augmentation and StepLR
### **Target**
- Implementing data augmentation (rotation with 7 degrees variance)
- Implementing learning rate scheduler from the 6th epoch
- Removing dropout
### **Results**
- Parameters - 9,752
- Best training accuracy - 99.43 %
- Best test accuracy - 99.49 % (very consistent after 7th epoch)
### **Analysis**
- After adding data augmentation and LR scheduler model is not overfitting.
- Also the accuracy is increasing.
