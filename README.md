# Python Homework
DexMate Python homework for interview

## Setup Env

You should install python first if there is no python 3.x installation. See more details on Python Offcial site.

Switch to your virtual environment of python, or create a new one:
```sh
# switch to your project root folder
# create a new virtual env (optional)
python -m venv <your venv>

# activate virtual env on Linux or macOS
source <your venv>/bin/activate
```

## Running Unit Tests

```sh
# install dependencies in editable mode
pip install -e .

# running unit tests
python tests/test.py
```
If everything goes well, the following message would display:
```sh
----------------------------------------------------------------------
Ran xx tests in 6.624s

OK
```
