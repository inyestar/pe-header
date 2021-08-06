from tkinter import *
from tkinter import ttk


# *args is used to pass a variable number of arguments
def search(*args):
    value = url.get()
    log.set("getting from %s" % value)


# Container
container = Tk()
container.title("PE Header Viewer")
container.geometry("1200x600")
# container.grid_rowconfigure(1, weight=1)
container.grid_rowconfigure(2, weight=1)
container.grid_columnconfigure(1, weight=1)

# Menu
menu_bar = Menu(container)
menu_file = Menu(menu_bar)
menu_file.add_command(label="New")
menu_file.add_command(label="Save")
menu_file.add_command(label="Print")
menu_file.add_command(label="Exit")
menu_bar.add_cascade(label="File", menu=menu_file)
container.config(menu=menu_bar)

# Var
url = StringVar()
log = StringVar()

# Style
# style = ttk.Style()
# style.configure('status.TFrame', background='white')
# style.configure('status.TLabel', background= 'white')

# URL Frame
url_frame = ttk.Frame(container, padding="5 5 5 5")
url_frame.grid(row=0, column=0, columnspan=2, sticky=(N, W, E, S))
ttk.Label(url_frame, text="URL").grid(row=0, column=0, padx=5)
ttk.Entry(url_frame, width=150, textvariable=url).grid(row=0, column=1, padx=5)
ttk.Button(url_frame, text="search", command=search).grid(row=0, column=2, padx=5)

# Result (Download File List) Frame
result_frame = ttk.Frame(container, padding="5 5 5 5")
result_frame.grid(row=1, column=0, columnspan=2, sticky=W)
ttk.Label(result_frame, text="No Result, Search First").grid(row=0, column=0)
# result_radio1 = ttk.Radiobutton(result_frame, text="test1", value=0)
# result_radio2 = ttk.Radiobutton(result_frame, text="test2", value=1)
# result_radio1.pack()
# result_radio2.pack()

# Header List Frame
header_frame = ttk.Frame(container)
header_frame.grid(row=2, column=0,  sticky=(N, W, E, S))
header_tree = ttk.Treeview(header_frame)

#  Header List Frame - Scroll
header_scroll = Scrollbar(header_frame, orient=HORIZONTAL)
header_scroll.pack(side=BOTTOM, fill=X)
header_tree.pack(fill="both", expand=True)

# Detail List Frame
detail_frame = ttk.Frame(container)
detail_frame.grid(row=2, column=1, sticky=(N, W, E, S))
detail_tree = ttk.Treeview(detail_frame)

#  Detail List Frame - Scroll
detail_scroll = Scrollbar(detail_frame, orient=VERTICAL)
detail_scroll.pack(side=RIGHT, fill=Y)
detail_tree.pack(fill="both", expand=True)

#  Detail List Frame - Column
detail_tree['columns'] = ('pFile', 'Raw Data', 'Value')
detail_tree.column('#0', width=0, stretch=NO)
detail_tree.column('pFile', anchor=CENTER)
detail_tree.column('Raw Data', anchor=CENTER)
detail_tree.column('Value', anchor=CENTER)
detail_tree.heading('#0', text='', anchor=CENTER)
detail_tree.heading('pFile', text='pFile', anchor=CENTER)
detail_tree.heading('Raw Data', text='Raw Data', anchor=CENTER)
detail_tree.heading('Value', text='Value', anchor=CENTER)
detail_tree.insert(parent='', index=0, iid=0, text='', values=('1', 'Vineet', 'Alpha'))

# Status Frame
status_frame = ttk.Frame(container, padding="5 0 5 5")
status_frame.grid(row=3, column=0, columnspan=2, sticky=(N, W, E, S))
status_label = ttk.Label(status_frame, textvariable=log)
status_label.pack(anchor=E)

# Execute
# input_url.focus()
container.bind("<Return>", search)
container.mainloop()