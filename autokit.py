from tkinter import *
import subprocess

def run():
    subprocess.run(["python", "my-code.py"])

def run2():
    subprocess.run(["python", "auto-inventory3.py"])

def run3():
    f = open("electricity.csv", "a")
    subprocess.call(["sudo", "powermetrics", "-n", "1", "|", "prep", "CPUs+GT+SA" ], stdout=f)

def run4():
    f = open("uptime.csv", "a")
    subprocess.call(["uptime", ">>", "uptime.csv"], stdout=f)

root = Tk()
Button(root, text="Search KIT Website", command=run).pack()
Button(root, text="Automation3", command=run2).pack()
Button(root, text="Electricity Data", command=run3).pack()
Button(root, text="Finish work", command=run4).pack()
root.mainloop()