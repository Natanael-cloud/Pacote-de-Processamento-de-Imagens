# Image Processing Package

Este pacote realiza operações básicas de processamento de imagens, incluindo transformação, combinação e visualização. Ideal para projetos que necessitam manipular imagens de forma simples e eficiente.

## Estrutura do Projeto

```
image_processing/
    __init__.py
    main.py
    processing/
        __init__.py
        combination.py
        transformation.py
    utils/
        __init__.py
        io.py
        plot.py
requirements.txt
setup.py
README.md
```

## Instalação

Clone o repositório e instale as dependências:

```bash
git clone https://github.com/seu-usuario/image-processing-package.git
cd image-processing-package
pip install -e .
```

## Funcionalidades

- **Combinação de imagens:** Junte duas imagens lado a lado.
- **Transformações geométricas:** Redimensione e rotacione imagens facilmente.
- **Funções auxiliares:** Leitura, escrita e visualização de imagens.

## Exemplo de Uso

```python
from image_processing.processing import resize_image, rotate_image, combine_images
from image_processing.utils import read_image, save_image, plot_image

# Redimensionar imagem
img = resize_image('caminho/para/imagem.jpg', (200, 200))
save_image(img, 'imagem_redimensionada.jpg')

# Rotacionar imagem
img_rot = rotate_image('caminho/para/imagem.jpg', 90)
plot_image(img_rot)

# Combinar imagens
img_comb = combine_images('img1.jpg', 'img2.jpg')
save_image(img_comb, 'imagem_combinada.jpg')
```

## Requisitos

- numpy
- Pillow
- matplotlib

## Licença

Este projeto está sob a licença MIT.