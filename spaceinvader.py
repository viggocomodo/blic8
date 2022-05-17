from tkinter import *

import random

tk =Tk()
canvas = Canvas(tk, width=400, height=600)
tk.title("Space Invaders")

#canvas.pack()
canvas.pack(expand=YES, fill=BOTH)

# Load the .gif image file.
shipgif = PhotoImage(file='C:/Users/Viggo Piggle/Pictures/spaceshipgood.gif')

#ship = canvas.create_rectangle(185, 570, 215, 600, fill="white", outline="red", tag="ship")
ship = canvas.create_line(200, 570, 200, 600,width = 10, fill="white", tag="ship")
                          
#ship2 =canvas.create_image(200, 500, image=shipgif, anchor=NW,tag="ship2")

global enemies
enemies = []

#create enemy ships
enemy1 = canvas.create_rectangle(35, 0, 65, 30, fill="red", outline="black")
enemies.append(enemy1)

enemy2 = canvas.create_rectangle(135, 0, 165, 30, fill="red", outline="black")
enemies.append(enemy2)

enemy3 = canvas.create_rectangle(235, 0, 265, 30, fill="red", outline="black")
enemies.append(enemy3)

enemy4 = canvas.create_rectangle(335, 0, 365, 30, fill="red", outline="black")
enemies.append(enemy4)

canvas.configure(bg='black')
                          
#I used the widget to put a score board
score = 0
widget = Label(canvas, text=score, fg="red", bg="black")  
widget.pack()
                          
#Tells the widget where it should be
canvas.create_window(200, 100, window=widget)       

# Used to go left or right with keybinds
def left(event): 
    # Used "print" for troubleshooting
    print("Left key pressed")
    x = -10
    y = 0
    canvas.move(ship, x, y)
        
def right(event):
    print("Right key pressed")
    x = 10
    y = 0
    canvas.move(ship, x, y)

def space(event):
    print("Space key pressed")    
    shooting()
    
#Makes so the gun can shoot
def shooting():
    global loaded_gun

    #Assign variable C to the coordinates of the ship
    c = canvas.coords("ship")
    print("c0", c[0]) #first value in an array is index 0
    print("c1", c[1])
    print("c2", c[2])
    print("c3", c[3])
    
    #Creates the shot
    canvas.create_line(c[0],c[1] + 20,c[2],c[3],width=5,fill="yellow",tag="shot")
    #Sets the loaded gun to 0 so it cannot fire
    loaded_gun = 0
    #call function and parse the shot name
    move_shot("shot")

def update_score():
    global score
    score = score + 100
    print("score", score)
    widget.config(text=score)
    
def move_shot(name):
    global loaded_gun
    canvas.move(name,0,-10)
    canvas.update()
    if loaded_gun == 0:
        shot = canvas.coords(name) 

        for x in enemies:
            #Get coordinates of enemy ship
            en = canvas.coords(x)
            #Calculate enemy ships width
            enemywidth = en[2] - en[0]
            print("enemywidth=", enemywidth)

            #Test if shot hits enemy
            if en[0] <= shot[0] <= en[0] +  enemywidth: 
                if shot[1] <= en[1] + enemywidth: 
                    #shot hits enemy 
                    canvas.delete(x) 
                    enemies.remove(x) 
                    canvas.delete(name)
                    loaded_gun = 1
                    update_score()
                    break
                
        if shot[1] < 0: 
            canvas.delete(name) 
            loaded_gun = 1 

    if loaded_gun == 0: 
        tk.after(50, move_shot, "shot")

#Binds the key binds so you can move left or right   
tk.bind("<Left>", left)
tk.bind("<Right>", right)
tk.bind("<space>", space)

#Had to move this to the bottom for it to work
canvas.pack(expand=YES, fill=BOTH)
tk.mainloop()
