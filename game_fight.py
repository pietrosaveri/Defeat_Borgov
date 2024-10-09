from tkinter import *
#window
wn=Tk()
wn.geometry('800x500')
wn.configure(background=('black'))

#instructions
welcome = Label(wn, text='Gain 20 points in this game to increase your level of attack stamina and satiety in the story.', bg='black', fg='white')
welcome.grid(column=0, row=0)
intructions =Label(wn, text='press the red button when the green square is the place near the yellow arrow to win.', bg='black', fg='white')
intructions.grid(column=0, row=1)
#yellow arrow

wn.create_rectangle(0, 0, 100, 100, fill="blue", outline = 'blue')
 
