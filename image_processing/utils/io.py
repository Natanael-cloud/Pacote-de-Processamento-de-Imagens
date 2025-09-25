
from PIL import Image

def read_image(image_path):
    """Lê a imagem do caminho especificado"""
    return Image.open(image_path)

def save_image(image, save_path):
    """Salva a imagem no caminho especificado"""
    image.save(save_path)
