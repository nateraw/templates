from setuptools import setup, find_packages

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name="mypackage",
    author="Nathan Raw",
    author_email="naterawdata@gmail.com",
    description="Some package that does something.",
    # license="",
    # url="",
    install_requires=requirements,
    packages=find_packages(),
)
