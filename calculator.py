from tkinter import *
rt  = Tk()
rt.title("CALCULATOR")
rt.configure(bg = "black")
rt.geometry("500x690")
value = StringVar()
value.set("")
avalue = StringVar()
avalue.set("Ans :       ")
def varshini(event):
    text = event.widget.cget("text")
    current_text = value.get()
    
    if text == "=":
        try:
           avalue.set("Ans :      " + str(eval("".join(current_text.split(" ")))))
        except SyntaxError:
            avalue.set("SyntaxError")
            
    elif text == "c":
        value.set(" ")
        avalue.set("Ans :    ")
    elif text == "^":
        value.set(current_text+"**")
        
    elif text == "x":
        value.set(current_text[:len(current_text)-2])
    else:
         value.set(current_text + text)
        
sc = Entry(rt, textvar = value,font = ("backlight",30),fg = "white",bg = "black")
sc.pack(ipadx = 100,ipady = 18,pady = 0,padx = 65)
vc = Entry(rt, textvar = avalue,font = ("book script",25),fg = "gray",bg = "black")
vc.pack(ipadx = 100,pady = 0,padx = 65)
f = Frame(rt,bg = "black")
b = Button(f,text = "c",font = ("ariel",30,"bold"),fg = "gray",bg = "black")
b.bind("<Button-1>",varshini)
b.pack(side = LEFT,padx = 19,pady = 12)
b = Button(f,text = "x",font = ("ariel",30,"bold"),fg = "gray",bg = "black")
b.pack(side = LEFT,padx = 19,pady = 12)
b.bind("<Button-1>",varshini)
b = Button(f,text = "/",font = ("ariel",30),fg = "gray",bg = "black")
b.pack(side = LEFT,padx = 19,pady = 12)
b.bind("<Button-1>",varshini)

b = Button(f,text = "^",font = ("ariel",30,"bold"),fg = "gray",bg = "black")
b.pack(side =LEFT ,padx = 18,pady = 12)
b.bind("<Button-1>",varshini)
b.pack()
f.pack()
f = Frame(rt,bg = "black")
b = Button(f,text = "9",font = ("ariel",30,"bold"),fg = "blue",bg = "black")
b.pack(side = LEFT,padx = 18,pady = 12)
b.bind("<Button-1>",varshini)
b = Button(f,text = "8",font = ("ariel",30,"bold"),fg = "blue",bg = "black")
b.pack(side = LEFT,padx = 18,pady = 12)
b.bind("<Button-1>",varshini)
b = Button(f,text = "7",font = ("ariel",30,"bold"),fg = "blue",bg = "black")
b.pack(side = LEFT,padx = 18,pady = 12)
b.bind("<Button-1>",varshini)
b = Button(f,text = "*",font = ("ariel",30,"bold"),fg = "gray",bg = "black")
b.pack(side = LEFT,padx = 18,pady = 12)
b.bind("<Button-1>",varshini)
b.pack()
f.pack()
f = Frame(rt,bg = "black")
b = Button(f,text = "6",font = ("ariel",30,"bold"),fg = "blue",bg = "black")
b.pack(side = LEFT,padx = 18,pady = 12)
b.bind("<Button-1>",varshini)
b = Button(f,text = "5",font = ("ariel",30,"bold"),fg = "blue",bg = "black")
b.pack(side = LEFT,padx = 17,pady = 12)
b.bind("<Button-1>",varshini)
b = Button(f,text = "4",font = ("ariel",30,"bold"),fg = "blue",bg = "black")
b.pack(side = LEFT,padx = 17,pady = 12)
b.bind("<Button-1>",varshini)
b = Button(f,text = "+",font = ("ariel",30,"bold"),fg = "gray",bg = "black")
b.pack(side = LEFT,padx = 16,pady = 12)
b.bind("<Button-1>",varshini)

b.pack()
f.pack()
f = Frame(rt,bg = "black")   
b = Button(f,text = "3",font = ("ariel",30,"bold"),fg = "blue",bg = "black")
b.pack(side = LEFT,padx = 18,pady = 12)
b.bind("<Button-1>",varshini)
b = Button(f,text = "2",font = ("ariel",30,"bold"),fg = "blue",bg = "black")
b.pack(side = LEFT,padx = 19,pady = 12)
b.bind("<Button-1>",varshini)
b = Button(f,text = "1",font = ("ariel",30,"bold"),fg = "blue",bg = "black")
b.pack(side = LEFT,padx = 19,pady = 12)
b.bind("<Button-1>",varshini)
b = Button(f,text = "-",font = ("ariel",30,"bold"),fg = "gray",bg = "black")
b.pack(side =LEFT ,padx = 18,pady = 12)
b.bind("<Button-1>",varshini)
b.pack()
f.pack()
f = Frame(rt,bg = "black")
b = Button(f,text = "%",font = ("ariel",30,"bold"),fg = "gray",bg = "black")
b.pack(side = LEFT,padx = 16,pady = 12)
b.bind("<Button-1>",varshini)
b = Button(f,text = "0",font = ("ariel",30,"bold"),fg = "blue",bg = "black")
b.pack(side = LEFT,padx = 18,pady = 12)
b.bind("<Button-1>",varshini)
b = Button(f,text = ".",font = ("ariel",30,"bold"),fg = "gray",bg = "black")
b.pack(side = LEFT,padx = 18,pady = 12)
b.bind("<Button-1>",varshini)
b = Button(f,text = "=",font = ("ariel",30,"bold"),fg = "gray",bg = "black")
b.pack(side =LEFT ,padx = 17,pady = 12)
b.bind("<Button-1>",varshini)
b.pack()
f.pack()
rt.mainloop()



