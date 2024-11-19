import argparse
from pathlib import Path

from utils.general import increment_path, check_file
from utils.torch_utils import select_device
from utils.loggers import Loggers
from train import train_one_epoch

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--weights', type=str, default='yolov5s.pt', help='initial weights path')
    parser.add_argument('--data', type=str, default='data.yaml', help='dataset.yaml path')
    parser.add_argument('--epochs', type=int, default=300, help='number of epochs')
    parser.add_argument('--batch-size', type=int, default=16, help='batch size')
    parser.add_argument('--img-size', type=int, default=640, help='image sizes (pixels)')
    parser.add_argument('--project', default='runs/train', help='save to project/name')
    parser.add_argument('--name', default='exp', help='save to project/name')
    parser.add_argument('--cache', action='store_true', help='cache images for faster training')

    opt = parser.parse_args()

    # Llama al método de entrenamiento principal
    train_one_epoch(opt)
