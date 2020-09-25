import os
import tkinter as tk

# Theme
fgColor = "white"
bgColor = "#212121"
menuColor = "#091db7"
activeColor = "#3f3f3f"
reliefStyle = "flat"

# Window
win = tk.Tk()
win.title("Styx Minecraft Launcher")
win.config(bg=bgColor)

# Check Java Path
os.system('where java > javapath.txt')
with open (os.getcwd() + '\\javapath.txt') as outlog:
    outdata = outlog.readlines()
javapath = outdata[0]

def start():
    pass

titleTxt = tk.Label(win, text="Styx MCL", font=('Calibri Light', 50), bg=bgColor, fg=fgColor)
titleTxt.pack()

startBtn = tk.Button(win, text="Start", command=start, font=('Calibri Light', 20), bg=bgColor, fg=fgColor, relief=reliefStyle, activebackground=activeColor)
startBtn.pack()

win.mainloop()