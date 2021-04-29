import setuptools
from yudzuki.__init__ import __version__

readme = ""
with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

try:
    setuptools.setup(
        author="Team LunaProject",
        version=__version__,
        url="https://github.com/LunaProject-Discord/yudzuki.py",
        description="An API Wrapper for YudzukiAPI",
        long_description=readme,
        long_description_content_type="text/markdown"
    )
except Exception as e:
    print(e)
