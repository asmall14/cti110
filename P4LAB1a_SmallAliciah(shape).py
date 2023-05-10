import turtle
win = turtle.Screen()   #Create a screen/workstation
luv = turtle.Turtle('turtle')   #Create a turtle named luv <3

#Create a square using loops

for num in range(4):
    luv.forward(100)
    luv.left(90)

#Move cursor to a different location

luv.penup()
luv.forward(200)
luv.pendown()

#Create a triangle using loops

for num in range(3):
    luv.forward(300)
    luv.left(120)
    
#end commands
win.mainloop()  #Wait for user to close window
