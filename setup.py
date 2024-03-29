import os
from runpy import run_path

from setuptools import find_packages, setup

# read the program version from version.py (without loading the module)
# __version__ = run_path('src/muller_idle/version.py')['__version__']
from src.muller_idle import __version__


def read(fname):
    """Utility function to read the README file."""
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="muller-idle",
    author="Alejandro Gil",
    version=__version__,
    author_email="alejandrogilelias940711@gmail.com",
    description="Muller Idle takes the core of what makes an adventure game so addictive and strips it down to its purest form!",
    license="proprietary",
    url="",
    packages=find_packages("src"),
    package_dir={"": "src"},
    package_data={"muller_idle": ["res/*"]},
    long_description=read("README.md"),
    install_requires=[
        "setuptools",
    ],
    tests_require=[
        "pytest",
        "pytest-cov",
        "pre-commit",
    ],
    platforms="any",
    python_requires=">=3.8",
)
