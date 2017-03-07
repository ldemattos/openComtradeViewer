#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
#
#  openComtradeViewer.py
#  
#  Copyright 2016 Leonardo M. N. de Mattos <l@mattos.eng.br>
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

import Tkinter as tkinter
import GUI
import sys

def main():
	
	# Check input file from stdin
	if len(sys.argv) == 2:	
		comtradeFile = sys.argv[1]
	else:
		comtradeFile = None

	# Generate main window
	rootwin = tkinter.Tk()
	GUI.mainWindow(rootwin,comtradeFile)
	rootwin.mainloop()
	
	return(0)

if __name__ == '__main__':
	main()
