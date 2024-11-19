#train.py
import os
import subprocess

# Ruta del YAML corregido
yaml_file = "intent_train_Face-Detection-3/data.yaml"

# Configura las rutas del proyecto
project_path = "C:/Users/risilvac/Downloads/___BASURA___/__IMG__/test/Face-Detection-3"
output_path = os.path.join(project_path, "runs")

# Comando para entrenar el modelo
command = [
    "python", "train.py",  # Cambia a 'train.py' en la ruta del repo YOLOv5
    "--img", "640",              # Tamaño de la imagen
    "--batch", "16",             # Tamaño del batch
    "--epochs", "50",            # Número de épocas
    "--data", yaml_file,         # Archivo YAML de configuración
    "--weights", "yolov5s.pt",   # Modelo base para transferencia
    "--project", output_path,    # Directorio para guardar resultados
    "--name", "face_detection",  # Nombre del proyecto
    "--cache"                    # Usa cache para acelerar el entrenamiento
]

# Ejecutar el comando
try:
    subprocess.run(command, check=True)
    print("Entrenamiento completado exitosamente.")
    print(f"El modelo entrenado se encuentra en: {output_path}")
except subprocess.CalledProcessError as e:
    print(f"Error durante el entrenamiento: {e}")
