from tkinter import *
from math import *


class Krozenje():
    def __init__(self,master):
        self.canvas = Canvas(master, width=600, height=600, background="black")
        self.canvas.pack(side=RIGHT)
        self.sonce=PhotoImage(file="sonce.ppm")
        self.luna = PhotoImage(file="luna.ppm")
        self.zemlja = PhotoImage(file="zemlja.ppm")
        self.sonceID = self.canvas.create_image(300,300, image=self.sonce)
        self.lunaID = self.canvas.create_image(500, 300, image=self.luna)
        self.zemljaID = self.canvas.create_image(550, 300, image=self.zemlja)
        self.kotZemlje=0
        self.kotLune=0
        self.pozicijaZemljex=500
        self.pozicijaZemljey=300
        self.premik()

    def premik(self):
        self.kotZemlje +=1
        dx = 300 + 200*cos(radians(self.kotZemlje))
        dy = 300 + 200*sin(radians(self.kotZemlje))
        self.canvas.coords(self.zemljaID,dx,dy)

        self.canvas.after(30,self.premik)








okno = Tk()
app = Krozenje(okno)
okno.mainloop()