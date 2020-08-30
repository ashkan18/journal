import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="journalists",
    version="0.0.2",
    author="Ashkan Nasseri",
    author_email="ashkan18@gmail.com",
    description="App for writing fun daily journalists.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ashkan18/journal",
    packages=setuptools.find_packages(),
    package_data={
        'journalists': [
                    'commands/*',
                    'lib/*',
                    'VERSION'
                    ]
      },
    install_requires=[
        'click~=6.7',
        'prompt-toolkit~=1.0.15',
        'termcolor~=1.1',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points='''
        [console_scripts]
        journalists=journalists:cli
    ''',
    python_requires='>=3.6',
    include_package_data = True,
)