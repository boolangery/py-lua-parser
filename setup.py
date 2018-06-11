from setuptools import setup, Extension
from distutils.command.sdist import sdist
from distutils.command.build_ext import build_ext
import distutils.cmd
import luaparser


with open('README.rst') as file:
    long_description = file.read()

ext_modules = [
    Extension("luaparser.builder",
    ["luaparser/builder.pyx"],
    language='c++')]

pyx_ext_modules = [Extension("luaparser.builder",
                             sources=["luaparser/builder.pyx", "luaparser/builder.pxd"],
                             language='c++'),
                   Extension("luaparser.astnodes",
                             sources=["luaparser/astnodes.pyx"],
                             language='c++'),
                   Extension("luaparser.astutils",
                             sources=["luaparser/astutils.pyx"],
                             language='c++')]

ext_modules = [Extension('luaparser.builder',
                         sources=['luaparser/builder.cpp'],
                         libraries=[],
                         include_dirs=[],
                         define_macros=[]),
               Extension('luaparser.astnodes',
                         sources=['luaparser/astnodes.cpp'],
                         libraries=[],
                         include_dirs=[],
                         define_macros=[]),
               Extension('luaparser.astutils',
                         sources=['luaparser/astutils.cpp'],
                         libraries=[],
                         include_dirs=[],
                         define_macros=[])]


class BuildExt(build_ext):
    def run(self):
        build_ext.run(self)


class CythonizeCommand(distutils.cmd.Command):
  description = 'Cythonize cython files'
  user_options = []

  def initialize_options(self):
      pass

  def finalize_options(self):
      pass

  def run(self):
    import Cython.Build
    Cython.Build.cythonize(pyx_ext_modules, verbose=True)


class Sdist(sdist):
    def __init__(self, *args, **kwargs):
        import Cython.Build
        Cython.Build.cythonize(pyx_ext_modules, verbose=True)
        sdist.__init__(self, *args, **kwargs)


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
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
    install_requires=[
        'antlr4-python3-runtime<=4.7.1',
    ],
    entry_points={
        'console_scripts': [
            'luaparser = luaparser.__main__:main'
        ]
    },
    ext_modules=ext_modules,
    cmdclass={
        'build_ext': BuildExt,
        'sdist': Sdist,
        'cythonize': CythonizeCommand,
    }
)
