from setuptools import find_packages, setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='msiaLex',
    packages=find_packages(include=['msiaLex']),
    version='0.2.1',
    description='Malaysia Lexicon',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Khor Yuen Kei',
    author_email='khoryk1104@gmail.com',
    url='https://github.com/yuenkeiwac/msialex',
    license='MIT',
    install_requires=[], 
    setup_requires=['pytest-runner'], 
    tests_require=['pytest==4.4.1'],
    test_suite='tests'
)
