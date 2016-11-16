#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  GUI_About.py
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

def aboutWin():
	
	import Tkinter as tkinter
	
	# create about window
	about = tkinter.Toplevel()
	about.rowconfigure(0,weight=1)
	about.columnconfigure(0,weight=1)
	
	# about window title
	about.title("openComtradeViewer - About")
	
	# set about window dimensions and position
	w = 400
	h = 190
	about.resizable(width='false', height='false')
	width = about.winfo_screenwidth()
	height = about.winfo_screenheight()
	posx = (width - w)/2.0
	posy = (height - h)/2.0
	about.geometry('%dx%d+%d+%d' % (w, h, posx, posy))
	
	# Window text
	tkinter.Label(about,text="openComtradeViewer", font=12).grid(row=0,column=0)
	tkinter.Label(about,text="Copyright 2016").grid(row=1,column=0)
	tkinter.Label(about,text="Leonardo M. N. de Mattos <l@mattos.eng.br>").grid(row=2,column=0)
	tkinter.Label(about,text="Project page: http://github.com/ldemattos/openComtradeViewer").grid(row=3,column=0)
	tkinter.Label(about,text="License: GNU GPL v3").grid(row=4,column=0)
	tkinter.Label(about,text="pyComtrade", font=12).grid(row=5,column=0)
	tkinter.Label(about,text="Copyright 2013").grid(row=6,column=0)
	tkinter.Label(about,text="Miguel Moreto <miguel.moreto@ufsc.br>").grid(row=7,column=0)
	tkinter.Label(about,text="Project page: http://github.com/miguelmoreto/pycomtrade").grid(row=8,column=0)
	tkinter.Label(about,text="License: GNU GPL v3").grid(row=9,column=0)
