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
    install_requires= open('requirements.txt').read().split("\n"),
    tests_require=['coverage'],
    zip_safe=False,
    classifiers=[
    'Development Status :: 3 - Alpha',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'Natural Language :: English',
    'License :: OSI Approved :: BSD License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    ],
    keywords='pagseguro, payment, payments, payment-gateway, credit-card'
)
