# AJAN-POMDP Service
A POMDP Service for AJAN

## Installation
- Create an environment in conda using the ajan_pomdp_py.yml file. Typically, done using the following command:
```conda env create -f ajan_pomdp_py.yml```
 
- Install the requirements.txt file using pip
```pip install -r requirements.txt```
- If installation of pomdp_py fails, install it using the 'install as a developer' as mentioned in https://h2r.github.io/pomdp-py/html/installation.html
- The requirements use Cython and other OS specific packages like pygraphviz, which may require additional installation steps. pygraphviz tends to fail so search for a wheel file for your machine and install it before pomdp_py.


## Usage
```python.exe -m uvicorn main:app --reload```
To start the application, run the main.py file using uvicorn since FastAPI is used.

## Ports
- The application runs on port `8000` by default.

## Tech Stack
buvnswrn/ajan_pomdp_py is built on the following main stack:

- <img width='25' height='25' src='https://img.stackshare.io/service/993/pUBY5pVj.png' alt='Python'/> [Python](https://www.python.org) – Languages
- <img width='25' height='25' src='https://img.stackshare.io/service/586/n4u37v9t_400x400.png' alt='Docker'/> [Docker](https://www.docker.com/) – Virtual Machine Platforms & Containers

Full tech stack [here](/techstack.md)
