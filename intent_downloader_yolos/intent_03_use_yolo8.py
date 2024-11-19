import json
from pathlib import Path
from ultralytics import YOLO
from PIL import Image, ImageDraw

class ImageDetector:
    def __init__(self, model_path):
        # Cargar el modelo YOLO
        self.model = YOLO(model_path)

    def detect_objects(self, image_path):
        # Realizar la predicción en la imagen
        results = self.model(image_path)

        # Obtener información de detección y prepararla para JSON y visualización
        objects = []
        image = Image.open(image_path)
        draw = ImageDraw.Draw(image)

        for obj in results[0].boxes.data.tolist():  # Si results es una lista de resultados
            x_min, y_min, x_max, y_max, confidence, class_id = obj[:6]
            obj_data = {
                "class_id": int(class_id),
                "confidence": confidence,
                "box": {
                    "x_min": int(x_min),
                    "y_min": int(y_min),
                    "x_max": int(x_max),
                    "y_max": int(y_max)
                }
            }
            objects.append(obj_data)
            # Dibujar el cuadro en la imagen
            draw.rectangle([(x_min, y_min), (x_max, y_max)], outline="red", width=2)

        # Construir las rutas de salida manualmente
        base_path = Path(image_path)
        output_image_path = base_path.parent / f"{base_path.stem}_RESULT{base_path.suffix}"
        output_json_path = base_path.parent / f"{base_path.stem}_RESULT.json"

        # Guardar la imagen con los cuadros alrededor de los objetos detectados
        image.save(output_image_path)

        # Guardar los detalles de los objetos en un archivo JSON
        with open(output_json_path, 'w') as json_file:
            json.dump(objects, json_file, indent=4)

        return objects

# Instancia de la clase y detección
detector = ImageDetector("yolov8n.pt")
image_path = "C:/Users/risilvac/Downloads/___BASURA___/__IMG__/botellas/BOTELLA_001.png"
objects = detector.detect_objects(image_path)

# Imprimir los objetos detectados
#print(objects)
print(json.dumps(objects, indent=4))