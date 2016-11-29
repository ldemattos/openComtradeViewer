#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  GUI_Plot.py
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

from matplotlib.widgets import Cursor
import matplotlib.pyplot as plt

# Method for plotting data
def runPlot(analog_curves,digital_curves,comtradeObj):
	
	# Checking if there are selecte variables
	if len(digital_curves) > 0 or len(analog_curves) > 0:
	
		# Commom stuff
		fig = plt.figure()
		ax = fig.add_subplot(111, axisbg='#FFFFCC')
		ax.grid()	
		cursor = Cursor(ax, useblit=True, color='red', linewidth=1)
	
		# plot analog selected data
		if len(analog_curves) > 0:
			for i in analog_curves:
				i = int(i)
				label="%s (%s)"%(comtradeObj.Ach_id[i],comtradeObj.getAnalogUnit(i+1))
				ax.plot(comtradeObj.getTime(),comtradeObj.getAnalogChannelData(i+1),\
				label=label,linewidth=2)
				
		# plot digital selected data
		if len(digital_curves) > 0:
			for i in digital_curves:			
				i = int(i)
				label="%s"%(comtradeObj.Dch_id[i])
				ax.plot(comtradeObj.getTime(),comtradeObj.getDigitalChannelData(i+1),\
				label=label,linewidth=2)
		
		# Show the plot image
		ax.legend()
		plt.show()	

	return(None)
