import tkinter as tk
from turtle import bgcolor
from  controller import *

if __name__ == '__main__':
    root = tk.Tk()
    root.title("KUMBO SAVINGS")
    root.geometry("800x600")
    root.config(bg="#DCDCDC")
    
    
    app = Controller(root)
    root.mainloop()
