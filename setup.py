from setuptools import find_packages, setup

with open("README.md") as f:
    long_description = f.read()

setup(
    name="substring_matcher",
    version="0.1.0",
    description="Looks for keyword matches inside of URLs using a list of keywords (substrings).",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="AGPL-3.0",
    author="Mohammad Adeel",
    author_email="Adeel.A.Mhd@gmail.com",
    packages=["substring_matcher"],
    install_requires=find_packages(exclude=['docs', 'tests*']),
    package_data={
        "substring_matcher": ["data/keywords.txt"],
        "substring_matcher": ["data/runtime_test_keywords"],
        "substring_matcher": ["data/test_keywords"],
        "substring_matcher": ["data/urls"],
    },
    import_package_data=True,
    python_requires=">=3.9",
    classifiers=[
        "Natural Language :: English",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: AGPL-3.0 License",
        "Programming Language :: Python :: 3.9",
    ]
    entry_points={"console_scripts": [
        "substring_matcher_cli=substring_matcher.substrin_matcher_cli:main"]},
)
