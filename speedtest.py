from tkinter import *
import speedtest
root=Tk()
root.config(bg="lightpink")
root.title("Internet speed test")
root.geometry("500x300")
label=Label(root,text="Internet speed check",font=("Lucida Sans Unicode",20,"bold","italic"),fg="red",bg="lightpink")
label.place(relx=0.5,rely=0.1,anchor=CENTER)
label_download=Label(root,text="Download speed 🠇 ",font=("Segio Print",18,"bold"),fg="black",bg="lightpink")
label_download.place(relx=0.25,rely=0.5,anchor=CENTER)
label_upload=Label(root,text="Upload speed 🠅 ",font=("Segio Print",18,"bold"),fg="black",bg="lightpink")
label_upload.place(relx=0.75,rely=0.5,anchor=CENTER)
label_download_speed=Label(root,font=("Yu Gothic Light",14,"bold"),bg="lightpink")
label_download_speed.place(relx=0.25,rely=0.6,anchor=CENTER)
label_upload_speed=Label(root,font=("Yu Gothic Light",14,"bold"),bg="lightpink")
label_upload_speed.place(relx=0.75,rely=0.6,anchor=CENTER)
def speedCheck():
    st=speedtest.Speedtest()
    st.get_best_server()
    download_speed=round(st.download()/1000000,2)
    label_download_speed["text"]=str(download_speed)+"mbps"
    upload_speed=round(st.upload()/1000000,2)
    label_upload_speed["text"]=str(upload_speed)+"mbps"

btn=Button(root,text="Check speed",command=speedCheck,fg="white",bg="lightpink",relief=FLAT,padx=15,pady=8,font=("Lucida Sans Unicode",10))
btn.place(relx=0.5,rely=0.3,anchor=CENTER)
root.mainloop()