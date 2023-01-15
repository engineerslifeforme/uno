from distutils.core import setup
setup(
    name='auto-uno',
    version='1.0',
    py_modules=['auto_uno'],
    url='https://github.com/engineerslifeforme/uno',
    author='Creative Rigor, LLC',
    author_email='creativerigor@gmail.com',
    license='MIT',
    description="Uno CLI for strategy testing",
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'uno = auto_uno.run:main',
        ]
    }
)