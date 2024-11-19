from ultralytics import YOLO

class ImageDetector:
    def __init__(self, model_path):
        # Cargar el modelo YOLO
        self.model = YOLO(model_path)

    def detect_objects(self, image_path):
        # Realizar la predicción en la imagen
        results = self.model(image_path)
        
        # Imprimir el tipo de la variable 'results' para inspeccionar su estructura
        print(f"Tipo de 'results': {type(results)}")
        print(f"Contenido de 'results': {results}")
        
        # Verifica si 'results' es un objeto de tipo 'Results' y si tiene el método pandas()
        if isinstance(results, list):
            print("Los resultados son una lista, no un objeto de resultados esperado.")
            objects = results[0].boxes  # Accede directamente a las cajas de predicción
        else:
            # Usar pandas() para obtener el dataframe si es un objeto 'Results'
            objects = results.pandas().xywh[0]
        
        return objects

# Instancia de la clase
detector = ImageDetector("yolov8n.pt")

# Detectar objetos en una imagen
image_path = "C:/Users/risilvac/Downloads/___BASURA___/__IMG__/botellas/BOTELLA_001.png"
objects = detector.detect_objects(image_path)

# Imprimir los objetos detectados
print(objects)
