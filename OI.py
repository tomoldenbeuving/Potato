from imageai.Detection.Custom import CustomObjectDetection
import os

execution_path = os.getcwd()

detector = CustomObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath( os.path.join(execution_path, "putdekselmodel.h5"))
detector.setJsonPath(os.path.join(execution_path, "detection_config.json"))
detector.loadModel()
detections = detector.detectObjectsFromImage(
input_image=os.path.join(execution_path , "image.jpg"), 
output_image_path=os.path.join(execution_path , "imagenew.jpg"), 
minimum_percentage_probability=30
)

for eachObject in detections:
    print(eachObject["name"] , " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"] )
    print("--------------------------------")