import turtle

#draw a square
def draw_square(angle):
  
  square = turtle.Turtle()
  square.shape("square")
  square.color("black")
  square.speed(5)
  square.right(angle)

  num = 0;
  while num<4:
    square.forward(100)
    square.right(90)
    num =  num + 1

def circle_of_squares():
  window = turtle.Screen()
  window.bgcolor("red")

  num = 0

  while num<360:
    draw_square(num)
    num = num+5

  window.exitonclick();

circle_of_squares()