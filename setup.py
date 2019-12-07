import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyutils",
    version="0.1",
    author="Marc Horlacher",
    author_email="marc.horlacher@gmail.com",
    description="Utilities for the Python language",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mhorlacher/pyutils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

