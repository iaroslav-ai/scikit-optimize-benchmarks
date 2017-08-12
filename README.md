# Benchmarks and Interfaces for Black Box Optimization Software

The interfaces are available to following software:

* [scikit-optimize](https://github.com/scikit-optimize/scikit-optimize/) (native support)
* [spearmint](https://github.com/HIPS/Spearmint) (python 2 only)
* [smac3](https://github.com/automl/SMAC3) (python 3 only)
* [gpyopt](https://github.com/SheffieldML/GPyOpt)
* [hyperopt](https://github.com/hyperopt/hyperopt)

Repository also contains a set of benchmarks intended for testing black
box optimization algorithms. Some are inspired by practical problems,
and many originate from literature and are based on [sigopt's evalset](https://github.com/sigopt/evalset) .

## Installation on Ubuntu - like systems ##

* To benchmark `scikit-optimize` only: `sudo bash skopt_py2.sh` or
`sudo bash skopt_py3.sh` depending whether you use python 2 or 3.

* Run `sudo bash full_install.sh` .

If any of this fails at some point, let us know!


## Docker image ##

```
sudo docker run -t -i iaroslavai/scikit-optimize-benchmarks /bin/bash
```

## Run on a single machine ##

```python
from tracks.ampgo import Hartmann3_3_ri, Ackley_3_1_r
from evaluation import parallel_evaluate, plot_results, calculate_metrics

from skopt import forest_minimize
from wrappers.hyperopt_minimize import hyperopt_minimize
from wrappers.gpyopt_minimize import gpyopt_minimize

r = parallel_evaluate(
    solvers=[forest_minimize, gpyopt_minimize, hyperopt_minimize],
    task_subset=[Hartmann3_3_ri, Ackley_3_1_r],  # set to None to evaluate on all tasks
    n_reps=2, # number of repetitions
    eval_kwargs={'n_calls': 10},
    joblib_kwargs={'n_jobs': -1, 'verbose': 10})

p = calculate_metrics(r) # returns pandas dataframe
p.to_csv('data.csv')
plot_results(r)
```



## Results

To reproduce, run `python run_all_tests.py`. Every number shown below is

lower confidence bound < mean < upper confidence bound,

where 95% confidence interval is computed using bootstrapping method.
Results below are for 128 runs with 64 calls budget for every problem.

|Method|Branin|Hart6|Select2Features|Train4LayerNN|
|------|------|-----|---------------|-------------|
forest_minimize|0.856<1.15<1.378|-2.945<-2.898<-2.855|-0.398<-0.39<-0.382|-1.005<-0.998<-0.99
gp_minimize|0.398<0.398<0.398|-3.264<-3.219<-3.183|-0.388<-0.379<-0.37|-1.093<-1.087<-1.082
dummy_minimize|1.126<1.295<1.451|-1.854<-1.779<-1.702|-0.369<-0.362<-0.355|-0.789<-0.773<-0.757


### Contributions ###

All contributions are welcome! :)

If you want to add a benchmark, consider this:

* It needs to have practical relevance and solving corresponding
optimization problem should clearly be valuable. For example, minimizing
random polynomials of power 3 is unlikely to be a problem encountered in
practice. Optimizing components of some medication to improve patient
recovery rate is.
* It needs to simulate a task, where the objective is unknown or complex,
and is expensive to evaluate.
* It needs to run quickly, so that benchmarking does not take days and
 so that progress can be done quickly. A speed - up for realistic
 optimization problem can be obtained by learning predictive models
 from the data to simulate actual objective function.
* It should be hard to guess [near] global optimal value with small
number of random guesses, that is, the problem should not be "easy".
This can be verified by running the dummy_minimize
procedure for many iterations. If the objective does not improve after
small number of iterations, it implies that optimization task is not
too complex.