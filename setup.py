import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="journal-ashkinas", # Replace with your own username
    version="0.0.1",
    author="Ashkan Nasseri",
    author_email="ashkann@spotify.com",
    description="App for writing fun daily journal.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ashkan18/journal",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)