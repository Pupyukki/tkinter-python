from tkinter import *
from tkinter import ttk
root=Tk()
root.config(bg="lightblue")
root.title("Temperature conversion")
root.geometry("800x400")
def calculate():
    option=choice.get()
    temp=int(temperature.get())
    if option=="Farenheit to Celsius":  
        result=(temp-32)*5/9
        label_result["text"]=str(result)+"°C"
    else:
        result=(temp*9/5)+32
        label_result["text"]=str(result)+"°F"
label=Label(root,text="Temperature conversion",font=("Lucida Sans Unicode",25,"bold","italic"),fg="darkblue",bg="lightblue")
label.place(relx=0.5,rely=0.1,anchor=CENTER)
label_temp=Label(root,text="Enter the temperature u want to convert: ",font=("Tahoma",18),fg="darkblue",bg="lightblue")
label_temp.place(relx=0.5,rely=0.25,anchor=CENTER)
temperature=Entry(root,font=("Calibri",13),width=30)
temperature.place(relx=0.5,rely=0.45,anchor=CENTER)
type=["Celsius to Farhenheit","Farenheit to Celsius"]
choice=ttk.Combobox(root,values=type,font=("Tahoma",15),width=30)
choice.set("Select your option")
choice.place(relx=0.5,rely=0.6,anchor=CENTER)
conversion_type=choice.get()
btn=Button(root,text="convert",font=("Tahoma",15),padx=10,pady=10,command=calculate,fg="white",bg="darkblue",relief=FLAT)
btn.place(relx=0.5,rely=0.75,anchor=CENTER)
label_result=Label(root,font=("Lucida Sans Unicode",20),fg="darkblue",bg="lightblue")
label_result.place(relx=0.5,rely=0.9,anchor=CENTER)
root.mainloop()