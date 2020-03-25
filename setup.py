import setuptools
from setuptools import setup

setup(name='ericnuno',
    version='0.60',
    description='Erics common functions',
    url="https://github.com/kingmold/ericnuno",
    author='Eric Nuno',
    author_email='ericnuno@gmail.com',
    license='MIT',
    packages=setuptools.find_packages(),
    install_requires=['requests', 'paramiko', 'bs4', 'serial', 'pyserial'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"))
