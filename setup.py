from setuptools import setup

setup(
    name='RatesPackage',
    version='0.2',
    description='get dollars rates from currency freaks',
    url='https://github.com/arshi8294/RatesPackage',
    author='Arshia',
    author_email='arshi829495@gmail.com',
    license='MIT',
    packages=['currency_freaks'],
    install_requires=['requests'],
    zip_safe=False
)
