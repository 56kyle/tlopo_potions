import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tlopo_potions", # Replace with your own username
    version="0.0.1",
    author="Kyle Oliver",
    author_email="56kyleoliver@gmail.com",
    description="A set of scripts for brewing potions in tlopo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/56kyle/tlopo_potions",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "window_input",
        "mouse",
        "keyboard",
    ],
)
