"""
hyperopt, scikit-optimize, spearmint, GPyOpt, RoBo, SMAC3
"""
from subprocess import Popen
import subprocess
from string import ascii_letters
import random
import zlib
import numpy as np
import os
import signal

from skopt.space import Real, Integer, Categorical
from skopt.utils import point_aslist, create_result

spearmint_home = "~/Spearmint/spearmint/main.py"

import contextlib
import os
import shutil
import tempfile
import sys

def rnd_name():
    return ''.join([random.choice(ascii_letters) for i in range(20)])


def decompress_array(a):
    return np.fromstring(zlib.decompress(a['value'].decode('base64'))).reshape(a['shape'])


def spearmint_minimize(func, dims, n_calls=64):

    param_names = sorted([rnd_name() for d in dims])
    search_space = dict(zip(param_names, dims))
    variables = {}

    for k, v in search_space.items():
        if isinstance(v, Real):
            variables[k] = {
                "type": "FLOAT",
                "size": 1,
                "min": v.bounds[0],
                "max": v.bounds[1]
            }
        elif isinstance(v, Integer):
            variables[k] = {
                "type": "INT",
                "size": 1,
                "min": v.bounds[0],
                "max": v.bounds[1]
            }
        elif isinstance(v, Categorical):
            variables[k] = {
                "type": "ENUM",
                "size": 1,
                "options": v.categories,
            }

    experiment_name = "exp_" + rnd_name()

    cfg = {
        "language": "PYTHON",
        "main-file": "objective.py",
        "experiment-name": experiment_name,
        "polling-time": 0.1,
        "max-finished-jobs": n_calls+1,
        "variables": variables
    }

    obj_runner = """
import numpy as np
import math
import os
import pickle

loc = os.path.dirname(os.path.realpath(__file__))
loc = os.path.join(loc, 'objective.py.bin')
obj_func = pickle.load(open(loc, 'rb'))

# Write a function like this called 'main'
def main(job_id, params):
    params = [params[k][0] for k in sorted(params.keys())]
    return obj_func(params)
"""


    exp_loc = tempfile.mkdtemp()
    print(exp_loc)

    obj_fnc =os.path.join(exp_loc, 'objective.py')
    obj_pic = obj_fnc + ".bin"

    import pickle

    with open(obj_fnc, 'w') as f:
        f.write(obj_runner)

    with open(obj_pic, 'wb') as f:
        pickle.dump(func, f)

    import json

    json.dump(cfg, open(os.path.join(exp_loc, 'config.json'), 'w'))

    if sys.version[0] == '2':
        python_executive = 'python'
    elif sys.version[0] == '3':
        python_executive = 'python3'
    else:
        raise EnvironmentError('Unsupported version of python: %s' % sys.version)

    command = python_executive + " " + spearmint_home + " " + exp_loc

    # https://stackoverflow.com/questions/4789837
    proc = Popen(
        [command],
        stdout=subprocess.PIPE,
        shell=True,
        preexec_fn=os.setsid
    )

    from pymongo import MongoClient
    col = MongoClient()['spearmint'][experiment_name + ".jobs"]

    import time
    while True:
        current_n = len(list(col.find({})))
        time.sleep(0.001)
        if current_n > n_calls:
            os.killpg(os.getpgid(proc.pid), signal.SIGTERM)
            break

    all_jobs = list(col.find({}))

    D = []

    for job in all_jobs:
        if job['status'] != 'complete':
            continue
        p = job['params']
        t = job['start time']
        y_value = job['values']['main']
        p_dict = {k: decompress_array(v['values'])[0] for k, v in p.items()}
        D.append((t, p_dict, y_value))

    D.sort(key=lambda x: x[0])
    D = D[:n_calls]
    X = [point_aslist(search_space, d[1]) for d in D]
    y = [d[2] for d in D]

    shutil.rmtree(exp_loc)

    return create_result(X, y, dims)