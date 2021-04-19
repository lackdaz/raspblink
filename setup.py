from setuptools import setup, find_packages

import os
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(dir_path, "VERSION")) as version_file:
    version = version_file.read().strip()

setup(
    version=version, name="raspblink", packages=["raspblink"], package_dir={"": "src"}
)
