from setuptools import setup, find_packages

setup(
    name='python-hw',
    version='0.0.1',
    description='DexMate Python homework',
    author='Yijun Tang',
    author_email='yijuntang94@gmail.com',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'Faker',
        'matplotlib'
    ],
)
