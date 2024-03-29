# coding=utf-8

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="two4two-laserschwelle",
    version="0.0.1",
    author="Philipp Weiss",
    author_email="philipp@itp.tu-berlin.de",
    description="Generate biased image data to train and test classifiers.",
    license='GPLv2+',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/laserschwelle/two4two",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Operating System :: POSIX :: Linux"
    ],
    python_requires='>=3.7',
)
