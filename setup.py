from setuptools import setup, find_packages

setup(
    name='wsv',
    version='1.1',
    packages=find_packages(),
    install_requires=[
        'reliable_txt @ git+https://github.com/jpeterburs/reliable-txt.git'
    ]
)
