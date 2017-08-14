# python 2 and 3 are both necessary.
# Spearmint only supports python 2.
# SMAC3 only supports python 3.

# install necessary dependencies if not present
apt-get update
apt-get install python python3 python-pip python3-pip git -y
apt-get install python-tk python3-tk -y # necessary for Docker image

# install necessary python packages
bash skopt_py2.sh
bash skopt_py3.sh

# install dask for distributed computing
# also installs many necessary dependencies
pip install dask[complete]
pip3 install dask[complete]

# install hyperopt
pip install hyperopt
pip3 install hyperopt

# install GPyOpt
pip install Gpy
pip3 install Gpy
pip install GpyOpt
pip3 install GpyOpt

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
apt-get install swig -y
cd
git clone https://github.com/automl/SMAC3.git
cd SMAC3
cat requirements.txt | xargs -n 1 -L 1 pip install
python setup.py install
cd $the_script_path

echo "Please run 'sudo service mongod start' in terminal before using 'spearmint_minimize'"

