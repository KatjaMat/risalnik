from tkinter import *
import math
class Risanje:
    def __init__(self,master):
        # ustvarimo platno
        self.platno=Canvas(master,width=500,height=500)
        self.platno.pack(side=RIGHT) #z pack umestiš na platno
        self.frame = Frame(master)
        self.frame.pack(side=LEFT, fill=Y)
        self.slika = list()
        self.platno.bind("<Button-1>", self.klik)
        self.platno.bind("<B1-Motion>",self.premik)
        self.zadnjiKlik=self.klik
        self.x=0
        self.y=0



        menu =Menu(master)
        menuNarisi=Menu(menu, tearoff=0)
        menuPobrisi=Menu(menu, tearoff=0)
        menuPobrisiZadnji=Menu(menu,tearoff=0)

        okno.config(menu=menu)
        menu.add_cascade(label='Nariši', menu=menuNarisi)
        menu.add_cascade(label='Pobriši', menu=menuPobrisi)
        menu.add_command(label='Končaj', command=master.destroy)


        menuNarisi.add_command(label='Piramida', command=self.piramida)
        menuNarisi.add_command(label='Tarca', command=self.tarca)
        menuNarisi.add_command(label='Trikotnik', command=self.trikotnik)
        menuNarisi.add_command(label='Torta', command=self.torta)

        menuPobrisi.add_command(label='Pobriši vse', command=self.pobrisi)
        menuPobrisi.add_command(label = 'Pobriši zadnjega', command=self.pobrisiZadnji)

        self.label1=Label(self.frame, text='Parametri:')
        self.label1.grid(row=0, column=0,sticky='w')
        self.label2=Label(self.frame, text='Položaj x:')
        self.label2.grid(row=1, column=0,sticky='w')
        self.label3 = Label(self.frame, text='Položaj y:')
        self.label3.grid(row=2, column=0,sticky='w')
        self.label4 = Label(self.frame, text='Velikost:')
        self.label4.grid(row=3, column=0, sticky='w')

        self.entry1=Entry(self.frame)
        self.entry1.grid(row=0, column=1)
        self.entry2 = Entry(self.frame)
        self.entry2.grid(row=1, column=1)
        self.entry3 = Entry(self.frame)
        self.entry3.grid(row=2, column=1)
        self.entry4 = Entry(self.frame)
        self.entry4.grid(row=3, column=1)


    def klik(self,event):
        self.x=event.x
        self.y=event.y
        sezID = self.platno.find_overlapping(event.x,event.y,event.x+1,event.y+1)
        if len(sezID) == 0: return
        else:
            zadnji=sezID[-1]
            for sez in self.slika:
                if zadnji in sez: self.zadnjiKlik=sez

    def premik(self,event):
        for el in self.zadnjiKlik:
            self.platno.move(el,event.x-self.x,event.y-self.y)
        self.x=event.x
        self.y=event.y

    def piramida(self):
        p1=int(self.entry1.get() or 8)
        p2=int(self.entry2.get() or 400 )
        p3=int(self.entry3.get() or 50)
        p4=int(self.entry4.get() or 20)
        sez = piramida(self.platno,p1,p2,p3,p4)
        self.slika.append(sez)

    def tarca(self):
        p1 = int(self.entry1.get() or 8)
        p2 = int(self.entry2.get() or 400)
        p3 = int(self.entry3.get() or 50)
        p4 = int(self.entry4.get() or 20)
        sez = tarca(self.platno, p1, p2, p3, p4)
        self.slika.append(sez)

    def trikotnik(self):
        p1 = int(self.entry1.get() or 4)
        p2 = int(self.entry2.get() or 200)
        p3 = int(self.entry3.get() or 100)
        p4 = int(self.entry4.get() or 200)
        sez = trikotnik(self.platno, p1, p2, p3, p4)
        self.slika.append(sez)

    def torta(self):
        p1 = (eval('['+self.entry1.get()+']' or [15, 20,20,20, 15]))
        p2 = int(self.entry2.get() or 400)
        p3 = int(self.entry3.get() or 50)
        p4 = int(self.entry4.get() or 20)
        sez = torta(self.platno, p1, p2, p3, p4)
        self.slika.append(sez)

    def pobrisi(self):
        self.platno.delete('all')
        self.slika=[]

    def pobrisiZadnji(self):
        if self.slika == []:
            return
        else:
            for el in self.slika[-1]:
                self.platno.delete(el)
        self.slika.pop()

def piramida(platno, n, x, y, d):
    s = []
    for i in range(n):
        id = platno.create_rectangle(x-(i+1)*d,y+i*d,x+(i+1)*d,y+(i-1)*d,fill="orange",outline="")
        s.append(id)
    return s

def tarca(platno,n,x,y,d):
    s = []
    for i in range(n,0,-1):
        barva="white"if i%2== 0 else "black"
        id = platno.create_oval(x-i*d, y-i*d, x+i*d, y+i*d, fill=barva, outline="black")
        s.append(id)
    return s

def trikotnik(platno,n,x,y,d):
    s = []
    if n==1:
        id = platno.create_polygon(x,y,x+d,y,x+d/2,y-d*math.sqrt(3)/2, fill="",outline="black")
        return [id]
    else:
        sez1 = trikotnik(platno,n-1,x,y,d/2)
        sez2 = trikotnik(platno,n-1,x+d/2,y,d/2)
        sez3 = trikotnik(platno,n-1,x+d/4,y-d*math.sqrt(3)/4,d/2)
        return(sez1+sez2+sez3)

barve=["blue","red","black","orange"]
def torta(platno,podatki,x,y,r):
    zacetni=0
    for i in range(len(podatki)):
        koncni = podatki[i] / sum(podatki) * 360
        platno.create_arc(x+r,y+r,x-r,y-r,start=zacetni,extent=koncni,style=PIESLICE,fill=barve[i],outline="black")
        zacetni+=koncni


okno = Tk()
app = Risanje(okno)
okno.mainloop()

