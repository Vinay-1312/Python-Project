
from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry("190x150")
root.title("Miles to KM")

def retrieve_input():
    inputValue=float(T.get("1.0","end-1c"))
    T1.delete(1.0,"end")
    T1.insert(1.0, inputValue* 1.609)
    
    

frm = ttk.Frame(root,padding = 20)
frm.pack(expand=1, fill=BOTH)



T = Text(root,width = 7,height = 1)
T.place(x=30,y=20)
ttk.Label(root, text="Miles",font = (10)).place(x=100, y=20)
#T.grid()
ttk.Label(root, text="Is equal to",font = (10)).place(x=10,y=50)
T1 = Text(root,width = 7,height = 1)
T1.place(x=85,y=50)
ttk.Label(root, text="km",font = (10)).place(x=150,y=50)
ttk.Button(frm, text="Calculate", command= lambda: retrieve_input()).place(x=-20, y=70)
ttk.Button(frm, text="Quit", command= root.destroy).place(x=60, y=70)
root.mainloop()