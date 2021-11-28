import setuptools

with open("readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="doctestfn",
    version="1.0.3",
    author="Jon Craton",
    author_email="jon@joncraton.com",
    description="Run doctests for a single function",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jncraton/doctestfn",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'doctestfn=doctestfn:main',
        ],
    },
    install_requires=[
    ],
)