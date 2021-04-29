import setuptools

readme = ""
with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

__version__ = "1.0.0"

setuptools.setup(
    name="yudzuki.py",
    author="LunaProject Team Member",
    version=__version__,
    url="https://github.com/LunaProject-Discord/yudzuki.py",
    description="An API Wrapper for YudzukiAPI",
    long_description=readme,
    long_description_content_type="text/markdown"
)
