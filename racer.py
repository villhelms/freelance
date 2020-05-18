import turtle

wn = turtle.Screen()
wn.screensize(480,480)
scene = turtle.Turtle()
car = turtle.Turtle()
speed = 10

def road():
  scene.speed(10)
  scene.setheading(0)
  scene.penup()
  scene.setposition(-480,200)
  scene.pendown()
  scene.forward(1000)
  scene.penup()
  scene.setposition(-480,-200)
  scene.pendown()
  scene.forward(1000)
  scene.penup()
  scene.setposition(-480, 100)
  for i in range(10):
    scene.pendown()
    scene.forward(50)
    scene.penup()
    scene.forward(60)
    scene.pendown()
  scene.penup()
  scene.setposition(-480, -100)
  for i in range(10):
    scene.pendown()
    scene.forward(52)
    scene.penup()
    scene.forward(58)
    scene.pendown()
road()

def setStart():
  car.setheading(0)
  car.speed(1)
  car.penup()
  car.setposition(-467,-50)
  car.pendown()

setStart()

def carMovement():
  car.forward(speed)
  wn.ontimer(carMovement,10)


def setCarHeading(angle):
  old_speed = car.speed()
  car.speed(0)
  car.setheading(angle)
  car.speed(old_speed)

wn.onkey(lambda: setCarHeading(90), 'Up')
wn.onkey(lambda: setCarHeading(180),'Left')
wn.onkey(lambda: setCarHeading(0),'Right')
wn.onkey(lambda: setCarHeading(-90),'Down')
wn.listen()
carMovement()

wn.mainloop()
