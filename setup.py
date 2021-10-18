import os
import pathlib

from setuptools import setup, find_packages

readme_path = pathlib.Path("README.md")

setup(
    name='notebook-video-writer',
    packages = find_packages(),
    version='0.0.3',
    description="Create videos from numpy arrays in a jupyter notebook",
    long_description=readme_path.read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/PWhiddy/notebook-video-writer",
    author="None",
    author_email="all.cows.like.to.moo@gmail.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    keywords=['video', 'notebook', 'jupyter', 'numpy', 'interactive'],
    install_requires=['numpy', 'moviepy'],
    python_requires=">=3.5",
)
