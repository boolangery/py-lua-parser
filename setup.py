from setuptools import setup

setup(name='luaparser',
      version='0.1',
      description='A lua parser in Python !',
      url='https://github.com/boolangery/py-lua-parser',
      author='Eliott Dumeix',
      author_email='',
      license='MIT',
      packages=['luaparser', 'luaparser.pprint', 'luaparser.parser'],
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
          'antlr4-python3-runtime<=4.7',
      ])