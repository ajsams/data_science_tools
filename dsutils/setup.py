from setuptools import find_packages, setup

setup(
    name="dsutils",
    packages=find_packages(include=["dsutils"]),
    version="0.1.0",
    description="Personal data science utilities library.",
    author="Aaron J. Sams",
    install_requires=[],
    setup_requires=["pytest-runner"],
    tests_require=["pytest==7.4.3"],
    test_suite="tests",
)
