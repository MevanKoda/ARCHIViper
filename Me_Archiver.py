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
        self.archive_file = ""
        self.extract_destination = ""

        self.root = tk.CTk()
        self.root.title("Me Archiver")
        self.root.geometry("500x500")

        # =======================
        # Title section
        # =======================

        self.label = tk.CTkLabel(self.root,text="ME ARCHIVER 3.0", font=('CTkHeadingFont',30),text_color="lightblue")
        self.label.pack(padx=20, pady=20)

        self.slogan = tk.CTkLabel(self.root, text="Simple & Light", font=('CTkCaptionFont', 15))
        self.slogan.pack()

        self.menu_frame = tk.CTkFrame(self.root,fg_color="transparent")
        self.menu_frame.pack(pady=10)


        # =======================
        # option section menu
        # =======================

        self.archive_option_btn = tk.CTkButton(self.menu_frame,text="Archive",font=("CTkHeadingFont",15),fg_color="green",hover_color="darkgreen",command=self.archive_menu)
        self.archive_option_btn.grid(row=0,column=0,padx=5)
        self.extract_option_btn = tk.CTkButton(self.menu_frame, text="Extract", font=("CTkHeadingFont", 15),fg_color="yellow",text_color="black",hover_color="orange",command=self.extract_menu)
        self.extract_option_btn.grid(row=0, column=1,padx=5)

        # =======================
        # archive option section
        # =======================
        self.archive_section= tk.CTkScrollableFrame(self.root,fg_color="transparent",height=450, width=600)
        self.archive_section.pack(expand=True)
        self.frame1 = tk.CTkFrame(self.archive_section)
        self.frame1.pack(padx=40,pady=(10,0))
        #initialize grid
        self.frame1.grid_columnconfigure(0, weight=1)
        self.frame1.grid_columnconfigure(1, weight=1)

        self.frame1.grid_rowconfigure(0, weight=1)
        self.frame1.grid_rowconfigure(1, weight=1)


        #Enter File Path
        self.file_label = tk.CTkLabel(self.frame1, text="Enter File Path", font=('CTkHeadingFont', 15),anchor="w")
        self.file_label.grid(row=0,column=0,padx=20, pady=(10,0),sticky="ew")
        self.arc_path_input = tk.CTkEntry(self.frame1, font=('TkTextFont',10),width =350)
        self.arc_path_input.grid(row=1, column=0,padx=20, pady=10)
        self.browser_btn = tk.CTkButton(self.frame1, text="Browse", font=("TkTextFont",10), command= self.select_folder)
        self.browser_btn.grid(row=1,column=1,padx=20)

        self.frame2 = tk.CTkFrame(self.archive_section)
        self.frame2.pack(pady=(10, 10))
        # initialize grid
        self.frame2.grid_columnconfigure(0, weight=1)
        self.frame2.grid_columnconfigure(1, weight=1)
        self.frame2.grid_columnconfigure(2, weight=1)

        self.frame2.grid_rowconfigure(0, weight=1)
        self.frame2.grid_rowconfigure(1, weight=1)
        #Zip Name
        self.name_label = tk.CTkLabel(self.frame2, text="Enter name", font=('CTkHeadingFont',15),anchor="w")
        self.name_label.grid(row=0,column=0,padx=15, pady=(10,0),sticky="ew")
        self.name_input = tk.CTkEntry(self.frame2,font=('CTkTextFont',10),width= 200)
        self.name_input.grid(row=1,column=0,padx=10,pady=10)
        self.type_label = tk.CTkLabel(self.frame2, text="Type",font=('CTkHeadingFont',15),anchor="w")
        self.type_label.grid(row=0,column=1,sticky="ew",padx=20,pady=(10,0))
        self.type_drop_down= tk.CTkOptionMenu(self.frame2, values=["zip","tar","gztar","bztar","xztar","zstdtar"])
        self.type_drop_down.grid(row=1,column=1,padx=15,pady=10)


        self.frame3 = tk.CTkFrame(self.archive_section)
        self.frame3.pack(padx=40, pady=(10, 0))
        # initialize grid
        self.frame3.grid_columnconfigure(0, weight=1)
        self.frame3.grid_columnconfigure(1, weight=1)

        self.frame3.grid_rowconfigure(0, weight=1)
        self.frame3.grid_rowconfigure(1, weight=1)
        #Archive Destination
        self.archive_label = tk.CTkLabel(self.frame3, text="Enter Destination", font=('CTkHeadingFont',15),anchor="w")
        self.archive_label.grid(row=0,column=0,padx=20, pady=(10,0), sticky="ew")
        self.arc_dest_input = tk.CTkEntry(self.frame3, font=('TkTextFont',10),width=350)
        self.arc_dest_input.grid(row=1,column=0,padx=20)
        self.browse_btn = tk.CTkButton(self.frame3,text="Browse",font=("TkTextFont",10), command= self.select_dest)
        self.browse_btn.grid(row=1,column=1,padx=20, pady=10)

        self.archive_btn = tk.CTkButton(self.archive_section, text="Archive", font=("CTkHeadingFont",15),command=self.archive_folder,fg_color="green", text_color="white", hover_color="darkgreen",width=100,height=35)
        self.archive_btn.pack(padx=20,pady=20)



        # =======================
        # extract option section
        # =======================

        self.extract_section = tk.CTkScrollableFrame(
            self.root,
            fg_color="transparent",
            height=450,
            width=600
        )
        self.extract_section.pack(expand=True)

        # ---------- Frame 1 (Select File) ----------
        self.ex_frame1 = tk.CTkFrame(self.extract_section)
        self.ex_frame1.pack(padx=40, pady=(10, 0))

        # grid config
        self.ex_frame1.grid_columnconfigure(0, weight=1)
        self.ex_frame1.grid_columnconfigure(1, weight=1)

        self.file_label = tk.CTkLabel(
            self.ex_frame1,
            text="Select File",
            font=('CTkHeadingFont', 15),
            anchor="w"
        )
        self.file_label.grid(row=0, column=0, padx=20, pady=(10, 0), sticky="ew")

        self.ext_path_input = tk.CTkEntry(
            self.ex_frame1,
            font=('TkTextFont', 10),
            width=350
        )
        self.ext_path_input.grid(row=1, column=0, padx=20, pady=10)

        self.browser_btn = tk.CTkButton(
            self.ex_frame1,
            text="Browse",
            font=("TkTextFont", 10),
            command=self.select_file
        )
        self.browser_btn.grid(row=1, column=1, padx=20)

        # ---------- Frame 2 (Destination) ----------
        self.ext_frame2 = tk.CTkFrame(self.extract_section)
        self.ext_frame2.pack(padx=40, pady=(10, 0))

        # grid config
        self.ext_frame2.grid_columnconfigure(0, weight=1)
        self.ext_frame2.grid_columnconfigure(1, weight=1)

        self.extract_label = tk.CTkLabel(
            self.ext_frame2,
            text="Enter Destination",
            font=('CTkHeadingFont', 15),
            anchor="w"
        )
        self.extract_label.grid(row=0, column=0, padx=20, pady=(10, 0), sticky="ew")

        self.ext_path_input = tk.CTkEntry(
            self.ext_frame2,
            font=('TkTextFont', 10),
            width=350
        )
        self.ext_path_input.grid(row=1, column=0, padx=20, pady=10)

        self.browse_btn = tk.CTkButton(
            self.ext_frame2,
            text="Browse",
            font=("TkTextFont", 10),
            command=self.extract_dest
        )
        self.browse_btn.grid(row=1, column=1, padx=20)

        # ---------- Extract Button ----------
        self.extract_btn = tk.CTkButton(
            self.extract_section,
            text="Extract",
            font=("CTkHeadingFont", 15),
            command=self.extract,
            fg_color="yellow",
            text_color="black",
            hover_color="orange",
            width=100,
            height=35
        )
        self.extract_btn.pack(padx=20, pady=20)

        self.root.mainloop()

    def select_folder(self):
        self.folder_path = filedialog.askdirectory()

        self.arc_path_input.insert(0,self.folder_path)
        if self.folder_path:
            print(f"Folder Path={self.folder_path}")
        else:
            print("No Folder Selected")
        return self.folder_path

    def select_dest(self):
        self.destination = filedialog.askdirectory()

        self.arc_dest_input.insert(0, self.destination)
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

    def archive_menu(self):
        print("Archive Menu")
        self.extract_section.pack_forget()
        self.archive_section.pack()


    def extract_menu(self):
        print("Extract Menu")
        self.extract_section.pack()
        self.archive_section.pack_forget()

    def select_file(self):
        self.archive_file = filedialog.askopenfilename(title="Open a file")
        if self.archive_file:
            print(f"Selected file :- {self.archive_file}")
        return self.archive_file

    def extract_dest(self):
        self.extract_destination= filedialog.askdirectory()

        if not self.extract_destination:
            print("No extract destination selected!!!")
    def extract(self):
        try:
            shutil.unpack_archive(self.archive_file, self.extract_destination)
            print(f"Extract Successfully✅ at {self.extract_destination}")
        except:
            print("Extract Failed😥")

App()