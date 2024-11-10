from setuptools import setup, find_packages

setup(
    name='math_quiz',
    version='0.1.0',    
    author='Md Salahuddin Parvez',
    packages=['math_quiz'],
    install_requires=['mpi4py>=2.0',
                      'numpy',                     
                      ],

    classifiers=[
        'Programming Language :: Python :: 3.5',
    ],
)