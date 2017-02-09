#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  GUI_Analyses.py
#  
#  Copyright 2017 Leonardo M. N. de Mattos <l@mattos.eng.br>
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
	
import numpy as np
import pylab

# Calculate RMS value
def calcRMS(comtradeObj,analog_curves):

	import tkMessageBox
	from scipy import integrate

	# Check if the selected data are ok
	if len(analog_curves) == 0:
		tkMessageBox.showerror("RMS - Error","Select at least one analog curve!")

	else:
		# previous variables
		dt = 1./comtradeObj.getSamplingRate()
		sizeWin = int(np.ceil(1. / comtradeObj.lf / dt))
		tcyc = sizeWin * dt
		datalen = comtradeObj.getNumberOfSamples()
		t = comtradeObj.getTime()

		# Allocate rms values vector
		xrms = np.zeros(datalen)

		# Generate figure frame
		pylab.figure()

		for i in analog_curves:
			i = int(i)

			# Getting oscillographics values
			x = comtradeObj.getAnalogChannelData(i+1)[:,0]**2.0

			# Compute RMS value for an one cycle window
			for k in xrange(0,datalen):
				xrms[k] = np.sqrt( integrate.trapz( x[k:(sizeWin+k)],t[k:(sizeWin+k)] ) / tcyc )

			# plot result
			label="%s (%s) - RMS"%(comtradeObj.Ach_id[i],comtradeObj.getAnalogUnit(i+1))
			pylab.plot(t,xrms,label=label)

		# Show all plots
		pylab.legend()
		pylab.show()
