from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title("Entrance")
root.geometry("500x500")
root.resizable(False,False);

id = StringVar()
def getID():
    Label(root, text="사번을 입력하시오:").pack(side = LEFT)
    Entry(root, textvariable = id, width = 20).pack(sid = RIGHT)
def clickMe():
    messagebox.showinfo("ID", id)

getid = getID()
action=ttk.Button(root, text="Click Me", command=clickMe)
action.pack(sid = TOP)

root.mainloop() #윈도우 종료될때 까지 실행