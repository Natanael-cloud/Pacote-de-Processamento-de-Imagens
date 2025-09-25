from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image processing package",
    version="0.0.1",
    author="Natanael Costa",
    author_email="natanpaivacosta@gmail.com",
    description="Pacote de processamento de imagens",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Natanael-cloud/Pacote-de-Processamento-de-Imagens",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=requirements,
)
