# How I built and installed this libarary

Largely, I followed the setup outlined by Kia Eisinga [here](https://medium.com/analytics-vidhya/how-to-create-a-python-library-7d5aea80cc3f).

First, I needed to be in the conda environment that lives in the parent directory of this repository. Currently that is called `datasci`.

This process required `wheel`, `setuptools`, `twine`, `pytest`, and `pytest-runner` which are all installed in that environment.

I created the `dsutils` folder for the main library and `tests` for testing with `pytest`. 

I also created a `setup.py` to configure the package. 