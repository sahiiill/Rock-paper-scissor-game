from tkinter import *
from PIL import Image, ImageTk
from random import randint

#Main Window
root = Tk()
root.title("Rock, Paper And Scissor!")
root.configure(background="cyan")


#Picture  H=Human, C=Computer
rockH_img=ImageTk.PhotoImage(Image.open("rockH.png"))
rockC_img=ImageTk.PhotoImage(Image.open("rockC.png"))
paperH_img=ImageTk.PhotoImage(Image.open("paperH.png"))
paperC_img=ImageTk.PhotoImage(Image.open("paperC.png"))
scissorH_img=ImageTk.PhotoImage(Image.open("scissorH.png"))
scissorC_img=ImageTk.PhotoImage(Image.open("scissorC.png"))


#Inserting Pictures
labelH= Label(root,image=rockH_img, bg="cyan")
labelC= Label(root,image=rockC_img, bg="cyan")
labelH.grid(row=1,column=0)
labelC.grid(row=1,column=4)


#Points
Hscore=Label(root,text=0,font=100,bg="cyan")
Cscore=Label(root,text=0,font=100,bg="cyan")
Hscore.grid(row=1,column=1)
Cscore.grid(row=1,column=3)

#Indicator
indicatorH=Label(root,text="You",font=50,bg="cyan")
indicatorC=Label(root,text="Computer",font=50,bg="cyan")
indicatorH.grid(row=0,column=1)
indicatorC.grid(row=0,column=3)


#Message
msg=Label(root,font=50,bg="cyan")
msg.grid(row=3,column=2)

#update message
def updateMessage(x):
    msg["text"]= x

#update user points
def updateScoreH():
    score = int(Hscore["text"])
    score =score+ 1
    Hscore["text"]= str(score)

#update comp points    
def updateScoreC():
    score=int(Cscore["text"])
    score += 1
    Cscore["text"]= str(score)


#find winner
def gameWinner(you,comp):
    if you == comp:
        updateMessage("It's a tie!")
    elif you == "rock":
        if comp == "paper":
            updateMessage("You loose...")
            updateScoreC()
        else:
            updateMessage("YOU WIN!!!!")
            updateScoreH()
    elif you == "paper":
        if comp == "scissor":
            updateMessage("You loose...")
            updateScoreC()
        else:
            updateMessage("YOU WIN!!!!")
            updateScoreH()
    elif you == "scissor":
        if comp == "rock":
            updateMessage("You loose...")
            updateScoreC()
        else:
            updateMessage("YOU WIN!!!!")
            updateScoreH()
    else:
        pass

#Update choices
choices=["rock","paper","scissor"]

def updateChoice(x):

#for Computer
    choiceC=choices[randint(0,2)]
    if choiceC=="rock":
        labelC.configure(image=rockC_img)
    elif choiceC=="paper":
        labelC.configure(image=paperC_img)
    else:
        labelC.configure(image=scissorC_img)


#for User
    if x == "rock":
        labelH.configure(image=rockH_img)
    elif x == "paper":
        labelH.configure(image=paperH_img)
    else:
        labelH.configure(image=scissorH_img)

    gameWinner(x, choiceC)



#Button
rock=Button(root,width=20,height=3,text="ROCK",bg="red", command=lambda: updateChoice("rock")).grid(row=2,column=1)
paper=Button(root,width=20,height=3,text="PAPER",bg="blue", command=lambda: updateChoice("paper")).grid(row=2,column=2)
scissor=Button(root,width=20,height=3,text="SCISSOR",bg="green", command=lambda: updateChoice("scissor")).grid(row=2,column=3)

root.mainloop()