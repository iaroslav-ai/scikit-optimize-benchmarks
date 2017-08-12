"""
hyperopt, RoBo
"""
from string import ascii_letters
import random
import tempfile
import pickle

import numpy as np

import GPyOpt

from skopt.space import Real, Integer, Categorical
from skopt.utils import point_aslist, create_result


def rnd_name():
    return ''.join([random.choice(ascii_letters) for i in range(20)])


class BenchWrapper():
    def __init__(self, func, save_to, transforms):
        self.func = func
        self.save_to = save_to
        self.transforms = transforms
        pickle.dump(([], []), open(self.save_to, 'wb'))


    def __call__(self, p):

        input_point = p[0]
        x = []

        for v, t in zip(input_point, self.transforms):
            if t is not None:
                v = t(v)
            x.append(v)

        y = self.func(x)

        Xi, yi = pickle.load(open(self.save_to, 'rb'))
        Xi.append(x)
        yi.append(y)
        pickle.dump((Xi, yi), open(self.save_to, 'wb'))

        return y


def gpyopt_minimize(func, dims, n_calls=64):

    param_names = sorted([rnd_name() for d in dims])
    bounds = []
    transforms = []

    for v, n in zip(dims, param_names):
        if isinstance(v, Real):
            bounds.append({'name':n, 'type': 'continuous', 'domain': v.bounds})
            transforms.append(None)
        elif isinstance(v, Integer):
            bounds.append({'name':n, 'type': 'continuous', 'domain': v.bounds})
            transforms.append(lambda x: int(np.round(x)))
        elif isinstance(v, Categorical):
            bounds.append({'name':n, 'type': 'discrete', 'domain': v.categories})
            transforms.append(None)

    with tempfile.NamedTemporaryFile() as save_to:
        tape_recorder = BenchWrapper(func, save_to.name, transforms)
        myProblem = GPyOpt.methods.BayesianOptimization(tape_recorder, bounds)
        myProblem.run_optimization(n_calls)
        Xi, yi = pickle.load(open(save_to.name, 'rb'))
        # somehow gpyopt seems to evaluate more than asked
        Xi = Xi[:n_calls]
        yi = yi[:n_calls]

    return create_result(Xi, yi, dims)