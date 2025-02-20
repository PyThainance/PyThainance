from setuptools import setup, find_packages

setup(
    name="pythainance",
    version="0.0.7",
    author="Warit Mahitti",
    author_email="mrwaritmahitti@gmail.com",
    description="AI financial analysis library for Thai financial data",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/PyThainance/PyThainance.git",
    packages=find_packages(),
    include_package_data=True,
    package_data={
    "pythainance": ["dataset/*.xlsx", "dataset/*.txt", "dataset/backup_dataset/*.xlsx"],
    },
    install_requires=[
        "pandas",
        "matplotlib",
        "seaborn",
        "openpyxl",
        "playwright",
        "beautifulsoup4"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
