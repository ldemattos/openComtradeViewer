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
		tkMessageBox.showerror("COMTRADE Information - Error", "Please select a valid COMTRADE data file first")
