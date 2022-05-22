from tkinter import *

import random

tk =Tk()
canvas = Canvas(tk, width=400, height=600)
tk.title("Space Invaders")

#canvas.pack()
canvas.pack(expand=YES, fill=BOTH)

## Load the .gif image file.
#shipgif = PhotoImage(file='C:/Users/Viggo Piggle/Pictures/spaceshipgood.gif')
#ship2 =canvas.create_image(200, 500, image=shipgif, anchor=NW,tag="ship2")

#ship = canvas.create_rectangle(185, 570, 215, 600, fill="white", outline="red", tag="ship")
ship = canvas.create_line(200, 570, 200, 600,width = 10, fill="white", tag="ship")                         

global enemies
#creates enemies array
enemies = []

#create enemy ships and append to enemies array
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
    loaded_gun = 0
    #Assign variable C to the coordinates of the ship
    shipCoords = canvas.coords("ship")
    print("c0", shipCoords[0]) #first value in an array is index 0
    print("c1", shipCoords[1])
    print("c2", shipCoords[2])
    print("c3", shipCoords[3])
     
    #Creates the shot 
    canvas.create_line(shipCoords[0],shipCoords[1] + 20,shipCoords[2],shipCoords[3],width=5,fill="yellow",tag="shot")
    #Sets the loaded gun to 0 so it cannot fire
    
    #call function with the shot name
    move_shot("shot")

#animate the shot and detect if hits enemy
def move_shot(shotName):                      
    print("shotName =", shotName)
    #access loaded gun variable 
    global loaded_gun
    #move the shot up (-10) pixels 
    canvas.move(shotName,0,-10)
    canvas.update()
    #if loaded gun = 0 it means a shot is firing on the screen
    if loaded_gun == 0:
        shotCoords = canvas.coords(shotName) 
        print("shotCoords =", shotCoords)

        for enemy in enemies:
            #Get coordinates of enemy ship
            enemyCoords = canvas.coords(enemy)
            #Calculate enemy ships width
            enemywidth = enemyCoords[2] - enemyCoords[0]
            print("enemywidth =", enemywidth)

            #Testing if the shot hits enemy
            #does the shot intersect x axis of an enemy
            if enemyCoords[0] <= shotCoords[0] <= enemyCoords[0] +  enemywidth: 
                print("shot is in line with enemy X coords", enemy)

                #does the shot intersect y axis of an enemy
                if shotCoords[1] <= enemyCoords[1] + enemywidth: 
                    print("shotCoords[1]=", shotCoords[1])
                    print("shot hits enemy", enemy)
                    #shot hits enemy 
                    #remove hit enemy from canvas
                    canvas.delete(enemy) 
                    #remove hit enemy from enemies array
                    enemies.remove(enemy) 
                    #deletes the shot from the canvas
                    canvas.delete(shotName)
                    #the shot is gone and now the gun is reloaded
                    loaded_gun = 1
                    #Calls the update score function
                    update_score()
                    break
                
        if shotCoords[1] < 0: 
            #the shot is off the canvas so delete it
            canvas.delete(shotName)
            #reload the gun 
            loaded_gun = 1 

    #If the shot hasnt hit an enemy
    if loaded_gun == 0:
        #move shot wait 50 milliseconds 
        tk.after(1000, move_shot, "shot")

def update_score():
    global score
    score = score + 100
    print("score", score)
    widget.config(text=score)

#Binds the key binds so you can move left or right   
tk.bind("<Left>", left)
tk.bind("<Right>", right)
tk.bind("<space>", space)


#Had to move this to the bottom for it to work
canvas.pack(expand=YES, fill=BOTH)
tk.mainloop()
