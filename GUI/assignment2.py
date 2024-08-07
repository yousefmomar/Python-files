from tkinter import *

def convert():
    t1.delete(0.0,END)
    g=round(float(mass.get())*1000,2)
    t1.insert(END,str(g)+" gm")

    t2.delete(0.0,END)
    pound=round(float(mass.get())*2.20462,4)
    t2.insert(END,str(pound)+" lbs")

    t3.delete(0.0,END)
    ounce=round(float(mass.get())*35.274,3)
    t3.insert(END,str(ounce)+" oz")

wind=Tk()
wind.title("Mass Convertor")
mass=StringVar()

b1=Button(wind,text="convert",command=convert)
e1=Entry(wind,textvariable=mass,bg="red",borderwidth=2.5)
t1=Text(wind,height=1,width=20)
t2=Text(wind,height=1,width=20)
t3=Text(wind,height=1,width=20)
l1=Label(wind,text="Enter Mass to convert")
l2=Label(wind,text="Kg")

b1.configure(bg="black",fg="blue")

l1.grid(row=0,column=1)
e1.grid(row=1,column=1)
l2.grid(row=1,column=2)
b1.grid(row=1,column=0)
t1.grid(row=3)
t2.grid(row=3,column=1)
t3.grid(row=3,column=2)

wind.mainloop()
