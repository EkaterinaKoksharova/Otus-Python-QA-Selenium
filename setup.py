""" Setup скрипт для сборки setuptools """

from setuptools.dist import Distribution
from setuptools import setup, find_packages


class BinaryDistribution(Distribution):

    def is_pure(self):
        return False


setup(
    name='opencart_tests',
    version='0.3',
    url='https://github.com/EkaterinaKoksharova/Otus-Python-QA-Selenium',
    license='MIT',
    author='Koksharova Ekaterina',
    author_email='koksharova3093@gmail.com',
    description='Opencart tests',
    packages=find_packages(),
    include_package_data=True,
    distclass=BinaryDistribution,
    package_data={
        "": ["*.txt", "*.rst"],
        "hello": ["*.msg"]
    },
    long_description=open('README.md').read(),
    setup_requires=['pytest', 'selenium'],
    zip_safe=True,
    classifiers=[
        "License :: OSI Approved :: Python Software Foundation License"
    ]
)
