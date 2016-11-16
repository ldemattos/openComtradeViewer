#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
#
#  openComtradeViewer.py
#  
#  Copyright 2016 Leonardo M. N. de Mattos <l@mattos.eng.br>
#                 Aniela M. P. Mendes <anielampm@protonmail.ch>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
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

# my libraries

import src.fileHandling
import src.mainGUI



def main():
	
	# Variables
	lisFile = "none.txt"
	
	# Generate main window
	rootwin = tkinter.Tk()
	src.mainGUI.mainWindow(rootwin)
	rootwin.mainloop()
	
	# Build main Window
	#~ src.mainGUI.buildGUI()
	
	return 0

if __name__ == '__main__':
	main()
