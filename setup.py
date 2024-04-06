from setuptools import setup

setup(
    name='objexp',
    version='0.0.1',
    # install_requires=[
    #     'python_version>"3.10"',
    # ],
    description='A plugin to say sorry in several ways',
    url='http://wuxv.art',
    author='lukelin',
    author_email='luke.l.lin@hotmail.com',
    license='SimPL-2.0',
    packages=['objexp'],
    zip_safe=False
)

# `pip install -e . `
# `-e` means sync modify from source to installed package.

# `python setup.py register`

# https://setuptools.pypa.io/en/latest/userguide/quickstart.html

