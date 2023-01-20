# Code 1 - The skeleton
### **Target** 
- Setting up the skeleton 
- Adding batch normalization to the layers <br/>
### **Results** 
- Parameters - 11,844
- Best training accuracy - 99.91 \%
- Best test accuracy - 99.34 \% <br/>
### **Analysis**
- Model is overfitting
- Dropout layers need to be introduced to reduce the gap between training and test dataset <br/>
<br/>

# Code 2 - Adding gap layer
### **Target** 
- Reducing the layers to decrease the number of parameters
- Introducing dropout layers
- Adding gap layers instead of the last convolution layer <br/>
### **Results** 
- Parameters - 9,308
- Best training accuracy - 98.93 \%
- Best test accuracy - 98.84 \% <br/>
### **Analysis**
- Model is not overfitting
- After adding GAP layer the accuracy of both training and test sets have reduced. 
- However after adding dropout layer, the gap between test and training accuracy is reduced. 
- Note- Just for reference I first introduced the gap layer and than added the dropout layer. The dropout layer reduced the accuracy of the training set, however it did not have any significant affect on the accuracy of test dataset.

# Code 3 -  Increased capacity
### **Target**

### **Results**

### **Analysis**

# Code 4 -  Image Augmentation
### **Target**

### **Results**

### **Analysis**

# Code 5 -  Learning rate
### **Target**

### **Results**

### **Analysis**
