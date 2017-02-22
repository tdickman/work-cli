import os
from setuptools import setup, find_packages


current_dir = os.path.abspath(os.path.dirname(__file__))

install_requires = []
console_scripts = []
with open(os.path.join(current_dir, 'requirements.txt')) as f:
    install_requires += f.read().splitlines()
    console_scripts.append('w = work:cli')

print(console_scripts)

setup(
    name="work",
    version='0.1.0',
    description="Cli for jira and a number of other tools",
    author="Tom Dickman",
    author_email="tdickman@rmn.com",
    url="",
    packages=find_packages(),
    setup_requires=['nose'],
    entry_points={
        'console_scripts': console_scripts
    },
    install_requires=install_requires,
)
