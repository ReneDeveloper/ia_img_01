#intent_train_00.py


from ultralytics import YOLO

# Cargar un modelo YOLO preentrenado (elige el tamaño adecuado: yolov8n.pt, yolov8s.pt, etc.)
model = YOLO('C:/Users/risilvac/Downloads/___BASURA___/__MODELS__/yolov8n.pt')  # Usa yolov8s.pt, yolov8m.pt, etc., si necesitas mayor precisión

# Entrenar el modelo con los datos especificados en data.yaml
model.train(data="data.yaml", epochs=50, imgsz=640, batch=16)

print("Entrenamiento completado.")

