#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  setup.py
#  
#  Copyright 2017 Leonardo M. N. de Mattos <l@mattos.eng.br>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; version 3 of the License.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  

from setuptools import setup

setup(name='openComtradeViewer',
	version='0.0',
	description='IEEE COMTRADE oscillograph visualizer',
	long_description='An open/free multi platform IEEE COMTRADE oscillograph records visualizer',
	classifiers=[
		'Development Status :: 3 - Alpha',
		'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
		'Programming Language :: Python :: 2.7',
		'Topic :: Multimedia :: Graphics :: Viewers',
	],
	license='GPLv3',
	author='Leonardo M. N. de Mattos',
	author_email='l@mattos.eng.br',
	url='https://github.com/ldemattos/openComtradeViewer',
	packages=['openComtradeViewer'],
	package_dir={'openComtradeViewer':'src'},
	data_files=[("", ["LICENSE"]),
				("", ["README.md"])
				],
    entry_points = {
				'console_scripts': [
					'ocv = openComtradeViewer.run:main',
				],              
	},
	include_package_data=True,
	zip_safe=False
)
