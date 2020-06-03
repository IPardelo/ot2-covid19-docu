# -*- coding: utf-8 -*-

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ot2-covid-pkg-sergas",
    version="1.0.0",
    author="Luis Lorenzo Mosquera, Victor Soroña Pombo, Ismael Castiñeira Paz",
    author_email="luislm@improvingmetrics.com, victorsp@improvingmetrics.com, ismael.castineira@ciberexperis.es",
    description="Several scripts for Opentrons covid19 PCR preparation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/luislorenzom/ot2-covid19",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL-3.0",
        "Operating System :: Debian",
    ],
    python_requires='>=3.7',
)
