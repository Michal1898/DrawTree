import turtle
turtle.speed("slowest")

def leaf_of_tree(distance):
    turtle.forward(distance)
    turtle.left(180)
    turtle.forward(distance)
    turtle.right(180)

leaf_of_tree(300)

