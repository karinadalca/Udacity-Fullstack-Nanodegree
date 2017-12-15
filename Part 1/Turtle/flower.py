import turtle

#draw a square
def draw_square(size, angle):
  
  square = turtle.Turtle()
  square.shape("circle")
  square.color("red")
  square.speed(5)
  square.right(angle)

  num = 0;
  while num<4:
    square.forward(size)
    square.right(90)
    num =  num + 1

def draw_flower():
  window = turtle.Screen()
  window.bgcolor("white")

  num = 0

  while num<360:
    draw_square(60, num)
    num = num+10

  stem = turtle.Turtle();
  stem.shape("arrow")
  stem.color("green")
  stem.speed(5)
  stem.right(90)
  stem.forward(200)
  stem.right(180)
  stem.forward(60)
  stem.circle(20)
  stem.forward(30)
  stem.right(180)
  stem.circle(20)

  window.exitonclick();

draw_flower()