from tkinter import *
from PIL import Image,ImageTk
root=Tk()

root.title("canvas using funtions")
root.geometry("1000x1000")

colour=Label(root,text="Enter Colour",font=("times",20,"bold"))
colour.place(relx=0.6,rely=0.9,anchor=CENTER)

inputbox=Entry(root)
inputbox.insert(0,"black")
inputbox.place(relx=0.8,rely=0.9,anchor=CENTER)

canvas=Canvas(root,width=750,height=750,bg="white")
canvas.pack()

img=ImageTk.PhotoImage(Image.open("start_point1.png"))
my_image=canvas.create_image(50,50,image=img)

direction=""
oldx=50
oldy=50
newx=50
newy=50

def right_dir(event):
    global direction
    global oldx
    global oldy
    global newx
    global newy
    direction="right"
    oldx=newx
    oldy=newy
    newx=newx+5
    draw(direction, oldx, oldy, newx, newy)
    
def left_dir(event):
    global direction
    global oldx
    global oldy
    global newx
    global newy
    direction="left"
    oldx=newx
    oldy=newy
    newx=newx-5
    draw(direction, oldx, oldy, newx, newy)
    
def up_dir(event):
    global direction
    global oldx
    global oldy
    global newx
    global newy
    direction="up"
    oldx=newx
    oldy=newy
    newy=newy-5
    draw(direction, oldx, oldy, newx, newy)
    
def down_dir(event):
    global direction
    global oldx
    global oldy
    global newx
    global newy
    direction="down"
    oldx=newx
    oldy=newy
    newy=newy+5
    draw(direction, oldx, oldy, newx, newy)

def draw(direction,oldx,oldy,newx,newy):
    fillcolour=inputbox.get()
    if (direction=="right"):
        right_line=canvas.create_line(oldx, oldy,newx,newy,width=3,fill=fillcolour)
    if(direction=="left"):
        left_line=canvas.create_line(oldx,oldy,newx,newy,width=3,fill=fillcolour)
    if(direction=="up"):
        up_line=canvas.create_line(oldx,oldy,newx,newy,width=3,fill=fillcolour)
    if(direction=="down"):
        down_line=canvas.create_line(oldx,oldy,newx,newy,width=3,fill=fillcolour)
    
root.bind("<Right>",right_dir)
root.bind("<Left>",left_dir)
root.bind("<Up>",up_dir)
root.bind("<Down>",down_dir)

root.mainloop()