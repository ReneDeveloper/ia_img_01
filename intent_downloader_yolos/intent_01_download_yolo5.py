import ssl
import urllib.request
import os

# Crear un contexto SSL que no verifique certificados
ssl._create_default_https_context = ssl._create_unverified_context

# Definir la ruta de destino
base_path = r"C:\Users\risilvac\Downloads\___BASURA___\__MODELS__\yolov5"

# Verificar si la carpeta existe, si no, crearla
if not os.path.exists(base_path):
    os.makedirs(base_path)

# Lista de URLs y nombres de archivos
files_to_download = {
    "https://github.com/ultralytics/yolov5/releases/download/v6.2/yolov5n-cls.pt": "yolov5n-cls.pt",
    "https://github.com/ultralytics/yolov5/releases/download/v6.2/yolov5s-cls.pt": "yolov5s-cls.pt",
    "https://github.com/ultralytics/yolov5/releases/download/v6.2/yolov5m-cls.pt": "yolov5m-cls.pt",
    "https://github.com/ultralytics/yolov5/releases/download/v6.2/yolov5l-cls.pt": "yolov5l-cls.pt",
    "https://github.com/ultralytics/yolov5/releases/download/v6.2/yolov5x-cls.pt": "yolov5x-cls.pt",
    "https://github.com/ultralytics/yolov5/releases/download/v6.2/resnet18.pt": "resnet18.pt",
    "https://github.com/ultralytics/yolov5/releases/download/v6.2/resnet34.pt": "resnet34.pt",
    "https://github.com/ultralytics/yolov5/releases/download/v6.2/resnet50.pt": "resnet50.pt",
    "https://github.com/ultralytics/yolov5/releases/download/v6.2/resnet101.pt": "resnet101.pt",
    "https://github.com/ultralytics/yolov5/releases/download/v6.2/efficientnet_b0.pt": "efficientnet_b0.pt",
    "https://github.com/ultralytics/yolov5/releases/download/v6.2/efficientnet_b1.pt": "efficientnet_b1.pt",
    "https://github.com/ultralytics/yolov5/releases/download/v6.2/efficientnet_b2.pt": "efficientnet_b2.pt",
    "https://github.com/ultralytics/yolov5/releases/download/v6.2/efficientnet_b3.pt": "efficientnet_b3.pt",
}

# Descargar cada archivo
for url, output_filename in files_to_download.items():
    # Crear la ruta completa de destino para cada archivo
    output_path = os.path.join(base_path, output_filename)
    try:
        print(f"Descargando {output_filename} desde {url}...")
        urllib.request.urlretrieve(url, output_path)
        print(f"Descargado exitosamente: {output_filename}")
    except Exception as e:
        print(f"Error al descargar {output_filename}: {e}")
