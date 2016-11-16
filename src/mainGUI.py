#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  GUI.py
#  
#  Copyright 2016 Leonardo M. N. de Mattos <leonardo@mattos.eng.br>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
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
#  

import Tkinter as tkinter
import os

class Window:
	
	def __init__ (self,toplevel):
		
		toplevel.rowconfigure(0,weight=1)
		toplevel.rowconfigure(1,weight=1)
		toplevel.columnconfigure(0,weight=1)
		toplevel.columnconfigure(1,weight=1)
		
		# Window title
		toplevel.title("openComtradeViewer")
		
		# Window dimensions and position
		w = 434
		h = 434
		toplevel.resizable(width='false', height='false')
		width = toplevel.winfo_screenwidth()
		height = toplevel.winfo_screenheight()
		posx = (width - w)/2.0
		posy = (height - h)/2.0
		toplevel.geometry('%dx%d+%d+%d' % (w, h, posx, posy))
		
		# Set window icon
		if os.name == "nt":
			toplevel.wm_iconbitmap(default='.\icons\Statistics.ico')
		else:
			#~ Here will be placed the options for Linux/Mac OS X
			pass
		
		# select file to be parsed (label)
		lbl_select = tkinter.Label(self, text="Select lis-file:")
	
		# Button to call file dialog selection
		# file selection
		def fileSelection():		
			lisFile = tkFileDialog.askopenfilename(title="Select lis-file:")
			
			if len(lisFile) != 0:		
			
				# Update parse button command
				btn_runParser.configure(command=lambda: runParser(lisFile))
				
				# Update lbl_LisFile
				lbl_lisFile.configure(text=os.path.basename(lisFile))		
				
			else: 
				
				# Update lis-file
				lisFile = "none.txt"
				
				# Update parse button command
				btn_runParser.configure(command=lambda: runParser(lisFile))
				
				# Update lbl_LisFile
				lbl_lisFile.configure(text="No file selected")
				
			
		btn_fileSelection = tkinter.Button(toplevel, text="Open", command=fileSelection)
		
		# Label to show the selected file name
		lbl_lisFile = tkinter.Label(toplevel, text="No file selected")
		
		# Button to run parser
		def runParser(lisFile):	
			
			if lisFile != "none.txt" and len(lisFile) != 0:
			
				[runStatus,outputFiles] = lis_stat_parser(["parseATPStats.py",lisFile],1)
				
				if runStatus == 0:
					
					infoText = "Everything seems to went OK! :)\n\nThe output files are saved on directory %s"\
					%(os.path.dirname(lisFile))
	
					tkMessageBox.showinfo("Parsing finished", infoText)
					
				elif runStatus == 1:
					tkMessageBox.showerror("Parsing finished", "Ooops!\nUnable to open the given lis-file :/")
				elif runStatus == 2:
					tkMessageBox.showerror("Parsing finished", "Ooops!\nThis is not a proper lis-file :/")
				else:
					tkMessageBox.showerror("Parsing finished", "Ooops!\nSomething unexpected happened :/")
					
			else:
				properMsg = "Select a proper lis-file clicking in Open button..."
				print properMsg
				tkMessageBox.showwarning("parseATPStats", "No file selected!\n"+properMsg)
			
		btn_runParser = tkinter.Button(toplevel, text="Parse it!",command=lambda: runParser(lisFile))
		
		# Create menu bar
		menubar = tkinter.Menu(toplevel)
		
		filemenu = tkinter.Menu(menubar, tearoff=0)
		filemenu.add_command(label="Select lis-file...", command=fileSelection)
		#~ filemenu.add_command(label="Run parser...", command=lambda: runParser(lisFile))
		filemenu.add_command(label="Exit", command=toplevel.quit)
		menubar.add_cascade(label="File", menu=filemenu)
		
		helpmenu = tkinter.Menu(menubar, tearoff=0)
		helpmenu.add_command(label="Project page", command=lambda: webbrowser.open(url,new=2))
		helpmenu.add_command(label="About", command=lambda: aboutWin())
		menubar.add_cascade(label="Help", menu=helpmenu)
			
		toplevel.config(menu=menubar)
		
		# Add the widgets to the window screen
		lbl_select.grid(sticky='w',row=0,column=0)
		btn_fileSelection.grid(sticky='w',row=1,column=0)
		lbl_lisFile.grid(sticky='w',row=1,column=1)
		btn_runParser.grid(sticky='nsew',row=2,column=0,columnspan=2)
		
