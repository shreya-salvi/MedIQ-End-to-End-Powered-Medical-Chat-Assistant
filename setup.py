from setuptools import setup, find_packages

setup(
    name="generative_ai_project",
    version="0.0.0",
    author="SHreya Salvi",
    author_email="shreyasalvi2120@gmail.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
)
