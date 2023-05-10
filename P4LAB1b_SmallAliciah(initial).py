import turtle          
win = turtle.Screen()           #Create a screen/workstation
luv = turtle.Turtle('turtle')   #Create a turtle named luv <3

# add some display options
luv.pensize(2)           # Penshape
luv.pencolor("blue")     # Pencolor
luv.shape("turtle")

#Create first initial A
         
luv.right(120)
luv.forward(100)
luv.left(180)
luv.forward(100)
luv.right(120)
luv.forward(100)
luv.left(180)
luv.forward(50)
luv.left(60)
luv.forward(50)
luv.right(205)

#Move cursor to a different location

luv.penup()
luv.forward(100)
luv.pendown()


#Create last initial S

luv.circle(25,200)          
luv.left(180)            
luv.circle(20,-270)


# end commands
win.mainloop()      #Wait for user to close window
