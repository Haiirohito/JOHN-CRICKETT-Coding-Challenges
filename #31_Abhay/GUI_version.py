import qrcode,PIL
from PIL import ImageTk
import tkinter as tk
from tkinter import ttk,messagebox,filedialog

def createqr(*args):
    data = text_entry.get()
    if data:
        img = qrcode.make(data) #generate QRcode
        res_img = img.resize((500,500))
        tkimage = ImageTk.PhotoImage(res_img)
        qr_canvas.delete('all')
        qr_canvas.create_image(0,0,anchor=tk.NW, image=tkimage)
        qr_canvas.image = tkimage
        
    else:
        messagebox.showwarning("warning,'Enter data first")
        
root = tk.Tk()
root.title("QR CODE GENERATOR")
root.geometry("500x500")
root.config(bg = 'white')
root.resizable(0, 0)
root.attributes('-fullscreen', True)


frame1 = tk.Frame(root,bd=2, relief=tk.RAISED)
frame1.place(x=500,y=5,width=500,height=500)

frame2 = tk.Frame(root,bd=2,relief=tk.SUNKEN)
frame2.place(x=575,y=550,width=350,height=300)

qr_canvas = tk.Canvas(frame1)
qr_canvas.create_image(0,0,anchor=tk.NW)
qr_canvas.pack(fill=tk.BOTH,expand=True)

text_entry = ttk.Entry(frame2,width=26,font=("TIMES NEW ROMAN",11),justify=tk.CENTER)
text_entry.bind("<Return>",createqr)
text_entry.place(x=85,y=10)

btn1 = ttk.Button(frame2,text="Create",width = 20,command=createqr)
btn1.place(x=50,y=50)

btn2 = ttk.Button(frame2,text="Exit",width=20,command=root.quit)
btn2.place(x=200,y=50)

root.mainloop()