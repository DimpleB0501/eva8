# import the modules
import os
from os import listdir
import matplotlib.pyplot as plt

n_row, n_col = 4, 4

image_jpg = []
# get the path/directory
folder_dir = "/home/dimple/Desktop/plot_images/out_images/"
for images in os.listdir(folder_dir):

    # check if the image ends with png
    if (images.endswith(".jpg")):
        image_jpg.append(folder_dir+images)

_, axs = plt.subplots(n_row, n_col, figsize=(12, 12))
axs = axs.flatten()
for img_path, ax in zip(image_jpg, axs):
    print (img_path)
    img = plt.imread(img_path)
    ax.imshow(img)
    ax.tick_params(left = False, right = False , labelleft = False , labelbottom = False, bottom = False)
plt.show()
