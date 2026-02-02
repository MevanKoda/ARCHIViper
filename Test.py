import shutil
import tkinter as tk
from tkinter import filedialog,messagebox


folder_path = ""
destination = ""
def selectFolder():
    global folder_path
    folder_path = filedialog.askdirectory()
    pathInput.insert(0,folder_path)
    if not folder_path:
        print("No Folder Selected")
    else:
        print(f"Folder Path = {folder_path}")
    return folder_path

def selectDest():
    global destination
    destination = filedialog.askdirectory()
    arcPathInput.insert(0,destination)
    if not destination:
        print("No Destination Selected")
    else:
        print(f"Archive Destination = {destination}")
    return destination

def archiveFolder():
    try:
        shutil.make_archive(destination, 'zip',folder_path)
        print(f"Archived Successfully✅ at {destination+"/MeArchive"}")
        pathInput.delete(0,tk.END)
        arcPathInput.delete(0,tk.END)
        messagebox.showinfo("Me Archiver", "Archived Successfully✅")
    except:
        print("Archive Failed😥")
        print(folder_path)

root = tk.Tk()
root.title("Me Archiver")
root.geometry("400x400")

Label = tk.Label(root, text="ME ARCHIVER 1.0", font=('Arial',20))
Label.pack(padx=20, pady=20)

introLabel = tk.Label(root, text="Simple & Lightweight", font=('Arial',10))
introLabel.pack(padx=20)

fileLabel=tk.Label(root, text="Enter File Path:", font=('Arial',12))
fileLabel.pack(padx=20)
pathInput= tk.Entry(root,font=('Arial', 10),width=40)
pathInput.pack(padx=20,pady=10,)
browseBtn = tk.Button(root, text="Browse", font=('Arial',10), command=selectFolder)
browseBtn.pack(padx=20)

archiveLabel = tk.Label(root, text="Enter Archive Destination:", font=('Arial',12))
archiveLabel.pack(padx=20)
arcPathInput= tk.Entry(root,font=('Arial', 10),width=40)
arcPathInput.pack(padx=20,pady=10,)
browseBtn = tk.Button(root, text="Browse", font=('Arial',10),command=selectDest)
browseBtn.pack(padx=20)
archiveBtn = tk.Button(root, text="Archive",font=('Arial', 10), command=archiveFolder)
archiveBtn.pack(padx=20,pady=20)

root.mainloop()
