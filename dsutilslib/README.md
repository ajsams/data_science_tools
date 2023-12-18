# How I built and installed this libarary

Largely, I followed the setup outlined by Kia Eisinga [here](https://medium.com/analytics-vidhya/how-to-create-a-python-library-7d5aea80cc3f).

* First, I needed to be in the conda environment that lives in the parent directory of this repository. Currently that is called `datasci`.
* This process required `wheel`, `setuptools`, `twine`, `pytest`, and `pytest-runner` which are all installed in that environment.
* Within the parent folder `dsutilslib` I created the `dsutils` folder for the main library and `tests` for testing with `pytest`. 
* I also created a `setup.py` to configure the package. 
* I built the library from `dsutilslib` with `python setup.py bdist_wheel`
* Then I installed the library to my current environment with `pip install dist/dsutils-0.1.0-py3-none-any.whl`

# Writing and Running tests with [pytest](https://docs.pytest.org/en/latest/getting-started.html)
Tests are configured to be located in the `tests` directory.

You can run tests from the root of `dsutilslib` with:

`python setup.py pytest` 

# Library details

