from setuptools import setup
import luaparser


with open('README.rst') as file:
    long_description = file.read()

setup(
    name='luaparser',
    version=luaparser.__version__,
    description='A lua parser in Python',
    long_description=long_description,
    url='https://github.com/boolangery/py-lua-parser',
    download_url='https://github.com/boolangery/py-lua-parser/archive/' + luaparser.__version__ + '.tar.gz',
    author='Eliott Dumeix',
    author_email='eliott.dumeix@gmail.com',
    license='MIT',
    packages=['luaparser', 'luaparser.parser', 'luaparser.utils', 'luaparser.tests'],
    zip_safe=False,
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    install_requires=[
        'antlr4-python3-runtime<=4.7.2',
    ],
    entry_points={
        'console_scripts': [
            'luaparser = luaparser.__main__:main'
        ]
    }
)
