import music_rename
from setuptools import setup

setup(name='music_rename',
      version=music_rename.__version__,
      description='Rename music files after ripping with EAC.',
      url='https://github.com/mfinelli/music-rename',
      author='Mario Finelli',
      license='GPL',
      install_requires=[
          'colorama', 'termcolor'
      ],
      packages=['music_rename'],
      entry_points={
          'console_scripts': [
              'music-rename=music_rename.console:main'
          ]
      })
