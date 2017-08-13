import sys

from skopt import gp_minimize
from wrappers.gpyopt_minimize import gpyopt_minimize
from wrappers.hyperopt_minimize import hyperopt_minimize

if sys.version[0] == '3':
    from bbob.wrappers import smac_minimize
    methods = [gp_minimize, gpyopt_minimize, hyperopt_minimize, smac_minimize]
else:
    from bbob.wrappers import spearmint_minimize
    methods = [gp_minimize, gpyopt_minimize, hyperopt_minimize, spearmint_minimize]

from bbob.evaluation import parallel_evaluate, calculate_metrics
from bbob.tracks import ampgo

r = parallel_evaluate(
    solvers=methods,
    task_subset=[ampgo.Ackley_3_1_r],
    n_reps=3,
    joblib_kwargs={
        'verbose': 10,
        'n_jobs': 1
    },
    eval_kwargs={
        'n_calls': 10
    }
)

#plot_results(r)
m = calculate_metrics(r)
m.to_csv('data.csv')