try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='bbob',
    version='0.1',
    description='Unified interfaces and benchmarks for a range of black box optimization software.',
    license='MIT',
    author='The bbob contributors',
    packages=['bbob'],
    install_requires=[
        "numpy", "scipy", "matplotlib", "bootstrapped", "scikit-learn",
        "scikit-optimize", "joblib",
    ],
    dependency_links=[
        "https://github.com/scikit-optimize/scikit-optimize/archive/master.zip",
        "https://github.com/sigopt/evalset/archive/master.zip"
    ]
)
