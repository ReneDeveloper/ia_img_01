#download_modelo.py

#https://app.roboflow.com/chameleonagile



#!pip install roboflow
import shutil
from roboflow import Roboflow
rf = Roboflow(api_key="BKs8YAJPYIXWjMyoGHEV")
project = rf.workspace("facedetection-l6ulp").project("face-detection-eanjd")
version = project.version(3)
dataset = version.download("yolov8")
                
# Descargar el dataset a una ubicación temporal
#dataset = version.download("yolov8")

# Mover los datos descargados a la ruta deseada
dest_path = "C:\\Users\\risilvac\\Downloads\\___BASURA___\\__IMG__\\test"

# La carpeta que se descarga en "dataset.location" es temporal. La movemos a la ruta final
shutil.move(dataset.location, dest_path)

print(f"Dataset descargado y movido a {dest_path}")
