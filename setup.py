from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='pfm',
    version='1.2.0',
    description='pfm is a command-line tool that allows you to create files and directories in an easy and efficient way. It provides a simple interface to create files and directories with customizable names and locations.',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pfm = pfm.pfm:main',
        ],
    },
    install_requires=requirements,
)
