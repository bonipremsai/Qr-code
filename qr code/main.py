import qrcode, PIL
from PIL import ImageTk
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

def createQr(*args):
    data = text_entry.get()
     
    if data:
        img = qrcode.make(data)
        resized_img = img.resize((280,250))
        tkimage = ImageTk.PhotoImage(resized_img)
        qr_canvas.delete("all")
        qr_canvas.create_image(0,0,anchor=tk.NW,image=tkimage)
        qr_canvas.image = tkimage
    else:
        messagebox.showinfo("Error","Enter Some Data First")


def saveQr(*args):
    data = text_entry.get()
     
    if data:
        img = qrcode.make(data)
        resized_img = img.resize((280,250))
        path = filedialog.asksaveasfilename(defaultextension=".png")
        if path:
            resized_img.save(path)
            messagebox.showinfo("Sucess","QR Code is Saved")
    else:
        messagebox.showinfo("Error","Enter Some Data First")


root = tk.Tk()
root.title("QR code Generator")
root.geometry("300x380")
root.config(bg="white")
root.resizable(0, 0)

frame1 = tk.Frame(root, bd=2,relief=tk.RAISED)
frame1.place(x=10,y=0,width=280,height=250)

frame2 = tk.Frame(root, bd=2,relief=tk.SUNKEN)
frame2 .place(x=10,y=260,width=280,height=100)

cover_img = tk.PhotoImage(file="scan.png")

qr_canvas = tk.Canvas(frame1)
qr_canvas.create_image(0,0,anchor=tk.NW,image=cover_img)
qr_canvas.bind("<Double-1>",saveQr)
qr_canvas.pack(fill=tk.BOTH)


text_entry = ttk.Entry(frame2,width=26,font=("Sitka Small", 11),justify=tk.CENTER)
text_entry.bind("<Return>",createQr)
text_entry.place(x=5,y=5)

btn_1 = ttk.Button(frame2,text="Create",width=10,command=createQr)
btn_1.place(x=25,y=50)

btn_2 = ttk.Button(frame2,text="Save",width=10,command=saveQr)
btn_2.place(x=100,y=50)

btn_3 = ttk.Button(frame2,text="Exit",width=10,command=root.quit)
btn_3.place(x=175,y=50)


root.mainloop()
