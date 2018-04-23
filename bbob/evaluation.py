from itertools import groupby
from types import ModuleType
import os
import pickle as pc

import numpy as np
from joblib import Parallel, delayed
import pandas as ps
from tqdm import tqdm

def single_rep_evaluate(solver, problem, n_calls=64, seed=0):
    np.random.seed(seed)
    fnc = problem()
    #print(problem)
    res = solver(fnc, fnc.space, n_calls=n_calls)
    # below is used to reduce the size of the result
    res.models = None
    res.random_state = None
    res.specs = None

    return res


def parallel_evaluate(solvers, task_subset=None, n_reps=32,
                      joblib_kwargs=None, eval_function=single_rep_evaluate, eval_kwargs=None):

    if joblib_kwargs is None:
        joblib_kwargs = {}
    if eval_kwargs is None:
        eval_kwargs = {}

    if task_subset is None:
        from bbob.tracks import all_tracks
        task_subset = all_tracks

    if isinstance(solvers, list):
        list_of_solvers = solvers
    else:
        list_of_solvers = [solvers]

    list_of_tasks = []

    if isinstance(task_subset, list):
        for task in task_subset:
            if isinstance(task, ModuleType):
                # task is a track
                list_of_tasks.extend(task.problems)
            else:
                # task is a particular problem
                list_of_tasks.append(task)
    elif isinstance(task_subset, ModuleType):
        list_of_tasks.extend(task_subset.problems)
    else:
        list_of_tasks = [task_subset]

    all_tasks = [(p, s)
        for s in list_of_solvers
        for p in list_of_tasks
        for _ in range(n_reps)]

    results = Parallel(**joblib_kwargs)(
        delayed(eval_function)(s, p, seed=i, **eval_kwargs)
        for i, (p, s) in enumerate(all_tasks)
    )

    pr = zip(all_tasks, results)

    results = {k: list(v) for k, v in groupby(pr, lambda x: x[0][1].__name__)}

    for solver, solver_res in results.items():
        results[solver] = {
            k: list(v)
            for k, v in groupby(list(solver_res), lambda x: x[0][0].__module__)
        }

    for solver, solver_res in results.items():
        for track, track_res in solver_res.items():
            solver_res[track] = {
                k: [e[1] for e in v]
                for k, v in groupby(list(track_res), lambda x: x[0][0].__name__)
            }

    return results


def plot_results(results):
    from skopt.plots import plot_convergence
    import matplotlib.pyplot as plt

    egsolver = list(results.keys())[0]

    for t in results[egsolver]:
        for p in results[egsolver][t]:
            ax = plot_convergence(*((s, results[s][t][p]) for s in results.keys()))
            ax.set_title(p)
            plt.show()


def calculate_metrics(results):
    import bootstrapped.bootstrap as bs
    import bootstrapped.stats_functions as bs_stats

    stat_dict = {}

    for s in tqdm(results):
        for t in results[s]:
            for p in results[s][t]:
                if not p in stat_dict:
                    stat_dict[p] = {}
                opts = np.array([result.fun for result in results[s][t][p]])
                stats = bs.bootstrap(opts, stat_func=bs_stats.mean, num_iterations=1000000, iteration_batch_size=100000, num_threads=-1)
                l, m, u = stats.lower_bound, stats.value, stats.upper_bound
                stat_dict[p][s] = "%s<%s<%s" % tuple(round(v, 3) for v in (l, m, u))

    from pandas import DataFrame
    # https://stackoverflow.com/questions/19258772/write-2d-dictionary-into-a-dataframe-or-tab-delimited-file-using-python
    df = DataFrame(stat_dict, index=list(results.keys()))
    df = df.T
    return df


def get_average_ranking(results):
    """
    Calculates the average rankings of algorithms over
    instances of benchmarks.
    """
    if isinstance(results, str):
        df = ps.read_csv(results)
    elif isinstance(results, ps.DataFrame):
        df = results
    else:
        df = ps.read_csv(results)

    methods = df.columns[1:]
    df = df.as_matrix()

    new_results = []

    for row in df:
        problem = row[0]
        results = row[1:]

        lmus = [[float(v) for v in s.split('<')] for s in results]
        ranks = []

        for l, m, u in lmus:
            ranks.append(sum([uu < l for ll, mm, uu in lmus])*1.0)

        new_results.append(ranks)

    mean_ranks = np.mean(new_results, axis=0)

    ranks = dict(zip(methods, mean_ranks))

    return ranks


def combine_results(results_set):
    """
    Combines multiple results objective into one.
    """

    # read results from folder if necessary
    if isinstance(results_set, str):
        result_list = []
        for f_name in tqdm(os.listdir(results_set)):
            result = pc.load(open(os.path.join(results_set, f_name), 'rb'))
            result_list.append(result)

        results_set = result_list

    base = results_set[0]

    for results in results_set[1:]:

        for s in results:
            for t in results[s]:
                for p in results[s][t]:

                    if s not in base:
                        base[s] = {}

                    if t not in base[s]:
                        base[s][t] = {}

                    if p not in base[s][t]:
                        base[s][t][p] = []

                    base[s][t][p] += results[s][t][p]

    return base
