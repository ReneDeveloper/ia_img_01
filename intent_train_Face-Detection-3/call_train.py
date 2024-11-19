import subprocess

# Ruta al script train.py del repositorio YOLOv5
train_script = "C:/Users/risilvac/__REPOS__/ia_img_01/intent_train_Face-Detection-3/train.py"
yaml_file = "C:/Users/risilvac/Downloads/___BASURA___/__IMG__/test/Face-Detection-3/dataset.yaml"
output_path = "C:/Users/risilvac/Downloads/___BASURA___/__IMG__/test/Face-Detection-3/runs"

command = [
    "python", train_script,
    "--img", "640",
    "--batch", "16",
    "--epochs", "50",
    "--data", yaml_file,
    "--weights", "yolov5s.pt",
    "--project", output_path,
    "--name", "face_detection",
    "--cache"
]

try:
    subprocess.run(command, check=True)
    print("Entrenamiento completado exitosamente.")
except subprocess.CalledProcessError as e:
    print(f"Error durante el entrenamiento: {e}")

