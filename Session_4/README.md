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

# Code 4 -  Affect of dropout layer
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
- Parameters - 8,204
- Best training accuracy - 98.54 \%
- Best test accuracy - 97.38 \% <br/>
### **Analysis**
- Adding GAP layer decreases the number of parameters in the model.
- There is a drop in test and train accuracy of the model
- Model is still overfitting

# Code 6 - Increase the capacity of the network
### **Target**
- Increase model capacity. Add more layers at the end.
### **Results**
- Parameters - 10,764
- Best training accuracy - 99.14 \%
- Best test accuracy - 99.18 \% <br/>
### **Analysis**
- The model is not overfitting.
- Less gap between the train and test accuracy.
- In the last epochs the train accuracy has been maintained at 99.1 % and test accuracy is maintained at 99.1%

# Code 7 -  Affect of data augmentation
### **Target**
- As explained in the class I implemented rotation transformation with 7 degrees, along with normalization as a data augmentation technique. 
### **Results**
- Parameters - 10,764
- Best training accuracy - 98.96 \%
- Best test accuracy - 99.38 \% <br/>
### **Analysis**
- As expected the training accuracy decreases as we have made the dataset harder for our model.
- However the training accuracy increases consistently and reaches 99.38 \% at the 15th epoch

