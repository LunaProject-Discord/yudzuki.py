import setuptools
from yudzuki import __version__ 

readme = ""
with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()
    
requirements = ""
with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = f.read()

setuptools.setup(
    name="yudzuki.py",
    author="LunaProject Team Member",
    version=__version__,
    url="https://github.com/LunaProject-Discord/yudzuki.py",
    license="MIT",
    description="An API Wrapper for YudzukiAPI",
    packages=setuptools.find_packages(),
    long_description=readme,
    long_description_content_type="text/markdown",
    install_requires=requirements
)
