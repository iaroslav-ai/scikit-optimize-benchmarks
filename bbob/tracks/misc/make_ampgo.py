from evalset.icml2016_tests import tests_for_nonparametric
from evalset import test_funcs

header = """from evalset.icml2016_tests import tests_for_nonparametric
from evalset import test_funcs
from skopt.space import Real, Integer
import numpy as np
import math

"""

classes = []
problems = []

for test in tests_for_nonparametric:
    nm = test['name']
    dm = test['dim']
    rs = test['res']

    int_idx = []

    postfix = "_r"

    if test['int'] is not None:
        int_idx = test['int']
        postfix += 'i'

    int_idx = str(int_idx)

    if rs is None:
        instance_name = "%s_%s" % (nm, dm)
    else:
        instance_name = "%s_%s_%s" % (nm, dm, rs)

    instance_name += postfix

    template="""class %s(test_funcs.%s):
    def __init__(self):
        super(%s, self).__init__(dim=%s)

        integer_idx = %s
        self.res = %s

        self.space = []
        for i, b in enumerate(self.bounds):
            if i in integer_idx:
                self.space.append(Integer(
                    int(math.ceil(b[0])),
                    int(math.floor(b[1]))
                ))
            else:
                self.space.append(Real(b[0], b[1]))

    def __call__(self, p):
        p = np.array(p)
        if self.res is None:
            return self.do_evaluate(p)
        return np.floor(self.res * self.evaluate(p)) / self.res
    """ % (instance_name, nm, instance_name, dm, int_idx, rs)

    classes.append(template)
    problems.append(instance_name)

module_code = header + '\n\n'.join(classes) + '\nproblems = [' + ', '.join(problems) + ']\n'
open('ampgo.py', 'w').write(module_code)