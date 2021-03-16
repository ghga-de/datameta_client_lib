"""
    DataMeta

    DataMeta  # noqa: E501

    The version of the OpenAPI document: 0.4.0
    Contact: leon.kuchenbecker@uni-tuebingen.de
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "datameta-client-lib"
VERSION = "0.4.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "urllib3 >= 1.25.3",
  "python-dateutil",
]

setup(
    name=NAME,
    version=VERSION,
    description="DataMeta",
    author="DataMeta Dev Team",
    author_email="leon.kuchenbecker@uni-tuebingen.de",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "DataMeta"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    DataMeta  # noqa: E501
    """
)
