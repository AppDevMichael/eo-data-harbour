"""eo_data_harbour: ingress module."""

from setuptools import find_namespace_packages, setup

with open("README.md") as f:
    desc = f.read()

install_requires = [
    "attrs",
    "pydantic[dotenv]<2",
    "kafka-python==2.0.2",
    "msgpack==1.0.7",
]

extra_reqs = {
    "dev": [
        "pytest",
        "pytest-cov",
        "pytest-asyncio",
        "pre-commit",
        "requests",
    ],
    "docs": ["mkdocs", "mkdocs-material", "pdocs"],
}


setup(
    name="eo_data_harbour.ingress",
    description="A Kafka consumer for ingressing data for EO Data Harbour",
    long_description=desc,
    long_description_content_type="text/markdown",
    python_requires=">=3.10",
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
    ],
    keywords="Ingress Kafka",
    author="Michael O'Connell",
    # author_email="",
    url="https://github.com/AppDevMichael/EODataHarbour",
    license="MIT",
    packages=find_namespace_packages(exclude=["alembic", "tests", "scripts"]),
    zip_safe=False,
    install_requires=install_requires,
    tests_require=extra_reqs["dev"],
    extras_require=extra_reqs,
)