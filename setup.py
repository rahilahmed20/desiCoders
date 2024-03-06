import setuptools
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="deepfake_image_detection",
    version="0.1",
    author="desiCoders",
    author_email="rahilahmed1720@gmail.com",
    description="A package which will detect that the image is real or deepfake.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rahilahmed20/desiCoders",
    project_urls={
        "Bug Tracker": "https://github.com/rahilahmed20/desiCoders/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    package_dir={'':"src"},
    packages=find_packages("src"),
    python_requires=">=3.6",
)