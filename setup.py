from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="scantot",
    version="3.1.0",
    author="ScanTot Contributors",
    description="Fast modular web security scanner",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/scantot/scantot",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.28.0",
        "dnspython>=2.3.0",
    ],
    entry_points={
        "console_scripts": [
            "scantot=scantot.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Security",
    ],
)