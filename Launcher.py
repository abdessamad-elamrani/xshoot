import tkinter as tk
import TshootWindow
import AnalyseWindow

# the first gui owns the root window
win1 = tk.Tk()
gui1 = AnalyseWindow.GUI(win1)
gui1.pack(fill="both", expand=True)

# the second GUI is in a Toplevel
win2 = tk.Toplevel(win1)
gui2 = TshootWindow.GUI(win2)
gui2.pack(fill="both", expand=True)

tk.mainloop()