def buildGUI():
	
	# create a new window
	window = tkinter.Tk()
	
	window.rowconfigure(0,weight=1)
	window.rowconfigure(1,weight=1)
	window.columnconfigure(0,weight=1)
	window.columnconfigure(1,weight=1)
	
	# Window title
	window.title("openComtradeViewer")
	
	# Window dimensions and position
	w = 434
	h = 434
	window.resizable(width='false', height='false')
	width = window.winfo_screenwidth()
	height = window.winfo_screenheight()
	posx = (width - w)/2.0
	posy = (height - h)/2.0
	window.geometry('%dx%d+%d+%d' % (w, h, posx, posy))
	
	# Set window icon
	if os.name == "nt":
		window.wm_iconbitmap(default='.\icons\Statistics.ico')
	else:
		#~ Here will be placed the options for Linux/Mac OS X
		pass
	
	# select file to be parsed (label)
	lbl_select = tkinter.Label(window, text="Select lis-file:")

	# Button to call file dialog selection
	# file selection
	def fileSelection():		
		lisFile = tkFileDialog.askopenfilename(title="Select lis-file:")
		
		if len(lisFile) != 0:		
		
			# Update parse button command
			btn_runParser.configure(command=lambda: runParser(lisFile))
			
			# Update lbl_LisFile
			lbl_lisFile.configure(text=os.path.basename(lisFile))		
			
		else: 
			
			# Update lis-file
			lisFile = "none.txt"
			
			# Update parse button command
			btn_runParser.configure(command=lambda: runParser(lisFile))
			
			# Update lbl_LisFile
			lbl_lisFile.configure(text="No file selected")
			
		
	btn_fileSelection = tkinter.Button(window, text="Open", command=fileSelection)
	
	# Label to show the selected file name
	lbl_lisFile = tkinter.Label(window, text="No file selected")
	
	# Button to run parser
	def runParser(lisFile):	
		
		if lisFile != "none.txt" and len(lisFile) != 0:
		
			[runStatus,outputFiles] = lis_stat_parser(["parseATPStats.py",lisFile],1)
			
			if runStatus == 0:
				
				infoText = "Everything seems to went OK! :)\n\nThe output files are saved on directory %s"\
				%(os.path.dirname(lisFile))

				tkMessageBox.showinfo("Parsing finished", infoText)
				
			elif runStatus == 1:
				tkMessageBox.showerror("Parsing finished", "Ooops!\nUnable to open the given lis-file :/")
			elif runStatus == 2:
				tkMessageBox.showerror("Parsing finished", "Ooops!\nThis is not a proper lis-file :/")
			else:
				tkMessageBox.showerror("Parsing finished", "Ooops!\nSomething unexpected happened :/")
				
		else:
			properMsg = "Select a proper lis-file clicking in Open button..."
			print properMsg
			tkMessageBox.showwarning("parseATPStats", "No file selected!\n"+properMsg)
		
	btn_runParser = tkinter.Button(window, text="Parse it!",command=lambda: runParser(lisFile))
	
	# Create menu bar
	menubar = tkinter.Menu(window)
	
	filemenu = tkinter.Menu(menubar, tearoff=0)
	filemenu.add_command(label="Select lis-file...", command=fileSelection)
	#~ filemenu.add_command(label="Run parser...", command=lambda: runParser(lisFile))
	filemenu.add_command(label="Exit", command=window.quit)
	menubar.add_cascade(label="File", menu=filemenu)
	
	helpmenu = tkinter.Menu(menubar, tearoff=0)
	helpmenu.add_command(label="Project page", command=lambda: webbrowser.open(url,new=2))
	helpmenu.add_command(label="About", command=lambda: aboutWin())
	menubar.add_cascade(label="Help", menu=helpmenu)
		
	window.config(menu=menubar)
	
	# Add the widgets to the window screen
	lbl_select.grid(sticky='w',row=0,column=0)
	btn_fileSelection.grid(sticky='w',row=1,column=0)
	lbl_lisFile.grid(sticky='w',row=1,column=1)
	btn_runParser.grid(sticky='nsew',row=2,column=0,columnspan=2)
	
	# draw the window and start the 'app'
	window.mainloop()
