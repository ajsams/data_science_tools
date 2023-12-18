# dsutils
 Data Science Environment and Utilities

# Installing Mamba/Conda

## Install [Miniforge](https://github.com/conda-forge/miniforge).

Assuming you have no active install of conda.

~~~bash
curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
bash Miniforge3-$(uname)-$(uname -m).sh
~~~

## Create and Configure [Conda](https://conda.io/projects/conda/en/latest/user-guide/index.html) Env with [Mamba](https://mamba.readthedocs.io/en/latest/) 
(see [Managing environments](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#) in Conda docs)

~~~bash
mamba env create --name datasci --file environment.yml

mamba activate datasci
~~~

If you need to update the environment after making changes to the `environment.yml` file. 

~~~bash
mamba env update --name datasci --file environment.yml --prune
~~~
Using `--name` here explicitly to ensure we are creating and updating the same environment, but this should be unnecessary if the name is correct within the `environment.yml` file. 

`--prune` will uninstall dependencies that were removed from the previous version of this environment. 

