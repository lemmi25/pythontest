import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python_test",
    version="0.0.1",
    author="Moritz Boesenberg",
    author_email="moritz.boesenberg@outlook.com",
    description="python_test",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lemmi25/python_test",
    project_urls={
        "Bug Tracker": "https://github.com/lemmi25/python-test/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
)