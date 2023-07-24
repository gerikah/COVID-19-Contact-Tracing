import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk
from tkinter import filedialog
import tkinter.font as tkfont
from backend import COVID_Contacts_Informations

class COVID_Contacts_Information_GUI:
    def __init__(self) -> None:
        
        
root = tk.Tk()
gui = COVID_Contacts_Information_GUI(root)
root.mainloop()