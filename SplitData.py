import os,shutil
from sklearn.model_selection import train_test_split

baseSourcePath="RoadSignDetection/"
dataPath="RoadData/"
# Read images and annotations
images = [os.path.join(baseSourcePath+'images', x) for x in os.listdir(baseSourcePath+'images')]
annotations = [os.path.join(baseSourcePath,'annotations', x) for x in os.listdir(baseSourcePath+'annotations') if x[-3:] == "txt"]

images.sort()
annotations.sort()

# Split the dataset into train-valid-test splits
train_images, val_images, train_annotations, val_annotations = train_test_split(images, annotations, test_size = 0.2, random_state = 1)
val_images, test_images, val_annotations, test_annotations = train_test_split(val_images, val_annotations, test_size = 0.5, random_state = 1)

os.makedirs(dataPath,exist_ok=True)
os.makedirs(dataPath+"images",exist_ok=True)
os.makedirs(dataPath+"annotations",exist_ok=True)
os.makedirs(dataPath+"images/train",exist_ok=True)
os.makedirs(dataPath+"images/val",exist_ok=True)
os.makedirs(dataPath+"images/test",exist_ok=True)
os.makedirs(dataPath+"labels/train",exist_ok=True)
os.makedirs(dataPath+"labels/val",exist_ok=True)
os.makedirs(dataPath+"labels/test",exist_ok=True)

#Utility function to move images
def copy_files_to_folder(list_of_files, destination_folder):
    for f in list_of_files:
        try:
            shutil.copy(f, destination_folder)
        except:
            print(f)
            assert False

# Move the splits into their folders
copy_files_to_folder(train_images, dataPath + 'images/train')
copy_files_to_folder(val_images, dataPath + 'images/val/')
copy_files_to_folder(test_images, dataPath + 'images/test/')
copy_files_to_folder(train_annotations, dataPath + 'labels/train/')
copy_files_to_folder(val_annotations, dataPath + 'labels/val/')
copy_files_to_folder(test_annotations, dataPath + 'labels/test/')






