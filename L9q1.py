# File: L9q1.py
# Author: Michael Asokwah 
# Date: 11/15/2022
# Section: 506 
# E-mail: masokwah@tamu.edu  
# Description: 
# This program simulates a bagel store with a graphical interface, the user is
# able to select a bagel and add one or multiple desired toppings,
# displaying the price at the end of the order. 






import tkinter
import tkinter.messagebox

def cost():
    if radio_var.get()==1:
        bagel_cost=1.29
    elif radio_var.get() == 2:
        bagel_cost=1.59
    elif radio_var.get() == 3:
        bagel_cost=1.69
    elif radio_var.get() == 4:
        bagel_cost=1.49
    if cb_cream.get()==1:
        bagel_cost = bagel_cost+0.50

    if cb_butter.get()==1:
        bagel_cost = bagel_cost+0.20
    if cb_jelly.get()==1:
        bagel_cost = bagel_cost+0.70
    if cb_blueb.get()==1:
        bagel_cost = bagel_cost+0.70

    result = 'Total is $: ' + str(round(bagel_cost,2))
    tkinter.messagebox.showinfo('Bagel cost', result)
        
main_window = tkinter.Tk()

top_frame = tkinter.Frame(main_window)
middle_frame = tkinter.Frame(main_window)
bottom_frame = tkinter.Frame(main_window)


color_frame = tkinter.Frame(middle_frame, borderwidth=1, relief = "solid")
game_frame = tkinter.Frame(middle_frame, borderwidth=1, relief = "solid")

greeting = tkinter.Label(top_frame, text = "Welcome to Sarge's Bagel Hut \n All prices include tax")
greeting.pack()

color_label = tkinter.Label(color_frame, text = "Pick a bagel", bg = 'white', borderwidth = 1, relief = "solid")

radio_var = tkinter.IntVar()

radio_var.set(1)

color_label.pack(side='left')

white = tkinter.Radiobutton(color_frame, text = 'White - $'+str(1.29), variable=radio_var, value = 1)
wheat = tkinter.Radiobutton(color_frame, text = 'Wheat - $'+str(1.59), variable=radio_var, value = 2)
raisin = tkinter.Radiobutton(color_frame, text = 'Cinnamon Raisin - $'+str(1.69), variable=radio_var, value = 3)
onion = tkinter.Radiobutton(color_frame, text = 'Onion - $'+str(1.49), variable=radio_var, value = 4)


white.pack()
wheat.pack()
raisin.pack()
onion.pack()

cb_cream = tkinter.IntVar()
cb_butter = tkinter.IntVar()
cb_jelly = tkinter.IntVar()
cb_blueb = tkinter.IntVar()



item = tkinter.Label(game_frame, text = "Pick toppings", borderwidth = 1, relief = "solid")
item.pack(side='left')

cream = tkinter.Checkbutton(game_frame, text = 'Cream cheese - $0.50', variable=cb_cream, width=20)
butter = tkinter.Checkbutton(game_frame, text = 'Butter - $0.50', variable=cb_butter, width=20)
jelly = tkinter.Checkbutton(game_frame, text = 'Peach jelly - $0.70', variable=cb_jelly, width=20)
blueb = tkinter.Checkbutton(game_frame, text = 'Blueberry - $0.70', variable=cb_blueb,  width=20)

Color_button = tkinter.Button(bottom_frame, text='Calculate',command=cost)
quit_button = tkinter.Button(bottom_frame, text='Quit', command=main_window.destroy)

quit_button.pack()
Color_button.pack()

cream.pack()
butter.pack()
jelly.pack()
blueb.pack()

color_frame.pack(side='left')
game_frame.pack(side='right')

top_frame.pack()
middle_frame.pack()
bottom_frame.pack()

main_window.mainloop()


