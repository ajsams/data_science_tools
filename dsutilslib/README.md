# How I built and installed this libarary

Largely, I followed the setup outlined by Kia Eisinga [here](https://medium.com/analytics-vidhya/how-to-create-a-python-library-7d5aea80cc3f).

* First, I needed to be in the conda environment that lives in the parent directory of this repository. Currently that is called `datasci`.
* This process required `wheel`, `setuptools`, `twine`, `pytest`, and `pytest-runner` which are all installed in that environment.
* Within the parent folder `dsutilslib` I created the `dsutils` folder for the main library and `tests` for testing with `pytest`. 
* I also created a `setup.py` to configure the package. 
* Rather than building the library per the article linked above, I simple pip installed editable:
	* From the root of `dsutilslib` I ran: `pip install -e ./`
	* This uses the setup file to install the package as editable, so changes are automatically reflected in my local environment.

# Writing and Running tests with [pytest](https://docs.pytest.org/en/latest/getting-started.html)
Tests are configured to be located in the `tests` directory.

You can run tests from the root of `dsutilslib` with:

`python setup.py pytest` 

# Library details

