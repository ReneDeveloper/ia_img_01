#ambiente.py


import sys
import os
import subprocess
import pkg_resources

class Ambiente:
    def __init__(self):
        self.python_version = sys.version
        self.python_path = sys.executable
        self.installed_packages = self.get_installed_packages()

    def get_installed_packages(self):
        # Usa pkg_resources para obtener las librerías instaladas
        packages = pkg_resources.working_set
        return [f"{pkg.key}=={pkg.version}" for pkg in packages]

    def print_ambiente(self):
        print(r"""
  __    __    __    __    __    __    __    __  
 /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \ 
| A | | M | | B | | I | | E | | N | | T | | E | |
 \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  
        """)
        
        print(f"\nAMBIENTE DETECTADO:\n")
        print(f"Python Version: {self.python_version}")
        print(f"Python Path: {self.python_path}\n")

        print("Instalado Paquetes:")
        for package in self.installed_packages:
            print(f" - {package}")
        
        print("\nFin de la información del ambiente.")

# Crear una instancia de la clase Ambiente y mostrar la información
ambiente = Ambiente()
ambiente.print_ambiente()




"""

AMBIENTE DETECTADO:

Python Version: 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)]
Python Path: C:/Users/risilvac/AppData/Local/Microsoft/WindowsApps/PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0/python.exe

Instalado Paquetes:
 - zipp==3.20.2
 - urllib3==2.2.3
 - ultralytics==8.3.29
 - ultralytics-thop==2.0.11
 - tzdata==2024.2
 - typing-extensions==4.12.2
 - tqdm==4.67.0
 - torchvision==0.19.1
 - torch==2.4.1
 - sympy==1.13.3
 - six==1.16.0
 - seaborn==0.13.2
 - scipy==1.10.1
 - requests==2.32.3
 - pyyaml==6.0.2
 - pytz==2024.2
 - python-dateutil==2.9.0.post0
 - pyparsing==3.1.4
 - py-cpuinfo==9.0.0
 - psutil==6.1.0
 - pillow==10.4.0
 - pandas==2.0.3
 - packaging==24.2
 - opencv-python==4.10.0.84
 - numpy==1.24.4
 - networkx==3.1
 - mpmath==1.3.0
 - matplotlib==3.7.5
 - markupsafe==2.1.5
 - kiwisolver==1.4.7
 - jinja2==3.1.4
 - importlib-resources==6.4.5
 - idna==3.10
 - fsspec==2024.10.0
 - fonttools==4.54.1
 - filelock==3.16.1
 - cycler==0.12.1
 - contourpy==1.1.1
 - colorama==0.4.6
 - charset-normalizer==3.4.0
 - certifi==2024.8.30
 - setuptools==56.0.0
 - pip==21.1.1

Fin de la informaci�n del ambiente.
[Finished in 2.5s]

"""