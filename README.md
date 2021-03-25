# lensorg

This repository contains a Python wrapper around LENS.org API

## Installation

### Auth
Lens API requires registration on site. You can get a scholarly free 15-day trial access or pay for the subscription. 

To get a token, go to API & Data section on the Lens site. Then press the button 'Create a token' - after creating a token, copy and save it for further usage cause the window with token appears only once

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

Add API token to `.env` file in the root dir, e.g. `token=123`


### Google colab
To use this package from google colab, run:
```bash
!pip -q --no-cache-dir install git+https://github.com/hcss-utils/lensorg.git
!pip -q --no-cache-dir install ratelimit python-dotenv
```

## Usage
* [local environment](examples/local-usage.ipynb)
* [google colab](examples/google-colab-usage.ipynb)
