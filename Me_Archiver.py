#==========================
#Me_Archiver 3.0 Update
#Implements OOP Structure
#CustomTkinter GUI for better UI
#Author: MevanKoda
#==========================

import shutil
import customtkinter as tk
import ctkmessagebox2 as messagebox
from customtkinter import filedialog

class App():
    def __init__(self):
        self.folder_path = ""
        self.destination = ""

        self.root = tk.CTk()
        self.root.title("Me Archiver")
        self.root.geometry("500x500")

        self.label = tk.CTkLabel(self.root,text="ME ARCHIVER 3.0", font=('CTkHeadingFont',30),text_color="lightblue")
        self.label.pack(padx=20, pady=20)

        self.slogan = tk.CTkLabel(self.root, text="Simple & Light", font=('CTkCaptionFont', 15))
        self.slogan.pack()


        self.frame1 = tk.CTkFrame(self.root)
        self.frame1.pack(padx=40,pady=(10,0))
        #initialize grid
        self.frame1.grid_columnconfigure(0, weight=1)
        self.frame1.grid_columnconfigure(1, weight=1)

        self.frame1.grid_rowconfigure(0, weight=1)
        self.frame1.grid_rowconfigure(1, weight=1)

        #Enter File Path
        self.file_label = tk.CTkLabel(self.frame1, text="Enter File Path", font=('CTkHeadingFont', 15),anchor="w")
        self.file_label.grid(row=0,column=0,padx=20, pady=(10,0),sticky="ew")
        self.path_input = tk.CTkEntry(self.frame1, font=('TkTextFont',10),width =350)
        self.path_input.grid(row=1, column=0,padx=20, pady=10)
        self.browser_btn = tk.CTkButton(self.frame1, text="Browse", font=("TkTextFont",10), command= self.select_folder)
        self.browser_btn.grid(row=1,column=1,padx=20)

        self.frame2 = tk.CTkFrame(self.root)
        self.frame2.pack(pady=(10, 10))
        # initialize grid
        self.frame2.grid_columnconfigure(0, weight=1)
        self.frame2.grid_columnconfigure(1, weight=1)
        self.frame2.grid_columnconfigure(2, weight=1)

        self.frame2.grid_rowconfigure(0, weight=1)
        self.frame2.grid_rowconfigure(1, weight=1)
        #Zip Name
        self.name_label = tk.CTkLabel(self.frame2, text="Enter name", font=('CTkHeadingFont',15),anchor="w")
        self.name_label.grid(row=0,column=0,padx=20, pady=(10,0),sticky="ew")
        self.name_input = tk.CTkEntry(self.frame2,font=('CTkTextFont',10),width= 200)
        self.name_input.grid(row=1,column=0,padx=20,pady=10)
        self.type_label = tk.CTkLabel(self.frame2, text="Type",font=('CTkHeadingFont',15),anchor="w")
        self.type_label.grid(row=0,column=1,sticky="ew",padx=20,pady=(10,0))
        self.type_drop_down= tk.CTkOptionMenu(self.frame2, values=["zip","tar","gztar","bztar","xztar","zstdtar"])
        self.type_drop_down.grid(row=1,column=1,padx=20,pady=10)


        self.frame3 = tk.CTkFrame(self.root)
        self.frame3.pack(padx=40, pady=(10, 0))
        # initialize grid
        self.frame3.grid_columnconfigure(0, weight=1)
        self.frame3.grid_columnconfigure(1, weight=1)

        self.frame3.grid_rowconfigure(0, weight=1)
        self.frame3.grid_rowconfigure(1, weight=1)
        #Archive Destination
        self.archive_label = tk.CTkLabel(self.frame3, text="Enter Destination", font=('CTkHeadingFont',15),anchor="w")
        self.archive_label.grid(row=0,column=0,padx=20, pady=(10,0), sticky="ew")
        self.arc_path_input = tk.CTkEntry(self.frame3, font=('TkTextFont',10),width=350)
        self.arc_path_input.grid(row=1,column=0,padx=20)
        self.browse_btn = tk.CTkButton(self.frame3,text="Browse",font=("TkTextFont",10), command= self.select_dest)
        self.browse_btn.grid(row=1,column=1,padx=20, pady=10)

        self.archive_btn = tk.CTkButton(self.root, text="Archive", font=("CTkHeadingFont",15),command=self.archive_folder,fg_color="green", text_color="white", hover_color="darkgreen",width=100,height=35)
        self.archive_btn.pack(padx=20,pady=20)
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

        self.arc_path_input.insert(0, self.destination)
        if self.destination:
            print(f"Archive Destination = {self.destination}")
        else:
            print("No Destination Selected")
        return self.destination

    def archive_folder(self):
        try:
            self.zip_name = self.name_input.get()
            self.archive_type = self.type_drop_down.get()
            shutil.make_archive((self.destination+"/"+self.zip_name),self.archive_type,self.folder_path)
            print(f"Archived Successfully✅ at {self.destination + "/" + self.zip_name}")
            self.path_input.delete(0,tk.END)
            self.arc_path_input.delete(0,tk.END)
            self.name_input.delete(0,tk.END)
        except:
            print("Archive Failed😥")

App()