# Code from:
# https://stackoverflow.com/questions/43731784/tkinter-canvas-scrollbar-with-grid


import tkinter as tk
from tkinter import *
# ==================================== enabling high DPI for windows ====================================
try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

# ==================================== ACTIONS (functions) to RUN ===================================================

def inject_frame(root,data1):

    Grid.rowconfigure(root, 0, weight=1)
    Grid.columnconfigure(root, 0, weight=1)

    number_rows = len(data1)
    rows = number_rows
    columns = 6

    # Create & Configure frame_main
    frame_main = tk.Frame(root, bg="gray")
    frame_main.grid(sticky=N + S + E + W)
    frame_main.place(x=471.0, y=86.0)

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
    canvas.configure(yscrollcommand=vsb.set, xscrollcommand=vsb.set)
    # Create a frame to contain the entries
    frame_entries = tk.Frame(canvas, bg="blue")
    canvas.create_window((0, 0), window=frame_entries, anchor='nw')

    # Create a 5x10 (rows x columns) grid of buttons inside the frame_main

    entries = [['' for j in range(columns)] for i in range(rows + 1)]

    #######  LOGFILE column
    entries[0][0] = tk.Entry(frame_entries, width=3)
    entries[0][0].insert(0, "Logfile")
    entries[0][0].grid(row=0, column=0, sticky='news')
    #######  LINE NUM
    entries[0][1] = tk.Entry(frame_entries, width=2)
    entries[0][1].insert(0, "Line num")
    entries[0][1].grid(row=0, column=1, sticky='news')
    ####### Issue found
    entries[0][2] = tk.Entry(frame_entries, width=20)
    entries[0][2].insert(0, "Issue found")
    entries[0][2].grid(row=0, column=2, sticky='news')
    ####### DESCRIPTION
    entries[0][3] = tk.Entry(frame_entries,width=15)
    entries[0][3].insert(0, "Description")
    entries[0][3].grid(row=0, column=3, sticky='news')
    ####### SOLUTION Matching KB or Mantis
    entries[0][4] = tk.Entry(frame_entries, width=50)
    entries[0][4].insert(0, "Link to solution (KB/Mantis/..)")
    entries[0][4].grid(row=0, column=4, sticky='news')
    ####### Whole LOG
    entries[0][5] = tk.Entry(frame_entries)
    entries[0][5].insert(0, "Whole Log line")
    entries[0][5].grid(row=0, column=5, sticky='news')

    for i in range(6):
        entries[0][i].config(state='disabled')

    for i in range(1, rows + 1):
        Grid.rowconfigure(frame_entries, i, weight=1)
        for j in range(columns):
            if (j == 0):
                entries[i][j] = tk.Entry(frame_entries, width=3,font='bold')  #
            if (j == 1):
                entries[i][j] = tk.Entry(frame_entries, width=2,font='bold')  #
            if (j == 2):
                entries[i][j] = tk.Entry(frame_entries, width=20, fg='blue',font='bold')  #
            if (j == 3):
                entries[i][j] = tk.Entry(frame_entries, width=15, font='bold')  #
            if (j == 4):
                entries[i][j] = tk.Entry(frame_entries, width=50, fg='blue',font='bold')  #
            else:
                entries[i][j] = tk.Entry(frame_entries,font='bold')
            # create a button inside frame_main
            entries[i][j].insert(0, data1[i - 1][j])
            entries[i][j].grid(row=i, column=j, sticky=N + S + E + W)

    # Update entries frames idle tasks to let tkinter calculate entries sizes
    frame_entries.update_idletasks()

    # Resize the canvas frame to show exactly 6-by-20 entries and the scrollbar
    first_columns_width = sum([entries[0][j].winfo_width() for j in range(0, 6)])
    if (number_rows < 22):
        first_rows_height = sum([entries[i][0].winfo_height() for i in range(0, number_rows)]) + 70
    else:
        first_rows_height = sum([entries[i][0].winfo_height() for i in range(0, 22)])
    frame_canvas.config(width=first_columns_width + vsb.winfo_width(),
                        height=first_rows_height + vsa.winfo_height())

    # Set the canvas scrolling region
    canvas.config(scrollregion=canvas.bbox("all"))

    frame_entries.grid_rowconfigure(0, weight=1)
    frame_entries.grid_columnconfigure(0, weight=1)

    return (frame_main,frame_canvas,canvas)

#root = tk.Tk()

#inject_frame(root)

#root.mainloop()
