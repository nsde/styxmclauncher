import os
import tkinter as tk

fgColor = "white"
bgColor = "#212121"
menuColor = "#091db7"
activeColor = "#3f3f3f"
reliefStyle = "flat"

win = tk.Tk()
win.title("Styx Minecraft Launcher")
win.config(bg=bgColor)

print(os.getenv("JAVA.HOME"))

def start():
    pass

titleTxt = tk.Label(win, text="Styx MCL", font=('Calibri Light', 50), bg=bgColor, fg=fgColor)
titleTxt.pack()

startBtn = tk.Button(win, text="Start", command=start, font=('Calibri Light', 20), bg=bgColor, fg=fgColor, relief=reliefStyle, activebackground=activeColor)
startBtn.pack()

win.mainloop()