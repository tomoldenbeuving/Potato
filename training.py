from imageai.Detection.Custom import DetectionModelTrainer

trainer = DetectionModelTrainer()
trainer.setModelTypeAsYOLOv3()
trainer.setDataDirectory(data_directory="C:\\Users\\Tom\\Documents\\0_Code\\AI\\putdeksel")
trainer.setTrainConfig(object_names_array=["putdeksel"], num_experiments= 200, batch_size=2)
trainer.trainModel()   

# , train_from_pretrained_model="C:\\Users\\Tom\\Documents\\0_Code\\AI\\pretrained-yolov3.h5"