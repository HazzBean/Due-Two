import tkinter as tk
from tkinter import messagebox
import datetime

def show_time():
    now = datetime.datetime.now()
    messagebox.showinfo("Current Time", now.strftime("%Y-%m-%d %H:%M:%S"))

show_time()

