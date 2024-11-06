from setuptools import setup, find_packages

setup(
    name='math_quiz',
    version='0.1.0',    
    description='A example Python package',
    url='https://github.com/shuds13/math_quiz',
    author='Md Salahuddin Parvez',
    license='BSD 2-clause',
    packages=['math_quiz'],
    entry_points={
        "console_scripts": [
            "math_quiz=math_quiz.math_quiz:math_quiz"
        ]
    },
    install_requires=['mpi4py>=2.0',
                      'numpy',                     
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)