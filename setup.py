import io
import os
import re

from setuptools import setup
from setuptools import find_packages

def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type(u"")
    with io.open(filename, mode="r", encoding="utf-8") as f:
        return re.sub(text_type(r':[a-z]+:`~?(.*?)`'), text_type(r'``\1``'), f.read())

setup(
    name="pyFinancialAnalysis",
    version="1.0.2",
    url="https://github.com/SebastianUrdaneguiBisalaya/pyFinancialAnalysis",
    license="MIT",
    
    author="Sebastian Marat Urdanegui Bisalaya",
    author_email="sebasurdanegui@gmail.com",
    
    description="",
    long_description=read("./README.md"),
    
    packages=find_packages(exclude=("tests",)),
    py_modules=["informations", "analysis", "graphics", "dashboard"],
    
    install_requires=[i.strip() for i in open("requirements.txt").readlines()],
    
    classifiers=[
            'Development Status :: 2 - Pre-Alpha',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2 :: Only',
            'Programming Language :: Python :: 2.3',
            'Programming Language :: Python :: 2.4',
            'Programming Language :: Python :: 2.5',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3 :: Only',
            'Programming Language :: Python :: 3.0',
            'Programming Language :: Python :: 3.1',
            'Programming Language :: Python :: 3.2',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
            'Programming Language :: Python :: 3.11',
            'Programming Language :: Python :: 3.12',
        ],
)