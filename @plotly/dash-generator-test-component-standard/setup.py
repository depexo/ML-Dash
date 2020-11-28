from setuptools import setup
import json

with open('package.json') as f:
    package = json.load(f)

package_name = str(package["name"].replace(" ", "_").replace("-", "_"))

setup(
    name=package_name,
    version=package["version"],
    author=package['author'],
    author_email='helimisaid777@gmail.com',
    packages=[package_name],
    include_package_data=True,
    license=package['license'],
    description=package.get("description", package_name),
    install_requires=[]
)
