import pathlib
​
import setuptools
​
HERE = pathlib.Path(__file__).parent.resolve()
LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding="utf-8")
setuptools.setup(
    name="your_project",
    version="1.0.0",
    description="Your project that does stuff",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author="your_name",
    packages=setuptools.find_namespace_packages(include=["folder_where_your_code_is.*"]),
    package_data={"": ["*.json"]},
    python_requires=">=3.9, <4",
)