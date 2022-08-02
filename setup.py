from setuptools import find_packages, setup

setup(
    name="datascience_test",
    version="0.0",
    url="https://github.com/Exii-ai/datascience-test",
    license="MIT",
    author="Khalim Conn-Kowlessar",
    author_email="khalim@exii.co",
    description="Exii datascience test repo",
    long_description="",
    packages=find_packages(exclude=("tests",)),
    install_requires=[],  # This should be any 3rd party packages so needs to be updated
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        "": ["VERSION"],
    },
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    setup_requires=["pytest-runner",],
    tests_require=["pytest", "pytest-cov"],
)