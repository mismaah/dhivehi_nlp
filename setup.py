import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dhivehi_nlp",
    version="1.0.8",
    author="Mismaah Abdulla",
    author_email="mismaahabdulla@gmail.com",
    description="Natural language processing tools for the Dhivehi language.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mismaah/dhivehi-nlp",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    include_package_data=True,
)
