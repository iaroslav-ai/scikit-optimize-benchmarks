"""
Example of running the benchmarks locally
on skopt and other software.
"""

from tracks.ampgo import Hartmann3_3_ri, Ackley_3_1_r
from evaluation import parallel_evaluate, plot_results, calculate_metrics

from skopt import forest_minimize
# spearmint works only in py2
#from wrappers.spearmint_minimize import spearmint_minimize
# smac wroks only in py3
#from wrappers.smac_minimize import smac_minimize
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