import os
from setuptools import setup
from setuptools import find_packages

setup(
    name='gym2dmc',
    version='1.0.0',
    author='',
    description=('a dmc like wrapper for gym environment'),
    license='',
    keywords='gym dm_control openai deepmind',
    packages=find_packages(),
    install_requires=[
        'dm_control',
    ],
    extras_require={
        'develop': ['pytest']
    }
)