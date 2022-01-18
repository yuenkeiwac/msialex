from setuptools import find_packages, setup
setup(
    name='msiaLex',
    packages=find_packages(include=['msiaLex']),
    version='0.1.0',
    description='Malaysia Lexicon',
    author='Khor Yuen Kei',
    author_email='khoryk1104@gmail.com',
    url='https://github.com/yuenkeiwac/msialex',
    license='MIT',
    install_requires=[], 
    setup_requires=['pytest-runner'], 
    tests_require=['pytest==4.4.1'],
    test_suite='tests'
)
