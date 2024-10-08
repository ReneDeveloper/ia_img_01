#test.py
#C:\Users\risilvac\Downloads\tesseract-ocr-w64-setup-5.4.0.20240606

import pytesseract as tess
from PIL import Image
import cv2
print("inicio")


ruta_tesseract_cmd = "C:/Users/risilvac/Downloads/PERSONAL/tesseract-ocr-w64-setup-5.4.0.20240606/"
ruta_tesseract_out = "C:/Users/risilvac/Downloads/PERSONAL/tesseract-ocr-w64-setup-5.4.0.20240606/"
bool_show_img = False
tess.pytesseract.tesseract_cmd = f'{ruta_tesseract_cmd}tesseract.exe'

# my_image = Image.open('D:\\PROGRAMMING\\3-Python\\My_Virtual_Envs\\ocr_youtube\\routing.PNG')
#my_image = cv2.imread('D:\\PROGRAMMING\\3-Python\\My_Virtual_Envs\\ocr_youtube\\routing.PNG')
my_image = cv2.imread('C:\\Users\\risilvac\\Downloads\\PERSONAL\\tesseract-ocr-w64-setup-5.4.0.20240606\\TEST.png')
print("antes de image_to_string")
txt = tess.image_to_string(my_image)
print("despues de image_to_string")
print(txt)

# Display original image
if bool_show_img:
    cv2.imshow('Image', my_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# my_file = open('file1.txt', 'w')
# my_file.write(txt + '\n')
# my_file.close()

#output = tess.image_path('text_result.txt')




#https://github.com/tbcodes/python_ocr_how_to_extract_text_from_an_image_using_python_pytesseract/blob/master/ocr_yt.py

"""
#tesseract install
#https://www.youtube.com/watch?v=OutxRdkNOK4
#https://pypi.org/project/pytesseract/
#https://tesseract-ocr.github.io/tessdoc/Installation.html
#https://github.com/UB-Mannheim/tesseract/wiki
#https://github.com/UB-Mannheim/tesseract/releases/download/v5.4.0.20240606/tesseract-ocr-w64-setup-5.4.0.20240606.exe


"""

"""
https: //github.com/SupunKavinda/jekyll-theme-leaf
https://github.com/tocttou/hacker-blog
https://github.com/longpdo/neumorphism
https://github.com/slemire/slemire.github.io
"""