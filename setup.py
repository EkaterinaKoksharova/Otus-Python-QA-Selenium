""" Setup скрипт для сборки setuptools """

import os
import setuptools
from setuptools.dist import Distribution
from setuptools import setup, find_packages

with open('requirements.txt') as requirements:
    required = requirements.read().splitlines()

with open('README.md', "r") as readme:
    long_description = readme.read()


class BinaryDistribution(Distribution):

    def is_pure(self):
        return False


setuptools.setup(
    name='opencart_tests',
    version='0.6',
    url='https://github.com/EkaterinaKoksharova/Otus-Python-QA-Selenium',
    license='MIT',
    author='Koksharova Ekaterina',
    author_email='koksharova3093@gmail.com',
    description='Opencart tests',
    packages=find_packages(),
    include_package_data=True,
    distclass=BinaryDistribution,
    long_description=open('README.md').read(),
    setup_requires=['pytest', 'selenium'],
    zip_safe=True,
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ]
)
