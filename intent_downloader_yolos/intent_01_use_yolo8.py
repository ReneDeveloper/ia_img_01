#intent_use_yolo8.py

from ultralytics import YOLO
import cv2

class YoloObjectDetector:
    def __init__(self, model_path="yolov8n.pt"):
        # Cargar el modelo YOLOv8 (por defecto, utilizamos el modelo preentrenado 'yolov8n.pt')
        self.model = YOLO(model_path)

    def detect_objects(self, image_path):
        # Cargar la imagen usando OpenCV
        image = cv2.imread(image_path)
        # Realizar la predicción con el modelo YOLO
        results = self.model(image)
        # Extraer los objetos detectados
        objects = results.pandas().xywh[0]  # Pandas DataFrame con los resultados
        return objects[['name', 'confidence']]  # Retornamos el nombre y la confianza de los objetos

# Uso
detector = YoloObjectDetector()
objects = detector.detect_objects("C:/Users/risilvac/Downloads/___BASURA___/__IMG__/botellas/BOTELLA_001.png")
print(objects)




#C:\Users\risilvac\AppData\Local\Programs\Python\Python38\Scripts

#C:\Users\risilvac\AppData\Local\Microsoft\WindowsApps\
