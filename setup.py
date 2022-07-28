from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "Image_attribute_classification"
AUTHOR_USER_NAME = "sanjeev49"
SRC_REPO = "src"
#LIST_OF_REQUIREMENTS = ["dvc", "tensorflow", "matplotlib", "pandas", "sklearn"]


setup(
    name=SRC_REPO,
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    description="A small package for DVC",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    author_email="sanjeevkr4983@gmail.com",
    packages=[SRC_REPO],
    license="MIT",
    python_requires=">=3.7",
    #install_requires=LIST_OF_REQUIREMENTS
)
