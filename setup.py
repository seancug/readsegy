# -*- coding: utf-8 -*-

# A simple setup script to create an executable using PyQt4. This also
# demonstrates the method for creating a Windows executable that does not have
# an associated console.
#
# PyQt4app.py is a very simple type of PyQt4 application
#
# Run the build process by running the command 'python setup.py build'
#
# If everything works well you should find a subdirectory in the build
# subdirectory that contains the files needed to run the application

import sys
from cx_Freeze import setup, Executable


base = 'Console'
	
options = {
    'build_exe': {
        'includes': ['atexit'],
		'optimize': 2,
		'excludes':['tk','tcl'],
		'compressed':True
    }
}

executables = [
    Executable('readcoord.py', base=base,targetName="readcoord.exe",
compress=True,icon='beauty.ico')
]

setup(name='readcoord',
      version='1.0',
      description='read SEGY data',
      options=options,
      executables=executables
      )
