import turtle #Simple importing

t= turtle.Turtle() #this link the pointer
s= turtle.Screen() #the screen provided
u= turtle.Turtle() #you can add another pointer;

s.bgcolor("black") #color provided to SCREEN 
u.color("white") #┌(・。・)┘♪
t.color("white") #color provided to pointer
t.speed(0)
u.speed(0) #here 0-max, 1-min
t.penup() #lift pen up to stop drawing
t.goto(0,-600) #set pointer to this position
t.pendown() #lift pen down to stop drawing
#t.forward(100) #move pointer FORWARD
# t.left(100) # TURN POINTER LEFT
" " "BUT THAT'S' WASTE IF YOU HAVE TO REPEAT IT AGAIN AND AGAIN,SO ∆" " "
t.fillcolor("purple") #fill color...in the shape which you draw by "t"
t.begin_fill()
#∆
for i in range(4):
     t.forward(100)
     t.left(90)
t.end_fill()
u.penup()
u.goto(50,-450)
u.pendown()
u.fillcolor("red")
u.begin_fill()
u.circle(50)  
u.end_fill()  
t.penup()   
t.left(90)
t.fd(290)#SHORT FORM--FORWARD
t.pendown()
t.penup()
t.goto(25,-300)
t.pendown()
t.fillcolor("blue")
t.begin_fill()
for i in range(8):
      t.fd(144)
      t.rt(135) #SHORT FORM--RIGHT
t.end_fill() 
u.left(90)   
t.penup()
t.goto(50,-80)
t.pendown()
t.fillcolor("pink")
t.begin_fill()
t.left(30)
for i in range(2):
      t.fd(200)
      t.rt(120)
#t.forward(200)
#t.right(120)
#t.forward(200)
#t.right(120)
#t.fd(200)
t.end_fill()

s.exitonclick()
" " " imp. for holding the screen and to exit when click...always in last{IMP} " " "

