# $Header: /home/eficas/CVSROOT/EficasV1/Tools/foztools/foztools.py,v 1.1.1.1 2001/12/04 15:38:23 eficas Exp $

###########################################################################
# This is a set of Python widgets, built on top of pythonTk.  They are
# designed to be highly customizable, flexible, and useful.  They are
# also all built from the base PythonTk widgets so no other external
# libraries are needed.
#
# Use it in good health.  It's hereby released under the GPL, if you
#  have questions about the GPL contact the Free Software Foundation.
#
# Author: Gary D. Foster <Gary.Foster@corp.sun.com>
#  with some ideas stolen from Mitch Chapman's stuff.
#
###########################################################################

__version__ = "$Revision: 1.1.1.1 $"

import Tkinter
Tk=Tkinter

class Slider:
    def __init__(self, master=None, orientation="horizontal", min=0, max=100,
		 width=100, height=25, autoLabel="true", appearance="sunken",
		 fillColor="blue", background="black", labelColor="yellow",
		 labelText="", labelFormat="%d%%", value=50, bd=2):
	# preserve various values
	self.master=master
	self.orientation=orientation
	self.min=min
	self.max=max
	self.width=width
	self.height=height
	self.autoLabel=autoLabel
	self.fillColor=fillColor
	self.labelColor=labelColor
	self.background=background
	self.labelText=labelText
	self.labelFormat=labelFormat
	self.value=value
	self.frame=Tk.Frame(master, relief=appearance, bd=bd)
	self.canvas=Tk.Canvas(self.frame, height=height, width=width, bd=0,
			      highlightthickness=0, background=background)
	self.scale=self.canvas.create_rectangle(0, 0, width, height,
						fill=fillColor)
	self.label=self.canvas.create_text(self.canvas.winfo_reqwidth() / 2,
					   height / 2, text=labelText,
					   anchor="c", fill=labelColor)
	self.update()
	self.canvas.pack(side='top', fill='x', expand='no')

    def update(self):
	# Trim the values to be between min and max
	value=self.value
	if value > self.max:
	    value = self.max
	if value < self.min:
	    value = self.min
	# Preserve the new value
	c=self.canvas
	# Adjust the rectangle
	if self.orientation == "horizontal":
	    c.coords(self.scale,
		     0, 0,
		     float(value) / self.max * self.width, self.height)
	else:
	    c.coords(self.scale,
		     0, self.height - (float(value) / self.max*self.height),
		     self.width, self.height)
	# Now update the colors
	c.itemconfig(self.scale, fill=self.fillColor)
	c.itemconfig(self.label, fill=self.labelColor)
	# And update the label
	if self.autoLabel=="true":
	    c.itemconfig(self.label, text=self.labelFormat % value)
	else:
	    c.itemconfig(self.label, text=self.labelFormat % self.labelText)
	c.update_idletasks()

class Indicator:
    def __init__(self, master=None, width=25, height=25, appearance="sunken",
		 onColor="green", offColor="black", onLabelColor="black",
		 offLabelColor="green", onLabelText="", offLabelText="",
		 on=1, bd=2):
	# preserve various values
	self.master=master
	self.onColor=onColor
	self.offColor=offColor
	self.onLabelColor=onLabelColor
	self.offLabelColor=offLabelColor
	self.onLabelText=onLabelText
	self.offLabelText=offLabelText
	self.on=on
	self.frame=Tk.Frame(master, relief=appearance, bd=bd)
	self.canvas=Tk.Canvas(self.frame, height=height, width=width, bd=0,
			      highlightthickness=0)
	self.light=self.canvas.create_rectangle(0, 0, width, height,
						fill=onLabelColor)
	self.label=self.canvas.create_text(self.canvas.winfo_reqwidth() / 2,
					   height / 2, text=onLabelText,
					   anchor="c", fill=onLabelColor)
	self.update()
	self.canvas.pack(side="top", fill='x', expand='no')

    def update(self):
	c=self.canvas
	# now update the status
	if self.on:
	    c.itemconfig(self.light, fill=self.onColor)
	    c.itemconfig(self.label, fill=self.onLabelColor)
	    c.itemconfig(self.label, text=self.onLabelText)
	else:
	    c.itemconfig(self.light, fill=self.offColor)
	    c.itemconfig(self.label, fill=self.offLabelColor)
            c.itemconfig(self.label, text=self.offLabelText)
	c.update_idletasks()

    def toggle(self):
	self.on=not self.on
	self.update()

    def turnon(self):
	self.on=1
	self.update()

    def turnoff(self):
	self.on=0
	self.update()

class Blinker(Indicator):
    def __init__(self, master=None, blinkrate=1, enabled=1, width=25,
		 height=25, appearance="sunken", onColor="green",
		 offColor="black", onLabelColor="black", offLabelColor="green",
		 onLabelText="", offLabelText="", on=1, bd=2):
	self.blinkrate=blinkrate
	self.enabled=enabled
	Indicator.__init__(self, master, width=width, height=height,
			     appearance=appearance, onColor=onColor,
			     offColor=offColor, onLabelColor=onLabelColor,
			     offLabelColor=offLabelColor,
			     onLabelText=onLabelText,
			     offLabelText=offLabelText, on=on, bd=bd)

    def update(self):
	if self.enabled:
	    self.on=not self.on
        Indicator.update(self)
	self.frame.after(self.blinkrate * 1000, self.update)

    
