import tkinter as tk
from tkinter import filedialog


class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.title = tk.Label(master=self.master, text="Upload file to scan")
        self.dialog_button = tk.Button(master=self.master, text="Upload",
                                    command=self.open_file_dialog, width=15)
        self.title.pack(pady=30)
        self.dialog_button.pack(pady=10)

    def open_file_dialog(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Log Files","*.log")])
        print(self.file_path)

root = tk.Tk()
root.title("OFCDebug Reader")
root.geometry('275x200')
app = Application(master=root)
app.mainloop()