"""
    Ce module propose la classe TOOLTIP pour
    mettre en oeuvre les bulles d'aide
"""

import Tkinter

class TOOLTIP:
    def __init__(self,widget):
        self.widget=widget
        self.text = None
        self.timer = None
        self.tooltip = None
        self.label = None
        self.bindings = []
        self.bindings.append(self.widget.bind("<Enter>", self._enter))
        self.bindings.append(self.widget.bind("<Leave>", self._leave))
        self.bindings.append(self.widget.bind("<ButtonPress>", self._leave))
        # user overrideable settings
        self.time = 1000                    # milliseconds
        self.relief = Tkinter.SOLID
        self.justify = Tkinter.LEFT
        self.fg = "#000000"
        self.bg = "#ffffe0"
        self.xoffset = 20
        self.yoffset = 1

    def setText(self, text):
        self.text = text

    def _unbind(self):
        if self.bindings and self.widget:
            self.widget.unbind("<Enter>", self.bindings[0])
            self.widget.unbind("<Leave>", self.bindings[1])
            self.widget.unbind("<ButtonPress>", self.bindings[2])
            self.bindings = []

    def destroy(self):
        self._unbind()
        self._leave()

    def _enter(self, *event):
        after_cancel(self.timer)
        self.timer = after(self.widget, self.time, self._showTip)

    def _leave(self, *event):
        after_cancel(self.timer)
        self.timer = None
        if self.tooltip:
            self.label.destroy()
            destruct(self.label)
            self.label = None
            self.tooltip.destroy()
            destruct(self.tooltip)
            self.tooltip = None

    def _showTip(self):
        if self.tooltip or not self.text:
            return
        c = self.widget.__class__
        if c in (Tkinter.Button,):
            if self.widget["state"] == Tkinter.DISABLED:
                return
        x = self.widget.winfo_rootx()
        y = self.widget.winfo_rooty() + self.widget.winfo_height()
        x = x + self.xoffset
        y = y + self.yoffset
        self.tooltip = Tkinter.Toplevel()
        self.tooltip.wm_iconify()
        self.tooltip.wm_overrideredirect(1)
        self.tooltip.wm_protocol("WM_DELETE_WINDOW", self.destroy)
        self.label = Tkinter.Label(self.tooltip, text=self.text,
                         relief=self.relief, justify=self.justify,
                         fg=self.fg, bg=self.bg, bd=1, takefocus=0)
        self.label.pack(ipadx=1, ipady=1)
        self.tooltip.wm_geometry("%+d%+d" % (x, y))
        self.tooltip.wm_deiconify()

