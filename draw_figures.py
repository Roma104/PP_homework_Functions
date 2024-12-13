import turtle
from figures import draw_square, draw_triangle, draw_rectangle  # Import the function from figures.py

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Create the turtle
pen = turtle.Turtle()
pen.speed(5)

# Draw figures in different locations
# Draw first square
pen.penup()
pen.goto(-150, 150)  # Move to new location
pen.pendown()
draw_square(pen,100)

# Draw second square
pen.penup()
pen.goto(100, 100)
pen.pendown()
draw_square(pen,50)

# Draw first triangle
pen.penup()
pen.goto(-150, 0)
pen.pendown()
draw_triangle(pen, 100)

# Draw second triangle
pen.penup()
pen.goto(50, 0)
pen.pendown()
draw_triangle(pen, 100)

# Draw first rectangle
pen.penup()
pen.goto(-150, -150)
pen.pendown()
draw_rectangle(pen, 120, 60)

# Draw second rectangle
pen.penup()
pen.goto(50, -150)
pen.pendown()
draw_rectangle(pen, 120, 60)

# Hide the turtle and finish
pen.hideturtle()
window.mainloop()