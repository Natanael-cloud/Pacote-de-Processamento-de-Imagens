
from PIL import Image

def resize_image(image_path, size):
    """Redimensiona a imagem para o tamanho especificado"""
    image = Image.open(image_path)
    resized_image = image.resize(size)
    return resized_image

def rotate_image(image_path, angle):
    """Rotaciona a imagem pelo ângulo especificado"""
    image = Image.open(image_path)
    rotated_image = image.rotate(angle)
    return rotated_image
