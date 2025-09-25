
from PIL import Image

def combine_images(image_path1, image_path2):
    """Combina duas imagens lado a lado"""
    image1 = Image.open(image_path1)
    image2 = Image.open(image_path2)
    combined_image = Image.new("RGB", (image1.width + image2.width, image1.height))
    combined_image.paste(image1, (0, 0))
    combined_image.paste(image2, (image1.width, 0))
    return combined_image
