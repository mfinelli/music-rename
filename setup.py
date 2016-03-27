from setuptools import setup

setup(
    name='music_rename',
    version='1.0.0',
    description='Rename music files after ripping with EAC.',
    url='https://github.com/mfinelli/music-rename',
    author='Mario Finelli',
    license='GPL',
    install_requires=[],
    packages=['music_rename'],
    entry_points={
        'console_scripts': [
            'music-rename=music_rename.console:main'
        ]
    }
)
