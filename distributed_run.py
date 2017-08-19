"""
Example how to run evaluation on multiple machines with dask
"""

import distributed.joblib
import pickle as pc

from joblib import parallel_backend
from skopt import gp_minimize, dummy_minimize, forest_minimize
from bbob.evaluation import parallel_evaluate, plot_results, calculate_metrics

#from bbob.wrappers.spearmint_minimize import spearmint_minimize
from bbob.wrappers.smac_minimize import smac_minimize
#from bbob.wrappers.gpyopt_minimize import gpyopt_minimize
#from bbob.wrappers.hyperopt_minimize import hyperopt_minimize
import random

run_with_dask = False
dask_scheduler = "34.213.78.238:8786"  # example scheduler address

res_name = ''.join([random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(15)]) + ".py2.bin"

def run():
    r = parallel_evaluate(
        solvers=[smac_minimize, ],
        task_subset=None,  # automatically selects all tasks
        n_reps=1,
        eval_kwargs={'n_calls': 64},
        joblib_kwargs={'n_jobs': 1, 'verbose': 1000})
    # it is a good idea to cache results
    pc.dump(r, open(res_name, 'wb'))

if run_with_dask:
    with parallel_backend('dask.distributed', scheduler_host=dask_scheduler):
        run()
else:
    run()

# load cached results
"""
r = pc.load(open(res_name, 'rb'))
p = calculate_metrics(r)  # returns panda's dataframe
p.to_csv('data.csv')
plot_results(r)
"""