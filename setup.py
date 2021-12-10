from setuptools import setup, find_packages
from glob import glob
from os.path import basename
from os.path import splitext

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="selenpack",
    version_config=True,
    setup_requires=["setuptools-git-versioning"],
    author="tomoki",
    url="https://github.com/tomoki171923/selenium-operation-package",
    description="this package helps operate Selenium. Support browser is Google Chrome.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "selenium>=4.1.0",
        "pillow==8.4.0",
    ],
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob("src/*.py")],
)
