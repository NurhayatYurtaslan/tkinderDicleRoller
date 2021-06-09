from tkinter import messagebox as mb
from tkinter import PhotoImage
import tkinter as tk
import random

r = tk.Tk()
r.geometry('700x600')
r.title('Nurlife Roller Dicle')

bg = PhotoImage('D:\image\background.jpg')
  
# Create Canvas
c = tk.Canvas(r, width=700, height=600)
#c.pack()
  
c.pack(fill = "both", expand = True)
  
# Display image
c.create_image( 0, 0, image = bg, anchor = "nw")




def roll_dice():
    global bttn_clicks
    # unicode character strings for dice
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    d = {'\u2680':1, '\u2681':2, '\u2682':3, '\u2683':4, '\u2684':5, '\u2685':6}
    die1 = random.choice(dice)
    die2 = random.choice(dice)
    ldice.configure(text=f'{die1} {die2}')
    c.create_window(300, 250, window=ldice)
    res = d[die1] + d[die2]
    label2.configure(text="You got  "+str(res))
    bttn_clicks += 1
    label1['text'] = "Dice rolled: " + str(bttn_clicks) + " times"
    if (bttn_clicks == 2 and res != 10):
        rollbutton.configure(state='disabled')
        mb.showerror("Game over", "Sorry,Try again")
    elif (res == 10):
        rollbutton.configure(state='disabled')
        mb.showinfo("Winner", "Congrats,you won!!")


def restart():
    global bttn_clicks
    bttn_clicks= 0
    label1.configure(text="")
    label2.configure(text="Not rolled yet")
    rollbutton.configure(state='normal')


ldice = tk.Label(r, text='', font=('Girassol', 120),fg='purple2')
rollbutton = tk.Button(r, text='Roll the dice', font=('girassol', 25,),state="disabled",background="MediumPurple1",foreground='white',height=1, width=15, command=roll_dice)
c.create_window(350, 120, window=rollbutton)
button1 = tk.Button(r, text='Start/Restart Game', font=('girassol', 25,),background="MediumPurple4",foreground='white',height=1, width=15, command=restart)
c.create_window(350, 50, window=button1)
label1 = tk.Label(r, text='', font=('Girassol',20,'bold'),fg='black')
c.create_window(180, 410, window=label1)
label2 = tk.Label(r, text='Not rolled yet', font=('Girassol',20,'bold'),bg='purple',fg='white',width=12)
c.create_window(480, 410, window=label2)
#label3 = tk.Label(r, text='Winning rule: The player wins if he/she gets a sum of 10 on rolling 2 dice,within 10 chances', font=('Times',13,'bold'),fg='white',bg="black")
#c.create_window(300, 450, window=label3)

# call the mainloop of Tk
r.mainloop()
