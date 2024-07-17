# import turtle

# timmy = turtle.Turtle()
# # print(timmy)
# timmy.shape("turtle")
# timmy.color("blue")
# timmy.backward(400)
# timmy.forward(600)

# my_screen = turtle.Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Name", ["Ali", "Ahmed", "Talal"])
table.add_column("Age", [34, 15, 19])
table.align = "r" # Aligns the table to the right
print(table)