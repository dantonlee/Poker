from tkinter import *
from PIL import ImageTk, Image

'''alt+B to start program in Sublime
'''

'''This program assists me in understanding Game Theory Optimal solutions for Spin N Gos: 3-handed hyper turbos.  
'''

'''Heads up nash equilibrium solutions 10- bbs'''
def display_nash():

	global nash
	nash = var6.get()

	if nash == "NASHJAM":
		imagenash = "C:/Python3.8/Spins/NASHJAM.png"
	elif nash == "NASHCALL":
		imagenash = "C:/Python3.8/Spins/NASHCALL.png"

	file = ImageTk.PhotoImage(Image.open(imagenash))
	label = Label(image=file)
	label.image = file
	label.grid(row=5, columnspan=6, pady=50)

'''show images from folder'''
def display_img():
	global actn
	actn = var4.get()

	if pos == "SB":
		image = '_'.join([ply,pos,bb])
	elif pos == "BBvsBTN":
		image = '_'.join([ply,pos,bb, "raise"])
	else:
		image = '_'.join([ply,pos,bb,actn])

	imagefile = "C:/Python3.8/Spins/" + image + ".png"

	file = ImageTk.PhotoImage(Image.open(imagefile))
	label = Label(image=file)
	label.image = file
	label.grid(row=5, columnspan=6, pady=50)

	var6.set(0)

'''response to villain: raise or limped pot?'''
def display_rspns():
	for i in r4:
		r4[i].grid_remove()
		var4.set(0)


	global bb
	bb = var3.get()

	if pos == "SB":
		values4 = {}
		display_img()
		return
	elif pos == "BBvsBTN":
		values4 = {}
		display_img()
		return
	else:
		values4 = {"raise" : "raise", "limp" : "limp"}

	count = 0

	label_4 = Label(root, text="Response?", width=10,font=("bold", 10))
	label_4.grid(row=4,column=count)
	for (t,v) in values4.items():
		count += 1
		r4[count] = Radiobutton(root, text=t, variable=var4, value=v, indicator=0, background="light blue", command=display_img)
		r4[count].grid(row=4, column=count, sticky=W)

'''Show number of effective big blinds'''
def display_bb():

	for i in r3:
		r3[i].grid_remove()
		var3.set(0)

	for i in r4:
		r4[i].grid_remove()
		var4.set(0)

	global pos
	pos = var2.get()

	if ply == "HU" and pos == "SB":
		values3 = {"9-11bb" : "9-11bb", "11-13bb" : "11-13bb", "13-17bb" : "13-17bb"}
	elif ply == "HU" and pos == "BB":
		values3 = {"11-13bb" : "11-13bb", "13-17bb" : "13-17bb"}
	elif ply == "3H" and pos == "SB":
		values3 = {"12-14bb" : "12-14bb", "14-17bb" : "14-17bb", "17-22bb" : "17-22bb", "22-25bb" : "22-25bb"}
	elif ply == "3H" and pos == "BB":
		values3 = {"10-12bb" : "10-12bb", "12-14bb" : "12-14bb", "14-17bb" : "14-17bb", "17-21bb" : "17-21bb", "21-25bb" : "21-25bb"}
	elif ply == "3H" and pos == "BBvsBTN":
		values3 = {"11-14bb" : "11-14bb", "14-17bb" : "14-17bb", "17-21bb" : "17-21bb", "21-25bb" : "21-25bb"}

	count = 0

	label_3 = Label(root, text="BBs?", width=10,font=("bold", 10))
	label_3.grid(row=3,column=count)
	for (t,v) in values3.items():
		count += 1
		r3[count] = Radiobutton(root, text=t, variable=var3, value=v, indicator=0, background="light blue", command=display_rspns)
		r3[count].grid(row=3, column=count, sticky=W)

'''Positions: Small Blind, Big Blind, Button'''
def display_pstn():

	for i in r2:
		r2[i].grid_remove()
		var2.set(0)

	for i in r3:
		r3[i].grid_remove()
		var3.set(0)

	for i in r4:
		r4[i].grid_remove()
		var4.set(0)

	global ply
	ply = var.get()

	if ply == "HU":
		values2 = {"SB" : "SB", "BB" : "BB"}
	else:
		values2 = {"SB" : "SB", "BB" : "BB", "BBvsBTN" : "BBvsBTN"}

	count = 0

	label_2 = Label(root, text="Position?",width=10,font=("bold", 10))
	label_2.grid(row=2, column=count)
	for (t, v) in values2.items():
		count += 1
		r2[count] = Radiobutton(root, text=t, variable=var2, value=v, indicator=0, background="light blue", command=display_bb)
		r2[count].grid(row=2, column=count, sticky=W)

'''initialize'''
root = Tk()
root.geometry('640x710')
root.title("Jackpot SitNGos")

r2 = dict()
r3 = dict()
r4 = dict()
var = StringVar()
var2 = StringVar()
var3 = StringVar()
var4 = StringVar()

var6 = StringVar()
global file

values = {"2" : "HU", "3" : "3H"}
count = 0

label_1 = Label(root, text="Players?",width=10,font=("bold", 10))
label_1.grid(row=1, column=count)

label_6 = Label(root, text="NASH?",width=10,font=("bold", 10))
label_6.grid(row=6, column=count)
Radiobutton(root, text="NASH JAM", variable=var6, value="NASHJAM", indicator=0, background="pink", command=display_nash).grid(row=6, column=1, sticky=W)
Radiobutton(root, text="NASH CALL", variable=var6, value="NASHCALL", indicator=0, background="pink", command=display_nash).grid(row=6, column=2, sticky=W)


for (t, v) in values.items():
	count += 1
	Radiobutton(root, text=t, variable=var, value=v, indicator=0, background="light blue", command=display_pstn).grid(row=1, column=count, sticky=W)


root.mainloop()






















