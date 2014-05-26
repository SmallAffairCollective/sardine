from setuptools import setup, find_packages

setup(
    name='sardine',
    version='0.0.1',
    packages=find_packages(),
    license='LICENSE',
    description='S.O.S. Game - it is delicious.',
    long_description=open('README.md').read(),
    author=u'Alex Noguchi',
    author_email='anoguchi@puc.edu',
    package_data={'': ['README.md', 'requirements.txt'], 'bowl': []},
    install_requires=[],
    entry_points={
        'console_scripts': [
            'sardine = sardine.ui:start',
        ]
    }
)
