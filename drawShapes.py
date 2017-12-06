import turtle

window = turtle.Screen()
window.bgcolor("red")

#draw a square
def draw_square():
  
  square = turtle.Turtle()
  square.shape("square")
  square.color("black")
  square.speed(1)

  num = 0;
  while num<4:
    square.forward(100)
    square.right(90)
    num =  num + 1

#draw a circle
def draw_circle():
  circle = turtle.Turtle()
  circle.shape("circle")
  circle.color("blue")
  circle.speed(1)

  circle.circle(100)

#draw a triangle
def draw_triangle():
  triangle = turtle.Turtle()
  triangle.shape("triangle")
  triangle.color("yellow")
  triangle.speed(3)

  triangle.forward(100)
  triangle.right(90)
  triangle.forward(100)
  triangle.left(45)
  triangle.backward(141.42)
  triangle.right(45)

draw_square()
draw_circle()
draw_triangle()

window.exitonclick();