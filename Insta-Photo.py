from tkinter import *
from PIL import Image, ImageTk
import instaloader

root = Tk()
root.geometry("500x300")
root.configure(background='#000000')
root.resizable(False, False)
root.title("InstaPhoto")

def download_data():
    url = str(link.get())
    instaloader.Instaloader().download_profile(url, profile_pic_only=False)
    Label(root,text="Download Completed",font=("Arial 15"),fg="white",bg="green").place(x=120,y=500)
    Label(root,text="Check Your Current Folder for the downloads",font=("Arial 15"),fg="white",bg="green").place(x=40,y=540)

link=StringVar()

Label(root,text="Username",bg="#000000",fg="white",font=30).pack(padx=25,pady=25)
link_entry = Entry(root,textvariable=link,width=25,font=18,bd=1).pack(padx=5,pady=5)

Button(root,text="Scrap Data",font=('Arial',20,"bold"),bg="purple",padx=2,pady=2,command=download_data).pack(padx=5,pady=50)
Label(root,text="Set Username and Scrap Datas",font=14,fg="white",bg="black").place(x=100,y=250)

root.mainloop()