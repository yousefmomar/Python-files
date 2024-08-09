from tkinter import*

def prin(num):
    t1.insert(END,num)

def CLR():
    t1.delete(0.0,END)

def EQU():

    equation=t1.get(1.0,"end-1c")
    if '+' in equation:
        equation=list(map(float,equation.split('+')))
        res=equation[0]+equation[1]

    elif '*' in equation:
        equation=list(map(float,equation.split('*')))
        res=equation[0]*equation[1]

    elif '/' in equation:
        equation=list(map(float,equation.split('/')))
        res=equation[0]/equation[1]

    elif '^' in equation:
        equation=list(map(float,equation.split('^')))
        res=equation[0]**equation[1]

    elif '-' in equation :
        if '-' == equation[0]:
            equation=equation[1:]
            equation=list(map(float,equation.split('-')))
            res=(-1)*equation[0]-equation[1]
        else:
            equation=list(map(float,equation.split('-')))
            res=equation[0]-equation[1]
    
    t1.delete(0.0,END)
    t1.insert(END,res)

wind=Tk()
wind.title("Calculator")
wind.geometry("600x700")
wind.configure(background="grey")

t1=Text(wind,height=1,width=30,font=("Arial",35),borderwidth=2.5)
t1.grid(row=0,columnspan=4,sticky="nesw")

bCLR=Button(wind,text="CLEAR",padx=100,pady=50,font=("Arial",35),bg="black",fg="black",command=CLR)
bCLR.grid(row=5,columnspan=2,sticky="nesw")

bEqu=Button(wind,text="=",padx=100,pady=50,font=("Arial",35),bg="deepskyblue",fg="deepskyblue",command=EQU)
bEqu.grid(row=5,column=2,columnspan=2,sticky="nesw")



b0=Button(wind,text="0",padx=50,pady=50,font=("Arial",30),bg="black",fg="blue",command=lambda:prin(0))
b1=Button(wind,text="1",padx=50,pady=50,font=("Arial",30),bg="grey",fg="blue",command=lambda:prin(1))
b2=Button(wind,text="2",padx=50,pady=50,font=("Arial",30),bg="grey",fg="blue",command=lambda:prin(2))
b3=Button(wind,text="3",padx=50,pady=50,font=("Arial",30),bg="grey",fg="blue",command=lambda:prin(3))
b4=Button(wind,text="4",padx=50,pady=50,font=("Arial",30),bg="grey",fg="blue",command=lambda:prin(4))
b5=Button(wind,text="5",padx=50,pady=50,font=("Arial",30),bg="grey",fg="blue",command=lambda:prin(5))
b6=Button(wind,text="6",padx=50,pady=50,font=("Arial",30),bg="grey",fg="blue",command=lambda:prin(6))
b7=Button(wind,text="7",padx=50,pady=50,font=("Arial",30),bg="grey",fg="blue",command=lambda:prin(7))
b8=Button(wind,text="8",padx=50,pady=50,font=("Arial",30),bg="grey",fg="blue",command=lambda:prin(8))
b9=Button(wind,text="9",padx=50,pady=50,font=("Arial",30),bg="grey",fg="blue",command=lambda:prin(9))

bPlus=Button(wind,text="+",padx=50,pady=50,font=("Arial",30),bg="orange",fg="orange",command=lambda:prin("+"))
bMinus=Button(wind,text="-",padx=50,pady=50,font=("Arial",30),bg="orange",fg="orange",command=lambda:prin("-"))
bProduct=Button(wind,text="*",padx=50,pady=50,font=("Arial",30),bg="orange",fg="orange",command=lambda:prin("*"))
bDiv=Button(wind,text="/",padx=50,pady=50,font=("Arial",30),bg="orange",fg="orange",command=lambda:prin("/"))
bPower=Button(wind,text="pow",padx=50,pady=50,font=("Arial",25),bg="orange",fg="orange",command=lambda:prin("^"))
bDot=Button(wind,text=".",padx=50,pady=50,font=("Arial",30),bg="deepskyblue",fg="deepskyblue",command=lambda:prin("."))

b0.grid(row=4,column=1,sticky="nesw")
b1.grid(row=3,column=2,sticky="nesw")
b2.grid(row=3,column=1,sticky="nesw")
b3.grid(row=3,sticky="nesw")
b4.grid(row=2,column=2,sticky="nesw")
b5.grid(row=2,column=1,sticky="nesw")
b6.grid(row=2,sticky="nesw")
b7.grid(row=1,column=2,sticky="nesw")
b8.grid(row=1,column=1,sticky="nesw")
b9.grid(row=1,sticky="nesw")

bPlus.grid(row=1,column=3,sticky="nesw")
bMinus.grid(row=2,column=3,sticky="nesw")
bProduct.grid(row=3,column=3,sticky="nesw")
bDiv.grid(row=4,column=3,sticky="nesw")
bPower.grid(row=4,column=2,sticky="nesw")
bDot.grid(row=4,sticky="nesw")

wind.mainloop()
