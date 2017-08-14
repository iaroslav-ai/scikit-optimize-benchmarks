"""
Example of running the benchmarks locally
on skopt and other software.
"""

from bbob.evaluation import parallel_evaluate, plot_results, calculate_metrics
from skopt import forest_minimize
from bbob.wrappers.gpyopt_minimize import gpyopt_minimize
from bbob.wrappers.hyperopt_minimize import hyperopt_minimize

from bbob.tracks.ampgo import Hartmann3_3_ri, Ackley_3_1_r

r = parallel_evaluate(
    solvers=[forest_minimize, gpyopt_minimize, hyperopt_minimize],
    task_subset=[Hartmann3_3_ri, Ackley_3_1_r],  # set to None to evaluate on all tasks
    n_reps=2, # number of repetitions
    eval_kwargs={'n_calls': 10},
    joblib_kwargs={'n_jobs': -1, 'verbose': 10})

p = calculate_metrics(r) # returns pandas dataframe
p.to_csv('data.csv')
plot_results(r)