from evalset.icml2016_tests import tests_for_nonparametric
from evalset import test_funcs
from skopt.space import Real, Integer
import numpy as np
import math

class Ackley_11_r(test_funcs.Ackley):
    def __init__(self):
        super(Ackley_11_r, self).__init__(dim=11)

        integer_idx = []
        self.res = None

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
    

class Ackley_3_1_r(test_funcs.Ackley):
    def __init__(self):
        super(Ackley_3_1_r, self).__init__(dim=3)

        integer_idx = []
        self.res = 1

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
    

class Adjiman_2_r(test_funcs.Adjiman):
    def __init__(self):
        super(Adjiman_2_r, self).__init__(dim=2)

        integer_idx = []
        self.res = None

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
    

class Alpine02_2_ri(test_funcs.Alpine02):
    def __init__(self):
        super(Alpine02_2_ri, self).__init__(dim=2)

        integer_idx = [0]
        self.res = None

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
    

class CarromTable_2_ri(test_funcs.CarromTable):
    def __init__(self):
        super(CarromTable_2_ri, self).__init__(dim=2)

        integer_idx = [0]
        self.res = None

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
    

class Csendes_2_r(test_funcs.Csendes):
    def __init__(self):
        super(Csendes_2_r, self).__init__(dim=2)

        integer_idx = []
        self.res = None

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
    

class DeflectedCorrugatedSpring_4_r(test_funcs.DeflectedCorrugatedSpring):
    def __init__(self):
        super(DeflectedCorrugatedSpring_4_r, self).__init__(dim=4)

        integer_idx = []
        self.res = None

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
    

class DeflectedCorrugatedSpring_7_r(test_funcs.DeflectedCorrugatedSpring):
    def __init__(self):
        super(DeflectedCorrugatedSpring_7_r, self).__init__(dim=7)

        integer_idx = []
        self.res = None

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
    

class Easom_2_r(test_funcs.Easom):
    def __init__(self):
        super(Easom_2_r, self).__init__(dim=2)

        integer_idx = []
        self.res = None

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
    

class Easom_4_r(test_funcs.Easom):
    def __init__(self):
        super(Easom_4_r, self).__init__(dim=4)

        integer_idx = []
        self.res = None

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
    

class Easom_5_r(test_funcs.Easom):
    def __init__(self):
        super(Easom_5_r, self).__init__(dim=5)

        integer_idx = []
        self.res = None

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
    

class Hartmann3_3_ri(test_funcs.Hartmann3):
    def __init__(self):
        super(Hartmann3_3_ri, self).__init__(dim=3)

        integer_idx = [0]
        self.res = None

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
    

class Hartmann6_6_10_r(test_funcs.Hartmann6):
    def __init__(self):
        super(Hartmann6_6_10_r, self).__init__(dim=6)

        integer_idx = []
        self.res = 10

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
    

class HelicalValley_3_r(test_funcs.HelicalValley):
    def __init__(self):
        super(HelicalValley_3_r, self).__init__(dim=3)

        integer_idx = []
        self.res = None

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
    

class LennardJones6_6_r(test_funcs.LennardJones6):
    def __init__(self):
        super(LennardJones6_6_r, self).__init__(dim=6)

        integer_idx = []
        self.res = None

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
    

class McCourt01_7_10_r(test_funcs.McCourt01):
    def __init__(self):
        super(McCourt01_7_10_r, self).__init__(dim=7)

        integer_idx = []
        self.res = 10

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
    

class McCourt03_9_r(test_funcs.McCourt03):
    def __init__(self):
        super(McCourt03_9_r, self).__init__(dim=9)

        integer_idx = []
        self.res = None

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
    

class McCourt06_5_r(test_funcs.McCourt06):
    def __init__(self):
        super(McCourt06_5_r, self).__init__(dim=5)

        integer_idx = []
        self.res = None

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
    

class McCourt07_6_12_r(test_funcs.McCourt07):
    def __init__(self):
        super(McCourt07_6_12_r, self).__init__(dim=6)

        integer_idx = []
        self.res = 12

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
    

class McCourt08_4_r(test_funcs.McCourt08):
    def __init__(self):
        super(McCourt08_4_r, self).__init__(dim=4)

        integer_idx = []
        self.res = None

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
    

