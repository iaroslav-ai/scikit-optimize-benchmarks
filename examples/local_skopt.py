"""
Example of running the benchmarks locally on skopt
only
"""

from skopt import dummy_minimize, forest_minimize
from evaluation import parallel_evaluate, plot_results, calculate_metrics
from tracks.ampgo import Hartmann3_3_ri, Ackley_3_1_r

r = parallel_evaluate(
    solvers=[forest_minimize, dummy_minimize, ],
    task_subset=[Hartmann3_3_ri, Ackley_3_1_r],  # set to None to evaluate on all tasks
    n_reps=10, # number of repetitions
    eval_kwargs={'n_calls': 32},
    joblib_kwargs={'n_jobs': -1, 'verbose': 10})

p = calculate_metrics(r) # returns pandas dataframe
p.to_csv('data.csv')
plot_results(r)