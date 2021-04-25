import setuptools
from yudzuki import __version__

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

setuptools.setup(
    name="yudzuki",
    version=__version__,
    author="Midorichan",
    description="An API Wrapper for YudzukiAPI"
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/LunaProject-Discord/yudzuki.py",
    packages=setuptools.find_packages()
)