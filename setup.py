import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

__version__ = "0.0.0"
REPO_NAME = "Text-Summarizer"
USER_NAME = "9085prayas"
SRC_REPO = 'text_summarizer'
EMAIL = "prayas9085@gmail.com"


setuptools.setup(

    name = REPO_NAME,

    version = __version__,
    author = USER_NAME,
    author_email = EMAIL,
    description = 'Python package for text summarization',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = f"https://github.com/{USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
)