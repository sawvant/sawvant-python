# coding: utf-8

"""
Sawvant Cutting Optimization API — Python SDK

File generated from our OpenAPI spec; DO NOT EDIT.
"""  # noqa: E501


from pathlib import Path

from setuptools import setup, find_packages  # noqa: H301

NAME = "sawvant"
VERSION = "0.1.0"
PYTHON_REQUIRES = ">= 3.8"
REQUIRES = [
    "urllib3 >= 1.25.3, < 3.0.0",
    "python-dateutil >= 2.8.2",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]
EXTRAS_REQUIRE = {
    # sawvant.streaming uses httpx: pip install "sawvant[streaming]"
    "streaming": ["httpx >= 0.24"],
}

setup(
    name=NAME,
    version=VERSION,
    description="Python SDK for the Sawvant cutting optimization API",
    author="Sawvant",
    url="https://sawvant.com",
    project_urls={
        "Source": "https://github.com/sawvant/sawvant-python",
        "Documentation": "https://sawvant.com/docs",
    },
    license="Apache-2.0",
    keywords=["sawvant", "cutting optimization", "sdk"],
    python_requires=PYTHON_REQUIRES,
    install_requires=REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description=(Path(__file__).parent / "README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    package_data={"sawvant": ["py.typed"]},
)
