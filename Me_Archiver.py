#==========================
#Me_Archiver 2.0 Update
#Implements OOP Structure
#Author: MevanKoda
#==========================

import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

class App():
    def __init__(self):
        self.folder_path = ""
        self.destination = ""

        self.root = tk.Tk()
        self.root.title("Me Archiver")
        self.root.geometry("500x500")

        self.label = tk.Label(self.root,text="ME ARCHIVER 2.0", font=('TkHeadingFont',20))
        self.label.pack(padx=20, pady=20)

        self.slogan = tk.Label(self.root, text="Simple & Light", font=('TkCaptionFont', 15))
        self.slogan.pack()

        #Enter File Path
        self.file_label = tk.Label(self.root, text="Enter File Path", font=('TkHeadingFont', 10))
        self.file_label.pack(padx=20, pady=20)
        self.path_input = tk.Entry(self.root, font=('TkTextFont',10),width =50)
        self.path_input.pack(padx=20, pady=10)
        self.browser_btn = tk.Button(self.root, text="Browse", font=("TkTextFont",10), command= self.select_folder)
        self.browser_btn.pack(padx=20)

        #Archive Destination
        self.archive_label = tk.Label(self.root, text="Enter Destination", font=('TkHeadingFont',10))
        self.archive_label.pack(padx=20, pady=20)
        self.arc_path_input = tk.Entry(self.root, font=('TkTextFont',10),width=50)
        self.arc_path_input.pack(padx=20)
        self.browse_btn = tk.Button(self.root,text="Browse",font=("TkTextFont",10), command= self.select_dest)
        self.browse_btn.pack(padx=20, pady=10)

        self.archive_btn = tk.Button(self.root, text="Archive", font=("TkHeadingFont",15),command=self.archive_folder,height=2, width=20)
        self.archive_btn.pack(padx=20,pady=10)
        self.root.mainloop()

    def select_folder(self):
        self.folder_path = filedialog.askdirectory()

        self.path_input.insert(0,self.folder_path)
        if self.folder_path:
            print(f"Folder Path={self.folder_path}")
        else:
            print("No Folder Selected")
        return self.folder_path

    def select_dest(self):
        self.destination = filedialog.askdirectory()
        self.archive_name = input("Enter Zip Name :- ")
        self.arc_path_input.insert(0, self.destination)
        if self.destination:
            print(f"Archive Destination = {self.destination}")
        else:
            print("No Destination Selected")
        return self.destination

    def archive_folder(self):
        try:
            shutil.make_archive((self.destination+"/"+self.archive_name),'zip',self.folder_path)
            print(f"Archived Successfully✅ at {self.archive_name}")
            self.path_input.delete(0,tk.END)
            self.arc_path_input.delete(0,tk.END)
            messagebox.showinfo("Me Archiver 2.0", "Archived Successfully")
        except:
            print("Archive Failed😥")

App()