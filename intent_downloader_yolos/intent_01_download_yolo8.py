#intent_01_yolo8.py

import requests

# URLs de los modelos YOLOv8
model_urls = {
    "yolov8n": "https://huggingface.co/Ultralytics/YOLOv8/resolve/main/yolov8n.pt",
    "yolov8s": "https://huggingface.co/Ultralytics/YOLOv8/resolve/main/yolov8s.pt",
    "yolov8m": "https://huggingface.co/Ultralytics/YOLOv8/resolve/main/yolov8m.pt",
    "yolov8l": "https://huggingface.co/Ultralytics/YOLOv8/resolve/main/yolov8l.pt",
    "yolov8x": "https://huggingface.co/Ultralytics/YOLOv8/resolve/main/yolov8x.pt",
}

# Función para descargar y guardar un modelo
def download_model(name, url):
    print(f"Descargando {name}...")
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(f"{name}.pt", "wb") as f:
            f.write(response.content)
        print(f"{name} descargado y guardado como {name}.pt")
    else:
        print(f"Error al descargar {name}")

# Descargar todos los modelos
for name, url in model_urls.items():
    download_model(name, url)
