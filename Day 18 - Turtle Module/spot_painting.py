import turtle as tp
import random, colorgram as cp
import canvasvg
from reportlab.graphics import renderPDF
from svglib.svglib import svg2rlg


image_path = "C:\\Users\\hanzalah\\OneDrive\\Pictures\\spot painting hirst.webp"
colors_used = cp.extract(image_path, 10)
rgb_colors = []

for i in colors_used:
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

# print(rgb_colors)
colors = [(202, 166, 109), (152, 73, 47), (170, 153, 41), (222, 202, 138), (53, 93, 124), (135, 32, 22)]

spot = tp.Turtle()
tp.colormode(255)

a, b = 0, 0
for j in range(5):
    spot.penup()
    spot.goto(a, b)
    spot.pendown()
    for i in range(5):
        spot.pendown()
        spot.dot(20, random.choice(colors))
        spot.penup()
        spot.fd(50)
    b = b + 50
  


screen = tp.Screen()
canvas = screen.getcanvas()
canvasvg.saveall("turtle_output.svg", canvas)
drawing = svg2rlg("turtle_output.svg")
renderPDF.drawToFile(drawing, "turtle_output.pdf")



screen.exitonclick()