from setuptools import find_packages, setup


setup(
    name='street_cred',
    packages=find_packages(),
    install_requires=[
        'cryptography~=2.9',
        'sqlalchemy~=1.3.15',
    ]
)
