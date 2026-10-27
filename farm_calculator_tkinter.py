from tkinter import *
root=Tk()
root.config(bg="white")
root.title("Farm calculator")
root.geometry("500x300")
Label1=Label(root,text="Farm Calculator",font=("Helvetica",30,"italic"),fg="black",bg="white")
Label1.pack()
Label2=Label(root,text="Please enter the width:",font=("Helvetica",20,"italic"),fg="black",bg="white")
Label2.pack()
width=Entry(root)
width.pack()
Label3=Label(root,text="Please enter the length:",font=("Helvetica",20,"italic"),fg="black",bg="white")
Label3.pack()
length=Entry(root)
length.pack()
Label4=Label(root,font=("Helvetica",25,"italic"),fg="red",bg="white")
Label4.pack()
Label5=Label(root,font=("Helvetica",25,"italic"),fg="red",bg="white")
Label5.pack()
def calculate():
    w=width.get()
    l=length.get()
    area=int(w)*int(l)
    Label4["text"]="Area is:"+str(area)+" sqm."
    perimeter=2*int(w)+int(l)*2
    Label5["text"]="Perimeter is:"+str(perimeter)+" m."

button=Button(root,text="calculate",command=calculate)
button.pack()
root.mainloop()