class McCourt09_3_r(test_funcs.McCourt09):
    def __init__(self):
        super(McCourt09_3_r, self).__init__(dim=3)

        integer_idx = []
        self.res = None

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
    

class McCourt10_8_r(test_funcs.McCourt10):
    def __init__(self):
        super(McCourt10_8_r, self).__init__(dim=8)

        integer_idx = []
        self.res = None

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
    

class McCourt11_8_r(test_funcs.McCourt11):
    def __init__(self):
        super(McCourt11_8_r, self).__init__(dim=8)

        integer_idx = []
        self.res = None

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
    

class McCourt12_7_r(test_funcs.McCourt12):
    def __init__(self):
        super(McCourt12_7_r, self).__init__(dim=7)

        integer_idx = []
        self.res = None

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
    

class McCourt13_3_r(test_funcs.McCourt13):
    def __init__(self):
        super(McCourt13_3_r, self).__init__(dim=3)

        integer_idx = []
        self.res = None

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
    

class McCourt14_3_r(test_funcs.McCourt14):
    def __init__(self):
        super(McCourt14_3_r, self).__init__(dim=3)

        integer_idx = []
        self.res = None

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
    

class McCourt16_4_r(test_funcs.McCourt16):
    def __init__(self):
        super(McCourt16_4_r, self).__init__(dim=4)

        integer_idx = []
        self.res = None

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
    

class McCourt16_4_10_r(test_funcs.McCourt16):
    def __init__(self):
        super(McCourt16_4_10_r, self).__init__(dim=4)

        integer_idx = []
        self.res = 10

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
    

class McCourt17_7_r(test_funcs.McCourt17):
    def __init__(self):
        super(McCourt17_7_r, self).__init__(dim=7)

        integer_idx = []
        self.res = None

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
    

class McCourt18_8_r(test_funcs.McCourt18):
    def __init__(self):
        super(McCourt18_8_r, self).__init__(dim=8)

        integer_idx = []
        self.res = None

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
    

class McCourt19_2_r(test_funcs.McCourt19):
    def __init__(self):
        super(McCourt19_2_r, self).__init__(dim=2)

        integer_idx = []
        self.res = None

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
    

class McCourt20_2_r(test_funcs.McCourt20):
    def __init__(self):
        super(McCourt20_2_r, self).__init__(dim=2)

        integer_idx = []
        self.res = None

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
    

class McCourt23_6_r(test_funcs.McCourt23):
    def __init__(self):
        super(McCourt23_6_r, self).__init__(dim=6)

        integer_idx = []
        self.res = None

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
    

class McCourt26_3_r(test_funcs.McCourt26):
    def __init__(self):
        super(McCourt26_3_r, self).__init__(dim=3)

        integer_idx = []
        self.res = None

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
    

class McCourt28_4_r(test_funcs.McCourt28):
    def __init__(self):
        super(McCourt28_4_r, self).__init__(dim=4)

        integer_idx = []
        self.res = None

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
    

class Michalewicz_4_r(test_funcs.Michalewicz):
    def __init__(self):
        super(Michalewicz_4_r, self).__init__(dim=4)

        integer_idx = []
        self.res = None

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
    

class Michalewicz_4_20_r(test_funcs.Michalewicz):
    def __init__(self):
        super(Michalewicz_4_20_r, self).__init__(dim=4)

        integer_idx = []
        self.res = 20

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
    

class Michalewicz_8_r(test_funcs.Michalewicz):
    def __init__(self):
        super(Michalewicz_8_r, self).__init__(dim=8)

        integer_idx = []
        self.res = None

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
    

class Mishra06_2_r(test_funcs.Mishra06):
    def __init__(self):
        super(Mishra06_2_r, self).__init__(dim=2)

        integer_idx = []
        self.res = None

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
    

class Ned01_2_r(test_funcs.Ned01):
    def __init__(self):
        super(Ned01_2_r, self).__init__(dim=2)

        integer_idx = []
        self.res = None

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
    

class OddSquare_2_r(test_funcs.OddSquare):
    def __init__(self):
        super(OddSquare_2_r, self).__init__(dim=2)

        integer_idx = []
        self.res = None

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
    

class Parsopoulos_2_ri(test_funcs.Parsopoulos):
    def __init__(self):
        super(Parsopoulos_2_ri, self).__init__(dim=2)

        integer_idx = [0]
        self.res = None

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
    

