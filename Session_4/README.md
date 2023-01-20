# Code 1 - The skeleton
### **Target** 
- Setting up the skeleton 
### **Results** 
- Parameters - 11,632
- Best training accuracy - 99.11 \%
- Best test accuracy - 98.83 \% <br/>
### **Analysis**
- Number of parameters is more than the desired parameters
- Training and test accuracy is less and its plateauing <br/>

# Code 2 - Lighter weight model
### **Target**
- Reduce the number of parameters in the network
- Modify the layers to increase accuracy
### **Results**
- Parameters - 9,608
- Best training accuracy - 98.98 \%
- Best test accuracy - 99.03 \% <br/>
### **Analysis**
- Number of parameters is within limit.
- The gap between training and test accuracy is less.<br/>

# Code 3 - Including batch normalization
### **Target**
- Adding batch normalization layers
### **Results**
- Parameters - 9,804
- Best training accuracy - 99.81 \%
- Best test accuracy - 99.27 \% <br/>
### **Analysis**
- Batch normalization drastically increases the accuracy of the model
- The model is overfitting. The training accuracy of the model is continously increasing. However the test accuracy toggles between 99.1- 99.3 \%.

# Code 4 -  Effect of dropout layer
### **Target**
- Adding 2 dropout layers
### **Results**
- Parameters - 9,804
- Best training accuracy - 99.24 \%
- Best test accuracy - 98.88 \% <br/>
### **Analysis**
- Model is still overfitting. 
- There is a gap between the training and test accuracy.
- The test accuracy stills toggles but at a lower range.

# Code 5 -  Introducing GAP layer
### **Target**
- Add GAP layer and remove the last BIG kernel.
### **Results**
- Parameters - 9,804
- Best training accuracy - 99.24 \%
- Best test accuracy - 98.88 \% <br/>
- 
### **Analysis**



# Code 6 -  Effect of data augmentation
### **Target**

### **Results**

### **Analysis**

# Code 7 -  Learning rate
### **Target**

### **Results**

### **Analysis**


