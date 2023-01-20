import turtle

turtle.mode("logo")
turtle.speed("slowest")
turtle.penup()
turtle.setpos(0,-0.4*turtle.window_height())
turtle.pendown()


def leaf_of_tree(distance):
    turtle.forward(distance)
    turtle.left(180)
    turtle.forward(distance)
    turtle.right(180)

def branch_of_tree(distance, angle):
    turtle.forward(distance/2)
    turtle.right(angle)
    leaf_of_tree(distance/2)
    turtle.left(angle)
    leaf_of_tree(distance/2)
    turtle.left(angle)
    leaf_of_tree(distance/2)
    turtle.right(angle)
    turtle.right(180)
    turtle.forward(distance/2)

branch_of_tree( 100, 60)
w=input("Press Enter")

