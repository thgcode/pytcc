from setuptools import setup
from pytcc.version import VERSION
setup(
    name="pytcc",
    version=VERSION,
url="https://github.com/thgcode/pytcc",
description="Python wrapper for the Tiny C Compiler",
    author="Thiago Seus",
    author_email="thiago.seus@yahoo.com.br",
    packages = ["pytcc"])
