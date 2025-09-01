import tkinter as tk 
def press(num):
    entry_val.set(entry_val.get()+str(num))

def calculate():
    try:
        entry_val.set(str(eval(entry_val.get())))
    except:
        entry_val.set("error")
    
def clear():
    entry_val.set("")

def backspace():
    entry_val.set(entry_val.get()[:-1])



root=tk.Tk()
root.title("Calculator")
root.geometry("355x500")

entry_val=tk.StringVar()
Buttons={
    ('7','8','9','c'),
    ('4','5','6','='),
    ('1','2','3','0'),
    ('/','*','+','-')
}

entry=tk.Entry(root, textvariable=entry_val, font=('Arial',20), justify='right',bd=8,relief='sunken')
entry.grid(row=0,column=0,columnspan=4, ipadx=9,ipady=9)

for i, row in enumerate(Buttons):
    for j, char in enumerate(row):
        if char=="=":
            action=calculate
        elif char=="c":
            action=clear
        else:
            action=lambda x=char: press(x)
        tk.Button(root, text=char, font=('Arial',20), command=action,width=5,height=2).grid(row=i+1,column=j)
    
tk.Button(root, text="del", width=5, height=2, font=('Arial',20), command=backspace).grid(row=5,column=0,columnspan=2)

root.mainloop()