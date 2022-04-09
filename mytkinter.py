import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
from tkinter import filedialog
from monitorer import Monitorer

# ==================================== enabling high DPI for windows ====================================
try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

# ==================================== ACTIONS (functions) to RUN ===================================================


def getFolderPath():
    folder_selected = filedialog.askdirectory()
    folderPath.set(folder_selected)


def load():
    f = open(filename.get(), 'r')
    host_entry.insert(0, f.readline().strip())
    user_entry.insert(0, f.readline().strip())
    paswd_entry.insert(0, f.readline().strip())
    interval_entry.insert(0, f.readline())
    iterations_entry.insert(0, f.readline())
    ### rest of lines in file are commands, getting them into list
    tempcomm = []
    for x in f:
        tempcomm.append(x)
    #### inserting the whole list to text area ( converting  list tempcomm to text again via ''.join(xx))
    textarea.insert(1.0, ''.join(tempcomm))

def run():
    # def __init__(self, host, user, passwd, sla, commands, iterations):
    print(
        f"lets run monitor.py, on this host {hostname.get()} and username/passowrd is {username.get()}/{password.get()}!")
    commands = textarea.get('1.0', 'end').splitlines()
    print('###')
    print("selected mode is: "+size_or_time.get())
    print(folderPath.get())
    print('###')
    m1 = Monitorer(hostname.get(), username.get(), password.get(), int(interval.get()), commands, int(iterations.get())-1, folderPath.get(),size_or_time.get())
    m1.start()


# ==================================== Root frame and Variables ===================================================


root = tk.Tk()
root.title('Fortigate Monitoring Tool')

hostname = tk.StringVar()
username = tk.StringVar()
password = tk.StringVar()
commands = tk.StringVar()
filename = tk.StringVar()
interval = tk.StringVar()
iterations = tk.StringVar()
size_or_time = tk.StringVar()
folderPath = tk.StringVar()

# ======================================== HOSTNAME ========================================================

##### label hostname  title to show on left side
host_label = ttk.Label(root, text="Firewall Hostname: ")
host_label.pack()
##### entry  to read hostname, and put in variable hostname
host_entry = ttk.Entry(root, width=15, textvariable=hostname)
host_entry.pack()
host_entry.focus()

# ======================================= USERNAME  ===========================================================


##### label username title to show on left side
user_label = ttk.Label(root, text="Username: ")
user_label.pack()
##### entry field to read username, and put in variable username
user_entry = ttk.Entry(root, width=15, textvariable=username)
user_entry.pack()
user_entry.focus()

# ====================================== PASSWORD =====================================================


##### label password title to show on left side
paswd_label = ttk.Label(root, text="Password: ")
paswd_label.pack()
##### entry field to read password, and put in variable username
paswd_entry = ttk.Entry(root, width=15, textvariable=password)
paswd_entry.pack()
paswd_entry.focus()


# ====================================== INTERVAL  ==================================================


##### label password title to show on left side
interval_label = ttk.Label(root, text="Interval between each round: ")
interval_label.pack()
##### entry field to read password, and put in variable username
interval_entry = ttk.Entry(root, width=15, textvariable=interval)
interval_entry.pack()
interval_entry.focus()

# ====================================== ITERATIONS  ==================================================


##### label password title to show on left side
iterations_label = ttk.Label(root, text="Max number of rounds: ")
iterations_label.pack()
##### entry field to read password, and put in variable username
iterations_entry = ttk.Entry(root, width=15, textvariable=iterations)
iterations_entry.pack()
iterations_entry.focus()

# ====================================== FolderPath  ==================================================

iterations_label = ttk.Label(root, text="Select where to save logs: ")
iterations_label.pack()
##### Button to select Folder
btnFind = ttk.Button(root, text="Browse Folder", command=getFolderPath)
btnFind.pack()

# ====================================== LoggingType Size Based or Time Based  ==================================================


##### label logging type
loggingtype_label = ttk.Label(root, text="Select if you want to log by Size or Time")
loggingtype_label.pack()
##### Radio buttons to select size or time !
r1 = ttk.Radiobutton(root,text="size based", value="s", variable=size_or_time)
r2 = ttk.Radiobutton(root,text="time based", value="t", variable=size_or_time)
r1.pack()
r1.focus()
r2.pack()
r2.focus()
# ==================================== COMMANDS   ====================================================

##### label commands title to show on left side
comm_label = ttk.Label(root, text="Commands: ")
comm_label.pack()
##### textarea to read commands, to read them, you can use get ('1.0','end') check greet funtion
textarea = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=30)
textarea.pack()
textarea.focus()




# =================================== LOAD  SETTINGS FROM FILE in same Folder as App ==============================================


##### label settings title to show on left side
settings_label = ttk.Label(root, text="Specify  file with existing settings: ")
settings_label.pack()
##### entry field to read file, and put in variable username
filename_entry = ttk.Entry(root, width=15, textvariable=filename)
filename_entry.pack()
filename_entry.focus()

##### button toload  settings from a local test file with firewall settings ip,username,password
load_button = ttk.Button(root, text="Load", command=load, )
load_button.pack()


# =================================== Start the Test ==============================================


##### if you click on this button, it will Start the test (call monitorer)
greet_button = ttk.Button(root, text="Start", command=run, )
greet_button.pack()


# =================================== Quiet the App  ==============================================


##### Quit button to quit the root window
quit_button = ttk.Button(root, text="Quit", command=root.destroy)
quit_button.pack()

root.mainloop()
