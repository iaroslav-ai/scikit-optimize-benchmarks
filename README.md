# Benchmarks and Interfaces for Black Box Optimization Software

The interfaces are available to following software:

* [scikit-optimize](https://github.com/scikit-optimize/scikit-optimize/) (native support)
* [spearmint](https://github.com/HIPS/Spearmint) (python 2 only)
* [smac3](https://github.com/automl/SMAC3) (python 3 only)
* [gpyopt](https://github.com/SheffieldML/GPyOpt)
* [hyperopt](https://github.com/hyperopt/hyperopt)

Repository contains a set of benchmarks intended for testing black
box optimization algorithms. Some are inspired by practical problems,
and many originate from literature and are based on [sigopt's evalset](https://github.com/sigopt/evalset) .


## Aggregated results

|Method|Average rank (less is better)|
|------|------------|
dummy_minimize | 3.931
forest_minimize | 2.172
gbrt_minimize | 1.966
gp_minimize | 1.138
gpyopt_minimize | 0.897
hyperopt_minimize | 2.845

Important note: these results need not generalize to the problems which
are largely different from problems in the evaluation set.

See below how these results are calculated.

## Installation on Ubuntu - like systems ##

* To benchmark `scikit-optimize` only: `sudo bash skopt_py2.sh` or
`sudo bash skopt_py3.sh` depending whether you use python 2 or 3.

* Run `sudo bash full_install.sh` .

If any of this fails at some point, let us know!


## Docker image ##

Has all of necessary software installed. Requires you to run mongo in
a screen in order to run spearmint.

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



## How performance is calculated

Results can be found in `results_history` folder, in `.csv` file
 with the latest date. To reproduce, run `python distributed_run.py`
 with `n_reps >= 64`.

Every entry in such `csv` file corresponds to performance of some
algorithm on some problem. Such entries consist of 3 values:
lower confidence bound < mean < upper confidence bound,
where 95% confidence interval is computed using bootstrapping method.

On every test optimization problem algorithms are ranked based on their
relative performance. A rank of some algorithm is a number of other
algorithms that significantly (based on derived interval) improve over
the algorithm. Consider example results below:

| A | B | C | D |
|---|---|---|---|
3<4<5|0<1<2|-1<0<1|-4<-2<-1|

Rank A = 3, B = 1, C = 1, D = 0. The rank for B and C is the same, as their
confidence intervals overlap. A large number of repetitions is used
to reduce the size of such intervals.

Confidence intervals and large number of iterations is used because
of empirical observation that results with small number of iterations
often cannot be reproduced and hence are unreliable.

## Contributions

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