import setuptools
from yudzuki import __version__

readme = ""
with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

setuptools.setup(
    author="Team LunaProject",
    version=__version__,
    url="https://github.com/LunaProject-Discord/yudzuki.py",
    description="An API Wrapper for YudzukiAPI",
    long_description=readme,
    long_description_content_type="text/markdown"
)
