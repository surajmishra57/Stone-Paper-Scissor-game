from tkinter import *
import random
from tkinter.font import Font
from tkinter import messagebox
n=0
win,drow,lose=0,0,0
def Chack(rand,n,frame):
    global win,drow,lose
    if rand==n:
        drow+=1
        messagebox.showinfo("GAMW DROW","GAME IS DROW")
        drowscore=Label(frame,text=drow,font=fonts,bg="blue")
        drowscore.place(x=350,y=10)
    if rand==1 and n==2 or rand==2 and n==3 or rand==3 and n==1:
        win+=1
        messagebox.showinfo("USER WIN","YOU WIN")
        winscore=Label(frame,text=win,font=fonts,bg="blue")
        winscore.place(x=90,y=10)
    if n==1 and rand==2 or n==2 and rand==3 or n==3 and rand==1:
        lose+=1
        messagebox.showinfo("COMPUTER WIN","YOU LOSE")
        losescre=Label(frame,text=lose,font=fonts,bg="blue")
        losescre.place(x=550,y=10)
    usercan=Canvas(frame,width=200,height=200,bg="orange")
    comcan=Canvas(frame,width=200,height=200,bg="orange")
    usercan.place(x=50,y=250)
    comcan.place(x=350,y=250)

def Stone(frame):
    usercan=Canvas(frame,width=200,height=200,bg="brown")
    usercan.place(x=50,y=250)
    stone=Label(usercan,text="STONE",font=fonts,bg="brown")
    stone.place(x=10,y=20)
    global n
    n=1
    Start(frame,n)

def Paper(frame):
    usercan=Canvas(frame,width=200,height=200,bg="lightblue")
    usercan.place(x=50,y=250)
    paper=Label(usercan,text="PAPER",font=fonts,bg="lightblue")
    paper.place(x=10,y=20)
    global n
    n=2
    Start(frame,n)
def Scissor(frame):
    usercan=Canvas(frame,width=200,height=200,bg="gray")
    usercan.place(x=50,y=250)
    scissor=Label(usercan,text="SCISSOR",font=fonts,bg="gray")
    scissor.place(x=10,y=20)
    global n
    n=3
    Start(frame,n)

def Start(frame,n):
   # if n==0:
    #     messagebox.showerror("Rock Paper Scissor","Pless choose one button first")
     #    return 0
    rand=random.randint(1,3)
    if rand==1:
        usercan=Canvas(frame,width=200,height=200,bg="brown")
        usercan.place(x=350,y=250)
        comstone=Label(usercan,text="STONE",font=fonts,bg="brown")
        comstone.place(x=10,y=20)
        Chack(rand,n,frame)
    if rand==2:
        usercan=Canvas(frame,width=200,height=200,bg="lightblue")
        usercan.place(x=350,y=250)
        compaper=Label(usercan,text="PAPER",font=fonts,bg="lightblue")
        compaper.place(x=10,y=20)
        Chack(rand,n,frame)
    if rand==3:
        usercan=Canvas(frame,width=200,height=200,bg="gray")
        usercan.place(x=350,y=250)
        comscissor=Label(usercan,text="SCISSOR",font=fonts,bg="gray")
        comscissor.place(x=10,y=20)
        Chack(rand,n,frame)
root=Tk()
root.title("ROCK PAPER SICSSOR GAME")
root.geometry("600x600+100+20")
frame=Frame(root,width=800,height=800,bg="blue")
frame.pack()
fontsize=Font(size=16)
fonts=Font(size=19)
label=Label(frame,text="USER",font=fontsize,bg="blue")
label.place(x=110,y=200)
labelcom=Label(frame,text="COMPUTER",font=fontsize,bg="blue")
labelcom.place(x=390,y=200)
WIN=Label(frame,text="WIN",font=fonts,bg="blue")
WIN.place(x=10,y=10)
LOSE=Label(frame,text="LOSE",font=fonts,bg="blue")
LOSE.place(x=470,y=10)
DROW=Label(frame,text="DROW",font=fonts,bg="blue")
DROW.place(x=250,y=10)
usercan=Canvas(frame,width=200,height=200,bg="orange")
comcan=Canvas(frame,width=200,height=200,bg="orange")
scorewin=Label(frame,text='0',font=fonts,bg="blue")
scoredrow=Label(frame,text='0',font=fonts,bg="blue")
scorelose=Label(frame,text='0',font=fonts,bg="blue")
scoredrow.place(x=350,y=10)
scorewin.place(x=90,y=10)
scorelose.place(x=550,y=10)
StoneButton=Button(frame,text="__________STONE__________",command=lambda : Stone(frame),bg="brown")
PaperButton=Button(frame,text="__________PAPER__________",command=lambda : Paper(frame),bg="lightblue")
ScissorButton=Button(frame,text="________SCISSOR________",command=lambda : Scissor(frame),bg="gray")
#StartButton=Button(frame,text="___________START_____________",bg="green",command=lambda : Start(frame,n))
usercan.place(x=50,y=250)
comcan.place(x=350,y=250)
StoneButton.place(x=30,y=500)
PaperButton.place(x=250,y=500)
ScissorButton.place(x=450,y=500)
#StartButton.place(x=240,y=550)
root.mainloop()



