from setuptools import setup, find_packages

setup(
    name="math_quiz",
    version="1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "math_quiz=math_quiz.math_quiz:math_quiz"
        ]
    },
    author="Md Salahuddin Parvez",
    url="https://github.com/parvezshams38/DSSS_HW_2",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)