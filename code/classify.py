import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

basepath = os.path.expanduser("~")
path = basepath + "/Projects/manclass"

file_dir = path + "/images"

image_paths = []
for root, dirs, files in os.walk(file_dir):
    for file in files:
        if file.endswith('.jpg'):
            image_paths.append(file)

classifications = []
for image_path in image_paths:
    image = mpimg.imread(f"{file_dir}/{image_path}")
    plt.imshow(image)
    plt.show()
    race = input("Race ID: ")
    while race not in ["1", "3", "5", "7", "9", "-"]:
        race = input("Enter a valid race ID: ")
    classifications.append([image_path, race])
