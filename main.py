# вариант 4
import pygame
from tkinter import *
from PIL import ImageTk, Image
import random

root = Tk()
pygame.mixer.init()
root.title("Tom Clancy’s Rainbow Six Siege")
root.geometry("1024x576")


def motion():
    canvas1.move(ball, 1, 0)
    if canvas1.coords(ball)[2] < 1024:
        root.after(10, motion)


def play():
    pygame.mixer.music.load("sound/rick.mp3")
    pygame.mixer.music.play(-1)


def clicked():
    # генерация ключа
    symbols = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7,
               'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13,
               'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19,
               'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26,
               '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
               '8': 8, '9': 9}

    interval = 40
    key = ''
    for i in range(4):
        summ = 1000
        block = ''
        while summ > interval:
            summ = 0
            block = ''
            for j in range(4):
                num = random.randint(1, 36)
                c = 0
                for k in symbols.keys():
                    c += 1
                    if c == num:
                        block += k
                        summ += symbols.get(k)

        if i != 3:
            key += block + ' - '
        else:
            key += block

    canvas1.itemconfig(label1_canvas, text=key)


bg = ImageTk.PhotoImage(Image.open("img/nws_rainbowsixsiege.jpg"))
canvas1 = Canvas(root, width=1024, height=576)
canvas1.pack(fill="both", expand=True)
canvas1.create_image(0, 0, image=bg, anchor="nw")

btn = Button(root, text="Генерировать ключ", command=clicked)

button1_canvas = canvas1.create_window(708, 384, anchor="nw", window=btn)
label1_canvas = canvas1.create_text(768, 350, text="Нажмите для генерации ключа", fill="black",
                                    font=('Helvetica 15 bold'))
ball = canvas1.create_oval(400, 500, 440, 540, fill='grey')

play()  # проигрывание музыки
motion()  # стремная, но анимация
root.mainloop()
