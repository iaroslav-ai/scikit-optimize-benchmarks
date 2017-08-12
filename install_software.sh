#!/usr/bin/env bash

# python 2 and 3 are both necessary.
# Spearmint only supports python 2.
# SMAC3 only supports python 3.

# install necessary dependencies if not present
apt-get update
apt-get install python python3 python-pip python3-pip git -y
apt-get install python-tk python3-tk -y # necessary for Docker image

# install necessary python packages
pip install -r requirements.txt
pip3 install -r requirements.txt

# install hyperopt
pip install hyperopt
pip3 install hyperopt

# install GPyOpt
pip install Gpy
pip3 install Gpy
pip install GpyOpt
pip3 install GpyOpt

# install dask for distributed computing
pip install dask[complete]
pip3 install dask[complete]

# install mongodb (necessary for spearmint)
pip install pymongo
bash mongod_install.sh
service mongod start
the_script_path=$PWD

# install spearmint
cd
git clone https://github.com/HIPS/Spearmint.git
cd Spearmint
pip install -e .
cd $the_script_path

# install SMAC3
apt-get install swig
pip3 install https://github.com/automl/SMAC3/archive/master.zip




echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
echo "Please run 'sudo service mongod start' in terminal before using 'spearmint_minimize'"
echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"