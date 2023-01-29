# Assignment
1. You are making 3 versions of your 4th assignment's best model (or pick one from best assignments): <br/>
- Network with Group Normalization
- Network with Layer Normalization
- Network with L1 + BN
2. You MUST: <br/>
- Write a single model.py file that includes GN/LN/BN and takes an argument to decide which normalization to include
- Write a single notebook file to run all the 3 models above for 20 epochs each
- Create these graphs:
   - Graph 1: Test/Validation Loss for all 3 models together
   - Graph 2: Test/Validation Accuracy for 3 models together
   - graphs must have proper annotation
3. Find 10 misclassified images for each of the 3 models, and show them as a 5x2 image matrix in 3 separately annotated images. 
4. Write an explanatory README file that explains:
- what is your code all about,
- how to perform the 3 normalizations techniques that we covered(cannot use values from the excel sheet shared)
- your findings for normalization techniques,
- add all your graphs
- your 3 collection-of-misclassified-images 
5. Upload your complete assignment on GitHub and share the link on LMS

# Solution
### Model
##### Following is my network's output from torch summary
![op](images/op.png)
##### Parameters
- Batch size - 128
- Optimizer - Stochastic gradient descent (SGD)
- Dropout - 0
- Scheduler - None
- Normalization techniques <br/>

| Technique                  |   Best training accuracy | Best test accuracy  |  L1 factor | number of groups |
|:--------------------------:|:------------------------:|:-------------------:|:----------:|:----------------:|
| L1 + Batch normalization   | 94.19% at 20th Epoch     | 92.01% at 1st epoch |    0.01    |       0          |    
| Layer normalization        | 99.35% at 19th Epoch     | 99.29% at 13th epoch|    0       |       0          |    
| Group normalization        | 99.45% at 19th Epoch     | 99.37% at 15th epoch|    0       |       8          |    


### 10 misclassified images for each of the 3 models
##### Network with L1 + BN
![batch](images/batch.png)
##### Network with Layer Normalization
![Layer](images/layer.png)
##### Network with Group Normalization
![group](images/group.png)
