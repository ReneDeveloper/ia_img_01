#test_002.py

import pytesseract as tess
from PIL import Image
import cv2

class GetTXT:
    def __init__(self, ruta_tesseract_cmd, ruta_tesseract_out, bool_show_img=False):
        self.ruta_tesseract_cmd = ruta_tesseract_cmd
        self.ruta_tesseract_out = ruta_tesseract_out
        self.bool_show_img = bool_show_img
        tess.pytesseract.tesseract_cmd = f'{self.ruta_tesseract_cmd}tesseract.exe'

    def process_image(self, img_path, id, x1, y1, x2, y2):
        # Leer la imagen
        my_image = cv2.imread(img_path)
        
        # Recortar la región del polígono especificado
        cropped_image = my_image[y1:y2, x1:x2]

        # Guardar la imagen recortada
        output_image_path = f"{self.ruta_tesseract_out}{id}.png"
        cv2.imwrite(output_image_path, cropped_image)
        
        # Extraer el texto de la imagen recortada
        txt = tess.image_to_string(cropped_image)

        # Guardar el texto en un archivo
        output_txt_path = f"{self.ruta_tesseract_out}{id}.txt"
        with open(output_txt_path, "w", encoding="utf-8") as txt_file:
            txt_file.write(txt)

        # Mostrar la imagen recortada si bool_show_img es True
        if self.bool_show_img:
            cv2.imshow('Cropped Image', cropped_image)
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
    img_path = 'C:/Users/risilvac/Downloads/PERSONAL/tesseract-ocr-w64-setup-5.4.0.20240606/TEST.png'
    
    # Procesar la imagen
    get_txt_instance.process_image(img_path, id, x1, y1, x2, y2)
