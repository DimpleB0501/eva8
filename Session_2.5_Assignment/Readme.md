# Assignment
![qs](images/ass.png)

# Solution
### First step - Create a custom data set
The first step in the assignment was to create a custom dataset that displays <br/>
- MNIST image <br/>
- MNIST label<br/>
- Generates a random number - one hot encoded (28x28)<br/>
- Addition Label (MNIST label + Random number)<br/>
Following images displays the custom dataset creation block in my colab notebook <br/>
![cd](images/custom_data.png)

### Model and training
Following are my training logs:
![ml](images/training_logs.png)

I have followed this [blog](https://github.com/zaidalyafeai/Machine-Learning/blob/master/Multi-input%20Network%20Pytorch.ipynb) to develop a neural network model thats adds 2 inputs. <br/>
The 2 inputs to my models from the custom dataset are <br/>
- MNIST image(28x28)<br/>
- One hot encoded randomly generated integer (0-9) (28x28)<br/>
There are 2 outputs from my model<br/>
- MNIST image based number classifier<br/>
- addition output of an MNIST image and random number<br/>


For visualization purpose I have tested the trained model on an image in the training set<br/>. Following image displays the ouput of the test:
![test](op.png)