class Pinter_2_ri(test_funcs.Pinter):
    def __init__(self):
        super(Pinter_2_ri, self).__init__(dim=2)

        integer_idx = [0, 1]
        self.res = None

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
    

class Plateau_2_r(test_funcs.Plateau):
    def __init__(self):
        super(Plateau_2_r, self).__init__(dim=2)

        integer_idx = []
        self.res = None

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
    

class Problem03_1_r(test_funcs.Problem03):
    def __init__(self):
        super(Problem03_1_r, self).__init__(dim=1)

        integer_idx = []
        self.res = None

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
    

class RosenbrockLog_11_r(test_funcs.RosenbrockLog):
    def __init__(self):
        super(RosenbrockLog_11_r, self).__init__(dim=11)

        integer_idx = []
        self.res = None

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
    

class Sargan_5_r(test_funcs.Sargan):
    def __init__(self):
        super(Sargan_5_r, self).__init__(dim=5)

        integer_idx = []
        self.res = None

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
    

class Sargan_2_ri(test_funcs.Sargan):
    def __init__(self):
        super(Sargan_2_ri, self).__init__(dim=2)

        integer_idx = [0]
        self.res = None

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
    

class Schwefel20_2_r(test_funcs.Schwefel20):
    def __init__(self):
        super(Schwefel20_2_r, self).__init__(dim=2)

        integer_idx = []
        self.res = None

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
    

class Schwefel20_2_ri(test_funcs.Schwefel20):
    def __init__(self):
        super(Schwefel20_2_ri, self).__init__(dim=2)

        integer_idx = [0]
        self.res = None

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
    

class Schwefel36_2_r(test_funcs.Schwefel36):
    def __init__(self):
        super(Schwefel36_2_r, self).__init__(dim=2)

        integer_idx = []
        self.res = None

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
    

class Shekel05_4_r(test_funcs.Shekel05):
    def __init__(self):
        super(Shekel05_4_r, self).__init__(dim=4)

        integer_idx = []
        self.res = None

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
    

class Sphere_7_ri(test_funcs.Sphere):
    def __init__(self):
        super(Sphere_7_ri, self).__init__(dim=7)

        integer_idx = [0, 1, 2, 3, 4]
        self.res = None

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
    

class StyblinskiTang_5_r(test_funcs.StyblinskiTang):
    def __init__(self):
        super(StyblinskiTang_5_r, self).__init__(dim=5)

        integer_idx = []
        self.res = None

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
    

class Tripod_2_r(test_funcs.Tripod):
    def __init__(self):
        super(Tripod_2_r, self).__init__(dim=2)

        integer_idx = []
        self.res = None

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
    

class Xor_9_r(test_funcs.Xor):
    def __init__(self):
        super(Xor_9_r, self).__init__(dim=9)

        integer_idx = []
        self.res = None

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
    
problems = [Ackley_11_r, Ackley_3_1_r, Adjiman_2_r, Alpine02_2_ri, CarromTable_2_ri, Csendes_2_r, DeflectedCorrugatedSpring_4_r, DeflectedCorrugatedSpring_7_r, Easom_2_r, Easom_4_r, Easom_5_r, Hartmann3_3_ri, Hartmann6_6_10_r, HelicalValley_3_r, LennardJones6_6_r, McCourt01_7_10_r, McCourt03_9_r, McCourt06_5_r, McCourt07_6_12_r, McCourt08_4_r, McCourt09_3_r, McCourt10_8_r, McCourt11_8_r, McCourt12_7_r, McCourt13_3_r, McCourt14_3_r, McCourt16_4_r, McCourt16_4_10_r, McCourt17_7_r, McCourt18_8_r, McCourt19_2_r, McCourt20_2_r, McCourt23_6_r, McCourt26_3_r, McCourt28_4_r, Michalewicz_4_r, Michalewicz_4_20_r, Michalewicz_8_r, Mishra06_2_r, Ned01_2_r, OddSquare_2_r, Parsopoulos_2_ri, Pinter_2_ri, Plateau_2_r, Problem03_1_r, RosenbrockLog_11_r, Sargan_5_r, Sargan_2_ri, Schwefel20_2_r, Schwefel20_2_ri, Schwefel36_2_r, Shekel05_4_r, Sphere_7_ri, StyblinskiTang_5_r, Tripod_2_r, Xor_9_r]
