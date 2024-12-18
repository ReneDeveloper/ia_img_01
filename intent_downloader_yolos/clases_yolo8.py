#clases_yolo8.py

from ultralytics import YOLO

# Cargar modelo YOLO
model = YOLO('yolov8n.pt')  # carga el modelo YOLO

# Obtener nombres de clases
class_names = model.names
print(class_names)



classes_en = {
    0: "person",
    1: "bicycle",
    2: "car",
    3: "motorcycle",
    4: "airplane",
    5: "bus",
    6: "train",
    7: "truck",
    8: "boat",
    9: "traffic light",
    10: "fire hydrant",
    11: "stop sign",
    12: "parking meter",
    13: "bench",
    14: "bird",
    15: "cat",
    16: "dog",
    17: "horse",
    18: "sheep",
    19: "cow",
    20: "elephant",
    21: "bear",
    22: "zebra",
    23: "giraffe",
    24: "backpack",
    25: "umbrella",
    26: "handbag",
    27: "tie",
    28: "suitcase",
    29: "frisbee",
    30: "skis",
    31: "snowboard",
    32: "sports ball",
    33: "kite",
    34: "baseball bat",
    35: "baseball glove",
    36: "skateboard",
    37: "surfboard",
    38: "tennis racket",
    39: "bottle",
    40: "wine glass",
    41: "cup",
    42: "fork",
    43: "knife",
    44: "spoon",
    45: "bowl",
    46: "banana",
    47: "apple",
    48: "sandwich",
    49: "orange",
    50: "broccoli",
    51: "carrot",
    52: "hot dog",
    53: "pizza",
    54: "donut",
    55: "cake",
    56: "chair",
    57: "couch",
    58: "potted plant",
    59: "bed",
    60: "dining table",
    61: "toilet",
    62: "tv",
    63: "laptop",
    64: "mouse",
    65: "remote",
    66: "keyboard",
    67: "cell phone",
    68: "microwave",
    69: "oven",
    70: "toaster",
    71: "sink",
    72: "refrigerator",
    73: "book",
    74: "clock",
    75: "vase",
    76: "scissors",
    77: "teddy bear",
    78: "hair drier",
    79: "toothbrush"
}

classes_es = {
    0: "persona",
    1: "bicicleta",
    2: "coche",
    3: "motocicleta",
    4: "avión",
    5: "autobús",
    6: "tren",
    7: "camión",
    8: "barco",
    9: "semáforo",
    10: "hidrante",
    11: "señal de stop",
    12: "parquímetro",
    13: "banco",
    14: "pájaro",
    15: "gato",
    16: "perro",
    17: "caballo",
    18: "oveja",
    19: "vaca",
    20: "elefante",
    21: "oso",
    22: "cebra",
    23: "jirafa",
    24: "mochila",
    25: "paraguas",
    26: "bolso",
    27: "corbata",
    28: "maleta",
    29: "frisbee",
    30: "esquís",
    31: "tabla de snowboard",
    32: "pelota deportiva",
    33: "cometa",
    34: "bate de béisbol",
    35: "guante de béisbol",
    36: "patineta",
    37: "tabla de surf",
    38: "raqueta de tenis",
    39: "botella",
    40: "copa de vino",
    41: "taza",
    42: "tenedor",
    43: "cuchillo",
    44: "cuchara",
    45: "bol",
    46: "plátano",
    47: "manzana",
    48: "sándwich",
    49: "naranja",
    50: "brócoli",
    51: "zanahoria",
    52: "perrito caliente",
    53: "pizza",
    54: "dona",
    55: "pastel",
    56: "silla",
    57: "sofá",
    58: "planta en maceta",
    59: "cama",
    60: "mesa de comedor",
    61: "inodoro",
    62: "televisión",
    63: "computadora portátil",
    64: "ratón",
    65: "control remoto",
    66: "teclado",
    67: "teléfono móvil",
    68: "microondas",
    69: "horno",
    70: "tostadora",
    71: "fregadero",
    72: "refrigerador",
    73: "libro",
    74: "reloj",
    75: "jarrón",
    76: "tijeras",
    77: "oso de peluche",
    78: "secador de pelo",
    79: "cepillo de dientes"
}

