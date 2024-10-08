#test_obtiene_screenshot_001.py

import pytesseract as tess
from PIL import Image
import cv2
import pyautogui
import numpy as np

class GetTXT:
    def __init__(self, ruta_tesseract_cmd, ruta_tesseract_out, bool_show_img=False):
        self.ruta_tesseract_cmd = ruta_tesseract_cmd
        self.ruta_tesseract_out = ruta_tesseract_out
        self.bool_show_img = bool_show_img
        tess.pytesseract.tesseract_cmd = f'{self.ruta_tesseract_cmd}tesseract.exe'

    def process_image(self, id, x1, y1, x2, y2):
        # Tomar screenshot del polígono especificado
        screenshot = pyautogui.screenshot(region=(x1, y1, x2 - x1, y2 - y1))

        # Generar la ruta de la imagen a partir de la ruta de salida y el ID
        output_image_path = f"{self.ruta_tesseract_out}{id}.png"
        
        # Guardar la imagen capturada
        screenshot.save(output_image_path)

        # Convertir el screenshot a un formato que OpenCV pueda leer
        screenshot_cv = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

        # Extraer el texto de la imagen capturada
        txt = tess.image_to_string(screenshot_cv)

        # Guardar el texto en un archivo
        output_txt_path = f"{self.ruta_tesseract_out}{id}.txt"
        with open(output_txt_path, "w", encoding="utf-8") as txt_file:
            txt_file.write(txt)

        # Mostrar la imagen capturada si bool_show_img es True
        if self.bool_show_img:
            cv2.imshow('Cropped Image', screenshot_cv)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        print(f"Imagen y texto procesados para el ID: {id}")

# Ejemplo de uso
if __name__ == "__main__":
    ruta_tesseract_cmd = "C:/Users/risilvac/Downloads/PERSONAL/tesseract-ocr-w64-setup-5.4.0.20240606/"
    ruta_tesseract_out = "C:/Users/risilvac/Downloads/___BASURA___/"
    get_txt_instance = GetTXT(ruta_tesseract_cmd, ruta_tesseract_out)

    # Parámetros de ejemplo
    id = "45"
    x1, y1, x2, y2 = 100, 100, 400, 400

    # Procesar la imagen
    get_txt_instance.process_image(id, x1, y1, x2, y2)
