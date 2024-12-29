from setuptools import setup, find_packages
setup(
    name='my-first-python-package',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pytest==6.2.4',
    ],
)
