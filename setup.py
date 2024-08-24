from setuptools import setup, find_packages

setup(
    name="python-hw",
    version="0.0.1",
    description="DexMate Python homework",
    author="Yijun Tang",
    author_email="yijuntang94@gmail.com",
    packages=find_packages(),
    install_requires=["pandas~=2.2.2", "numpy", "Faker~=27.4.0", "matplotlib~=3.9.2"],
)
