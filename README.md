#Train Yolov5
for reference 
https://blog.paperspace.com/train-yolov5-custom-data/
Git reference  https://github.com/ultralytics/yolov5


download Trafric Road_Sign_Dataset and process with 


For data preparation from Poascal data formet here is files https://github.com/ParmpalSinghGill/YoloDataPreration

As we expect we have data in images and label folder further containing train, val and test
with 
python Convertannotations.py
python SplitData.py

In labels their is text file containing 
Labelindex     centerx,       centery,     width,       height
0      0.517 0.658 0.145  0.423

Make file road_sign_data.yaml with content 
With content 
train: ../Road_Sign_Dataset/images/train/ 
val:  ../Road_Sign_Dataset/images/val/
test: ../Road_Sign_Dataset/images/test/

# number of classes
nc: 4

# class names
names: ["trafficlight","stop", "speedlimit","crosswalk"]

Define parameter in  hyp.scratch.yaml and model at yolov5s.yaml

And run
python train.py --img 640 --cfg yolov5s.yaml --hyp hyp.scratch.yaml --batch 32 --epochs 100 --data road_sign_data.yaml --weights yolov5s.pt --workers 24 --name yolo_road_det

Boom training Start
