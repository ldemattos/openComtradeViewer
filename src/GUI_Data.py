#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  GUI_Data.py
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

def OscilloInfo(comtradeObj):
	
	import tkMessageBox

	if comtradeObj != None:
		infoText = ("Substation: %s\n"
		"Recorder: %s\n"
		"System frequency: %i Hz\n"
		"Total samples: %i\n"
		"Samples per cycle: %i")%\
		(comtradeObj.station_name.strip(),\
		comtradeObj.rec_dev_id.strip(),\
		comtradeObj.lf,\
		comtradeObj.getNumberOfSamples(),\
		int(1./comtradeObj.lf*comtradeObj.getSamplingRate()))
		tkMessageBox.showinfo("COMTRADE Information", infoText)
		
	else:		
		tkMessageBox.showerror("COMTRADE Information - Error","Please select a valid COMTRADE data file first")
		
def exportData(comtradeObj,analog_curves,digital_curves):
	
	import tkFileDialog
	import tkMessageBox
	import numpy as np
	
	# Options for file dialog
	options = {}
	options['defaultextension'] = '.dat'
	options['filetypes'] = [('ASCII data file', '.dat'),('All Files', '.*')]
	options['title'] = 'Select file to export data:'	
	dataFile = tkFileDialog.asksaveasfilename(**options)
	
	if len(dataFile) != 0 and (len(analog_curves) or len(digital_curves)):
		
		# open data file
		fp_dataFile = open(dataFile,'w+')
		
		# common variables
		sam_len = comtradeObj.getNumberOfSamples()
		time = comtradeObj.getTime()
		
		# start writing the header
		fp_dataFile.write("# time")
		
		# Export analog curves
		if len(analog_curves) > 0:
			
			# Write headers and Retrieve data			
			data = np.zeros(shape=(sam_len,len(analog_curves)))
			j = 0
			for i in analog_curves:
				i = int(i)
				fp_dataFile.write(" %s"%(comtradeObj.Ach_id[i]))
				data[0:sam_len,j:j+1] = comtradeObj.getAnalogChannelData(i+1)
				j += 1
			
			fp_dataFile.write("\n")
			
			# Finally write it to the text file
			for i in xrange(0,sam_len):
				fp_dataFile.write("%f"%(time[i]))

				for j in xrange(0,len(analog_curves)):
					fp_dataFile.write(" %f"%(data[i,j]))
				
				fp_dataFile.write("\n")
		
		# Export digital curves	
		else:
			
			# Write headers and Retrieve data
			data = np.zeros(shape=(sam_len,len(digital_curves)))
			j = 0
			for i in digital_curves:
				i = int(i)
				fp_dataFile.write(" %s"%(comtradeObj.Dch_id[i]))
				data[0:sam_len,j:j+1] = comtradeObj.getDigitalChannelData(i+1)
				j += 1
			
			fp_dataFile.write("\n")
			
			# Finally write it to the text file
			for i in xrange(0,sam_len):
				fp_dataFile.write("%f"%(time[i]))

				for j in xrange(0,len(digital_curves)):
					fp_dataFile.write(" %f"%(data[i,j]))
				
				fp_dataFile.write("\n")
			
		# close data file
		fp_dataFile.close
		
	elif(len(dataFile)) != 0:
		tkMessageBox.showerror("Export selected data failed","No analog or digital data selected!")
