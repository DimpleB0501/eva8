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


# Code 1 - Lighter weight model
### **Target**
### **Results**
### **Analysis**



# Code 2 - Adding dropout layer
### **Target**
### **Results**
### **Analysis**



# Code 3 - Adding data augmentation and StepLR
### **Target**
### **Results**
### **Analysis**
