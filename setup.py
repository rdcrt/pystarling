import io
import re
from setuptools import setup, find_packages

import os


# Get package version number
# Source: https://packaging.python.org/single_source_version/
def read(*names, **kwargs):
    with io.open(
            os.path.join(os.path.dirname(__file__), *names),
            encoding=kwargs.get('encoding', 'utf8')
    ) as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]",
        version_file, re.M
    )
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name='pystarling',
    version=find_version('pystarling', '__init__.py'),
    license='MIT License',
    packages=find_packages(),
    install_requires=[
        'python-dateutil>=2.6.1',
        'requests>=2.18.4',
        'six>=1.10.0'
    ]
)
