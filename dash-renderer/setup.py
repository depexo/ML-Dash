import json
from setuptools import setup

with open("package.json") as fp:
    package = json.load(fp)

setup(
    name="dash_renderer",
    version=package["version"],
    author="Said Helimi",
    author_email="helimisaid777@gmail.com",
    packages=["dash_renderer"],
    include_package_data=True,
    license="MIT",
    description="Front-end component renderer for Dash",
    install_requires=[],
)
