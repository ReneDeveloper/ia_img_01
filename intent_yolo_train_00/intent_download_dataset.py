#intent_download_dataset.py


#pip install roboflow

#from roboflow import Roboflow
#rf = Roboflow(api_key="F1jp2K3MUhSu4hH37lDa")
#project = rf.workspace("chameleonagile").project("hard-hat-sample-iacbv")
#version = project.version(1)
#dataset = version.download("yolov8")
                


# Instalar la biblioteca de Roboflow si no la tienes instalada
# !pip install roboflow

from roboflow import Roboflow
import shutil

# Autenticación con la API Key de Roboflow
rf = Roboflow(api_key="F1jp2K3MUhSu4hH37lDa")
project = rf.workspace("chameleonagile").project("hard-hat-sample-iacbv")
version = project.version(1)

# Descargar el dataset a una ubicación temporal
dataset = version.download("yolov8")

# Mover los datos descargados a la ruta deseada
dest_path = "C:\\Users\\risilvac\\Downloads\\___BASURA___\\__IMG__\\test"

# La carpeta que se descarga en "dataset.location" es temporal. La movemos a la ruta final
shutil.move(dataset.location, dest_path)

print(f"Dataset descargado y movido a {dest_path}")
