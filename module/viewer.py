from tkinter import *
from tkinter import ttk
from module import crawler
from module import parser


class Viewer(Tk):
    def __init__(self):
        super().__init__()

        # Container
        self.title("PE Header Viewer")
        self.geometry("1200x600")
        # self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Menu
        menu_bar = Menu(self)
        menu_file = Menu(menu_bar)
        # menu_file.add_command(label="New")
        # menu_file.add_command(label="Save")
        # menu_file.add_command(label="Print")
        menu_file.add_command(label="Exit", command=self.exit)
        menu_bar.add_cascade(label="File", menu=menu_file)
        # menu_bar.bind('<<MenuSelect>>', self.select_menu)
        self.config(menu=menu_bar)

        # Var
        self.url = StringVar()
        self.log = StringVar()

        # URL Frame
        # left, top, right, bottom
        url_frame = ttk.Frame(self, padding="5 5 5 5")
        url_frame.grid(row=0, column=0, columnspan=2, sticky=(N, W, E, S))
        ttk.Label(url_frame, text="URL", width=5).grid(row=0, column=0, padx=5)
        ttk.Entry(url_frame, width=148, textvariable=self.url).grid(row=0, column=1, padx=5)
        ttk.Button(url_frame, text="search", command=self.search).grid(row=0, column=2)
        # self.bind("<Return>", self.search)

        # Result (Download File List) Frame
        result_frame = ttk.Frame(self, name = "result_frame", padding="5 0 5 5")
        result_frame.grid(row=1, column=0, columnspan=2, sticky=(N, W, E, S))
        ttk.Label(result_frame, text="From", width=5).grid(row=0, column=0, padx=5)
        self.combo_box = ttk.Combobox(result_frame, width=146, state='readonly')
        ttk.Button(result_frame, text="analyze", command=self.analyze).grid(row=0, column=2)
        self.combo_box.grid(row=0, column=1, padx=5)
        # self.combo_box.bind('<<ComboboxSelected>>', self.analyze)

        # Header List Frame
        header_frame = ttk.Frame(self, padding="5 0 0 5")
        header_frame.grid(row=2, column=0, sticky=(N, W, E, S))
        header_tree = ttk.Treeview(header_frame)

        #  Header List Frame - Scroll
        header_scroll = Scrollbar(header_frame, orient=HORIZONTAL)
        header_scroll.pack(side=BOTTOM, fill=X)
        header_tree.pack(fill="both", expand=True)

        # Detail List Frame
        detail_frame = ttk.Frame(self, padding="5 0 5 5")
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
        status_frame = ttk.Frame(self, padding="5 0 5 5")
        status_frame.grid(row=3, column=0, columnspan=2, sticky=(N, W, E, S))
        self.status_label = ttk.Label(status_frame, textvariable=self.log, borderwidth=2, relief="groove")
        self.status_label.pack(fill=BOTH)

    def exit(self):
        self.destroy()

    def search(self, *args):
        url = self.url.get()
        self.log.set("requesting...")
        self.update_combobox(crawler.get_exe_urls(url))

    def update_combobox(self, urls):
        self.combo_box['values'] = urls
        self.combo_box.current(0)
        self.log.set("url for exe updated")

    def analyze(self, *args):
        download_url = self.combo_box.get()
        self.log.set("starting download from [%s]" % download_url)
        file_name = crawler.save_exe(download_url)
        if file_name:
            parser.read_byte(file_name)
            # parse하고 나면 self.content로 저장필요


