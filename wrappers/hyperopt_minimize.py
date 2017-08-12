"""
RoBo
"""
from string import ascii_letters
import random
import tempfile
import pickle

import numpy as np

from hyperopt import hp, fmin, tpe

from skopt.space import Real, Integer, Categorical
from skopt.utils import point_aslist, create_result


def rnd_name():
    return ''.join([random.choice(ascii_letters) for i in range(20)])


class BenchWrapper():
    def __init__(self, func, save_to, param_types):
        self.func = func
        self.save_to = save_to
        self.param_types = param_types
        pickle.dump(([], []), open(self.save_to, 'wb'))


    def __call__(self, p):
        x = [p[k] for k in sorted(p.keys())]

        for i, t in enumerate(self.param_types):
            if isinstance(t, Integer):
                x[i] = int(x[i])

        y = self.func(x)

        Xi, yi = pickle.load(open(self.save_to, 'rb'))
        Xi.append(x)
        yi.append(y)
        pickle.dump((Xi, yi), open(self.save_to, 'wb'))

        return y


def hyperopt_minimize(func, dims, n_calls=64):

    param_names = sorted([rnd_name() for d in dims])
    search_space = dict(zip(param_names, dims))

    for k, v in search_space.items():
        if isinstance(v, Real):
            search_space[k] = hp.uniform(k, v.bounds[0], v.bounds[1])
        elif isinstance(v, Integer):
            search_space[k] = hp.quniform(k, v.bounds[0], v.bounds[1], 1)
        elif isinstance(v, Categorical):
            search_space[k] = hp.choice(k, v.categories)

    with tempfile.NamedTemporaryFile() as save_to:
        tape_recorder = BenchWrapper(func, save_to.name, dims)

        solution = fmin(
            fn=tape_recorder,
            space=hp.choice('main', [search_space]),
            algo=tpe.suggest,
            max_evals=n_calls
        )

        Xi, yi = pickle.load(open(save_to.name, 'rb'))

    return create_result(Xi, yi, dims)