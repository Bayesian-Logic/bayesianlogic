# Copyright (c) 2020 Bayesian Logic, Inc.
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bayesianlogic",
    version="0.0.1a1",
    author="Nimar Arora",
    author_email="nimar.arora@gmail.com",
    description="A package for Bayesian Inference",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Bayesian-Logic/bayesianlogic",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires='>=3.6',
)
