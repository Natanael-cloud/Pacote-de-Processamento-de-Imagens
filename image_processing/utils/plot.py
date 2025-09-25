
import matplotlib.pyplot as plt

def plot_image(image):
    """Exibe a imagem em um gráfico"""
    plt.imshow(image)
    plt.axis('off')  # Remove os eixos
    plt.show()
