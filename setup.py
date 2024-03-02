from setuptools import setup, find_packages

setup(
    name="deepfake_image_detection",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "torch",
        "transformers",
        "Pillow"
    ],
)
