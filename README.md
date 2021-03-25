# lensorg

This repository contains a Python wrapper around LENS.org API

## Installation

### Auth
to be updated.

### Local
To use or contribute to this repository, first checkout the code. Then create a new virtual environment:

```bash
$ git clone https://github.com/hcss-utils/lensorg.git
$ cd lensorg
$ python3 -m venv env
$ . env/bin/activate
```

Install the package and its dependencies
```bash
(env)$ pip install -r requirements.txt 
```

### Google colab
To use this package from google colab, run:
```bash
!pip -q --no-cache-dir install git+https://github.com/hcss-utils/lensorg.git
!pip -q --no-cache-dir install ratelimit python-dotenv
```

## Usage
* [local environment](examples/local-usage.ipynb)
* [google colab](examples/google-colab-usage.ipynb)
