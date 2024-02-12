from setuptools import setup, find_packages

setup(
    name='wsv',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'git+https://github.com/jpeterburs/reliable-txt.git'
    ]
)