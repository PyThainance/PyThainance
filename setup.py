# setup.py

from setuptools import setup, find_packages

setup(
    name="PyThainance",
    version="0.1.0",
    author="Warit Mahitti",
    author_email="mrwaritmahitti@gmail.com",
    description="AI financial analysis library for Thai financial data",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/PyThainance/PyThainance.git",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "matplotlib",
        "seaborn",
        "openpyxl"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
