from distutils.core import setup

setup(
    name='pagseguro_python_client',
    version='0.1.0',
    packages=['', 'tests'],
    url='https://github.com/geraldoandradee/pagseguro_python_client',
    license='GNU GENERAL PUBLIC LICENSE',
    author='Geraldo Andrade',
    author_email='hi@geraldoandrade.com',
    description='Pagseguro V2 python client.',
    install_requires=[
          'requests==2.6.2', 'inflection==0.3.0'
      ],
    tests_require=['coverage']
)
