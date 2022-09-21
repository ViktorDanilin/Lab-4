# вариант 4
from playsound import playsound  # добавить музыку на фон
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Tom Clancy’s Rainbow Six Siege")
root.geometry("1024x576")

bg = ImageTk.PhotoImage(Image.open("img/nws_rainbowsixsiege.jpg"))  # добавить гифку
canvas1 = Canvas(root, width=1024, height=576)
canvas1.pack(fill="both", expand=True)
canvas1.create_image(0, 0, image=bg, anchor="nw")

def clicked():
    key = 'key'  # добавить генерацию ключа
    canvas1.itemconfig(label1_canvas, text=key)

btn = Button(root, text="Генерировать ключ", command=clicked)

button1_canvas = canvas1.create_window(708, 384, anchor="nw", window=btn)
label1_canvas = canvas1.create_text(768, 350, text="Нажмите для генерации ключа", fill="black", font=('Helvetica 15 bold'))


root.mainloop()
