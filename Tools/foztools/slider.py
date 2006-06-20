# -*- coding: utf-8 -*-
#!/usr/local/bin/python
import Tkinter
from foztools import Slider

Tk=Tkinter

def main():
    class Test:
        def __init__(self):
            win = Tk.Frame()
            win.master.title("Slider Demo")
            self.progress1=Slider(win, fillColor="red", labelColor="yellow",
                                  value=0, width=200, height=15,
                                  appearance="sunken", autoLabel="false",
                                  labelFormat="%s",
                                  labelText="Gary.Foster@corp.sun.com",
                                  orientation="horizontal", bd=3)
            self.progress2=Slider(win, fillColor="blue", labelColor="black",
                                  background="white", value=250, width=50,
                                  height=200, appearance="raised", max=250,
                                  labelFormat="%d", orientation="vertical", bd=4)
            self.progress1.frame.pack()
            self.progress2.frame.pack()
            win.pack()
            self.progress1.frame.after(1000, self.update)
            self.increment1=1
            self.increment2=-1

        def update(self, event=None):
            bar1=self.progress1
            bar2=self.progress2

            bar1.value=bar1.value+self.increment1
            if bar1.value > bar1.max:
                self.increment1=-1
                bar1.fillColor="green"
                bar1.labelColor="red"
            if bar1.value < bar1.min:
                self.increment1=1
                bar1.fillColor="red"
                bar1.labelColor="yellow"
            bar1.update()
            bar1.frame.after(100, self.update)

            bar2.value=bar2.value+self.increment2
            if bar2.value > bar2.max:
                self.increment2=-1
            if bar2.value < bar2.min:
                self.increment2=1
            bar2.update()

    t = Test()
    Tk.mainloop()

if __name__=="__main__":
    main()
