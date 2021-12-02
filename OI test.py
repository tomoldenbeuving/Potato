from imageai.Detection import ObjectDetection
import os
import time

execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath( os.path.join(execution_path, "yolo.h5"))
detector.loadModel()
detections = detector.detectObjectsFromImage(
input_image=os.path.join(execution_path , "image.jpg"), 
#output_type= "array",
output_image_path=os.path.join(execution_path , "imagenew.jpg"), 
minimum_percentage_probability=30
)

for eachObject in detections:
    print(eachObject["name"] , " : ",  "%.2f" % eachObject["percentage_probability"], " : ", eachObject["box_points"])
    print(time.asctime())
    print("--------------------------------")