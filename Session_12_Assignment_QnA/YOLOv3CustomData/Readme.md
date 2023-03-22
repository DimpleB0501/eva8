# Breif overview
Following [code](https://github.com/DimpleB0501/eva8/blob/main/Session_12_Assignment_QnA/YOLOv3CustomData/YoloV3Sample.ipynb) displays the training of YOLOv3 on custom dataset.<br/>
The model is trained for 4 classes (hard hat, mask, vest, boots). <br/>
As a part of this assignment I have collected 100 images(25 images for each class) and have annotated these images using [YoloV3 Annotation Tool](https://github.com/miki998/YoloV3_Annotation_Tool) to create labels in darknet yolo format. <br/>
I trained the yolov3 model by adding the 100 images and labels to this [dataset](https://drive.google.com/file/d/1sVSAJgmOhZk6UG7EzmlRjXfkzPxmpmLy/view) which are annotated by EVA5 Students. <br/>
Apart from this I have modified the **yolov3-custom.cfg** file in the [theschoolofai's YoloV3 base code](https://github.com/theschoolofai/YoloV3) by changing the **classes** to 4 and **filters=27** (so that VOLOv3's output vector has 27 dimensions (4+1+4)*3).


# Output
### Output Images
Output of the yolov3 model trained on 16 images (4 for each class)
![out_img](./backup/images/out_images.png)

### YouTube Video
|Output video of YOLOv3 trained on custom data for Personal Protective Equipment(PPE)|
|:------------:|
|![Output video](./backup/images/ppe.gif)|
|[Youtube Link](https://youtu.be/jx3caRbWkPY)|


