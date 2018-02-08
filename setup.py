from setuptools import setup

__version__ = '1.1.2'

setup(
    name = 'luaparser',
    version = __version__,
    description = 'A lua parser in Python',
    url = 'https://github.com/boolangery/py-lua-parser',
    download_url = 'https://github.com/boolangery/py-lua-parser/archive/' + __version__ + '.tar.gz',
    author = 'Eliott Dumeix',
    author_email = 'eliott.dumeix@gmail.com',
    license = 'MIT',
    packages = ['luaparser', 'luaparser.parser', 'luaparser.utils', 'luaparser.tests'],
    zip_safe = False,
    classifiers = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
    install_requires = ['antlr4-python3-runtime<=4.7', 'llist<=0.4']
)