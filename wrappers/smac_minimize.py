"""
hyperopt, GPyOpt, RoBo
"""
from string import ascii_letters
import random
import tempfile
import pickle

from smac.configspace import ConfigurationSpace
from ConfigSpace.hyperparameters import CategoricalHyperparameter, \
    UniformFloatHyperparameter, UniformIntegerHyperparameter
from ConfigSpace.conditions import InCondition

from smac.tae.execute_func import ExecuteTAFuncDict
from smac.scenario.scenario import Scenario
from smac.facade.smac_facade import SMAC

from skopt.space import Real, Integer, Categorical
from skopt.utils import point_aslist, create_result


def rnd_name():
    return ''.join([random.choice(ascii_letters) for i in range(20)])


class SMACBenchWrapper():
    def __init__(self, func, save_to):
        self.func = func
        self.save_to = save_to
        pickle.dump(([], []), open(self.save_to, 'wb'))


    def __call__(self, cfg, seed):
        x = [cfg[k] for k in sorted(cfg.keys())]
        y = self.func(x)

        Xi, yi = pickle.load(open(self.save_to, 'rb'))
        Xi.append(x)
        yi.append(y)
        pickle.dump((Xi, yi), open(self.save_to, 'wb'))

        return y


def smac_minimize(func, dims, n_calls=64):

    param_names = sorted([rnd_name() for d in dims])
    search_space = dict(zip(param_names, dims))

    cs = ConfigurationSpace()
    for k, v in search_space.items():
        if isinstance(v, Real):
            cs.add_hyperparameter(
                UniformFloatHyperparameter(
                    name=k, lower=v.bounds[0], upper=v.bounds[1]
                )
            )
        elif isinstance(v, Integer):
            cs.add_hyperparameter(
                UniformIntegerHyperparameter(
                    name=k, lower=v.bounds[0], upper=v.bounds[1]
                )
            )
        elif isinstance(v, Categorical):
            cs.add_hyperparameter(
                CategoricalHyperparameter(
                    name=k, choices=v.categories
                )
            )

    scenario = Scenario({
        "run_obj": "quality",  # we optimize quality (alternative runtime)
        "runcount-limit": n_calls,  # at most 200 function evaluations
        "cs": cs,  # configuration space
        "deterministic": "true"
        })


    with tempfile.NamedTemporaryFile() as save_to:
        tape_recorder = SMACBenchWrapper(func, save_to.name)
        taf = ExecuteTAFuncDict(tape_recorder)
        smac = SMAC(scenario=scenario, tae_runner=taf)
        incumbent = smac.optimize()
        Xi, yi = pickle.load(open(save_to.name, 'rb'))

    #x = point_aslist(search_space, parameters)
    #y = value

    return create_result(Xi, yi, dims)