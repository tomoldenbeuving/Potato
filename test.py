from imageai.Detection import VideoObjectDetection
import os
import cv2

camera = cv2.VideoCapture(0, cv2.CAP_DSHOW) #captureDevice = camera

# Check if the webcam is opened correctly
if not camera.isOpened():
    raise IOError("Cannot open webcam")

def forFrame(frame_number, output_array, output_count):
    print("FOR FRAME " , frame_number)
    print("Output for each object : ", output_array)
    print("Output count for unique objects : ", output_count)
    print("------------END OF A FRAME --------------")


execution_path = os.getcwd()

detector = VideoObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath( os.path.join(execution_path , "yolo.h5"))
detector.loadModel()


wat = detector.detectObjectsFromVideo(camera_input= camera, return_detected_frame= True, frames_per_second=20, log_progress=True, per_frame_function=forFrame())

try:
    print(wat)
except KeyboardInterrupt:
    quit


