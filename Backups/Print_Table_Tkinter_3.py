# Code from:
# https://stackoverflow.com/questions/43731784/tkinter-canvas-scrollbar-with-grid


import tkinter as tk
from tkinter import *
from tkinter import ttk


class gridFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        


        frame_main = tk.Frame(self, bg="gray")
        frame_main.grid(sticky='news')
        frame_main.place(x = 471.0, y = 86.0)

        # Create a frame for the canvas with non-zero row&column weights
        frame_canvas = tk.Frame(frame_main)
        frame_canvas.grid(row=2, column=0, pady=(5, 0), sticky='nw')
        frame_canvas.grid_rowconfigure(0, weight=1)
        frame_canvas.grid_columnconfigure(0, weight=1)
        # Set grid_propagate to False to allow 5-by-5 entries resizing later
        frame_canvas.grid_propagate(False)

        # Add a canvas in that frame
        canvas = tk.Canvas(frame_canvas, bg="yellow")
        canvas.grid(row=0, column=0, sticky="news")

        # Link a scrollbar to the canvas
        vsb = tk.Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
        vsb.grid(row=0, column=1, sticky='ns')


        # Link a scrollbar to the canvas
        vsa = tk.Scrollbar(frame_canvas, orient="horizontal", command=canvas.xview)
        vsa.grid(row=1, column=0, sticky='ew')

        # configure
        canvas.configure(yscrollcommand=vsb.set,xscrollcommand=vsb.set)

        # Create a frame to contain the entries
        frame_entries = tk.Frame(canvas, bg="blue")
        canvas.create_window((0, 0), window=frame_entries, anchor='nw')

        # Add 9-by-5 entries to the frame
        rows = 40
        columns = 6
        entries = [[tk.Button() for j in range(columns)] for i in range(rows)]
        for i in range(0, rows):
            for j in range(0, columns):
                if(j==1):   ## make line number small 10 width
                    entries[i][j] = tk.Entry(frame_entries, text=("%d,%d" % (i + 1, j + 1)),width=10)
                    entries[i][j].grid(row=i, column=j, sticky='news')
                if(j==2):   ## log entry
                    entries[i][j] = tk.Entry(frame_entries, text=("%d,%d" % (i + 1, j + 1)),width=40)
                    entries[i][j].grid(row=i, column=j, sticky='news')
                else:
                    entries[i][j] = tk.Entry(frame_entries, text=("%d,%d" % (i + 1, j + 1)))
                    entries[i][j].grid(row=i, column=j, sticky='news')

        # Update entries frames idle tasks to let tkinter calculate entries sizes
        frame_entries.update_idletasks()

        # Resize the canvas frame to show exactly 6-by-20 entries and the scrollbar
        first5columns_width = sum([entries[0][j].winfo_width() for j in range(0, 4)])
        first5rows_height = sum([entries[i][0].winfo_height() for i in range(0, 22)])
        frame_canvas.config(width=first5columns_width + vsb.winfo_width(),
                            height=first5rows_height + vsa.winfo_height())
        # Set the canvas scrolling region
        canvas.config(scrollregion=canvas.bbox("all"))

        ### add titles, and disable them
        entries[0][0].insert(0, "logfile")
        entries[0][1].insert(0, "line number")
        entries[0][2].insert(0, "matched log")
        entries[0][3].insert(0, "signature used")
        entries[0][4].insert(0, "solution/reference")
        entries[0][5].insert(0, "more info")

        for i in range(6):
            entries[0][i].config(state='disabled')

        frame_entries.grid_rowconfigure(0, weight=1)
        frame_entries.grid_columnconfigure(0, weight=1)

self = tk.Tk()

inject_frame(self)

self.mainloop()
