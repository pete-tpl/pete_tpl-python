import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pete_tpl",
    version="0.1.9",
    author="Sergei Belyakov",
    author_email="1899416+tasmanianfox@users.noreply.github.com",
    description="A template engine inspired by TWIG",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pete-tpl",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.6',
    scripts=['scripts/petetpl_postinstall.py'],
)