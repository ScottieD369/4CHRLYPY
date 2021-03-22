# 4 channel Relay Code By:Scottie Digital 2016

from Tkinter import *
import tkFont
import RPi.GPIO as GPIO
from subprocess import call

GPIO.setmode(GPIO.BOARD)
GPIO.setup(29, GPIO.OUT)
GPIO.setup(31, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.output(29, GPIO.HIGH)
GPIO.output(31, GPIO.HIGH)
GPIO.output(33, GPIO.HIGH)
GPIO.output(35, GPIO.HIGH)

win = Tk()
myFont = tkFont.Font(family = 'Helvetica', size = 22, weight = 'bold')

def rly1():
	#print("LED button pressed")
	if GPIO.input(29) :
                GPIO.output(29,GPIO.LOW)
                Relay1["text"]='ON'
                Relay1["bg"]="green"
	else:
		GPIO.output(29,GPIO.HIGH)
                Relay1["text"] = "OFF"
                Relay1["bg"]= "red"

def rly2():
	#print("LED button pressed")
	if GPIO.input(31) :
 		GPIO.output(31,GPIO.LOW)
		Relay2["text"] = "ON"
		Relay2["bg"]= "green"
	else:
		GPIO.output(31,GPIO.HIGH)
                Relay2["text"] = "OFF"
                Relay2["bg"]= "red"

def rly3():
	#print("LED button pressed")
	if GPIO.input(33) :
 		GPIO.output(33,GPIO.LOW)
		Relay3["text"] = "ON"
		Relay3["bg"]= "green"
	else:
		GPIO.output(33,GPIO.HIGH)
                Relay3["text"] = "OFF"
                Relay3["bg"]= "red"

def rly4():
	#print("LED button pressed")
	if GPIO.input(35) :
 		GPIO.output(35,GPIO.LOW)
		Relay4["text"] = "ON"
		Relay4["bg"]= "green"
	else:
		GPIO.output(35,GPIO.HIGH)
                Relay4["text"] = "OFF"
                Relay4["bg"]= "red"

def exitProgram():
	#print("Exit Button pressed")
        GPIO.cleanup()
	win.quit()	
def ShuttingDown():
	#print("Exit Button pressed")
        GPIO.cleanup()
	call("sudo shutdown -h now", shell=True)
	win.quit()			

win.config(background = "#000000")
win.geometry("{0}x{0}+0+0".format(win.winfo_screenwidth(),win.winfo_screenheight()))
win.attributes('-fullscreen', True)
win.resizable(0,0)

label0 = Label(win,text="4 Ch Relay Control",font=myFont,background="#000000",foreground="white")
label0.grid(row=1,column=2,columnspan=2,sticky="news")

label1 = Label(win,text="Relay 1",font=myFont,background="#000000",foreground="white")
label1.grid(row=2,column=1)

Relay1 = Button(win,text="Off",bg="red",font=myFont,command=rly1,height=4,width=10,activebackground="#FFFF33",activeforeground="#FF0000")
Relay1.grid(row=3,column=1)

label2 = Label(win,text="Relay 2",font=myFont,background="#000000",foreground="white")
label2.grid(row=2,column=2)

Relay2 = Button(win,text="Off",bg="red",font=myFont,command=rly2,height=4,width=10,activebackground="#FFFF33",activeforeground="#FF0000")
Relay2.grid(row=3,column=2)

label3 = Label(win,text="Relay 3",font=myFont,background="#000000",foreground="white")
label3.grid(row=2,column=3)

Relay3 = Button(win,text="Off",bg="red",font=myFont,command=rly3,height=4,width=10,activebackground="#FFFF33",activeforeground="#FF0000")
Relay3.grid(row=3,column=3)

label4 = Label(win,text="Relay 4",font=myFont,background="#000000",foreground="white")
label4.grid(row=2,column=4)

Relay4 = Button(win,text="Off",bg="red",font=myFont,command=rly4,height=4,width=10,activebackground="#FFFF33",activeforeground="#FF0000")
Relay4.grid(row=3,column=4)

label6 = Label(background="#000000",foreground="white")
label6.grid(row=4,column=2,columnspan=2)

exitButton = Button(win,text="Exit",font=myFont,command=exitProgram,height=2,width=6,activebackground="#FFFF33",activeforeground="#FF0000") 
exitButton.place(x=6,y=395)

ShutdownButton = Button(win,text="Off",font=myFont,command=ShuttingDown,height=2,width=6,activebackground="#FFFF33",activeforeground="#FF0000") 
ShutdownButton.place(x=666,y=395)

mainloop()