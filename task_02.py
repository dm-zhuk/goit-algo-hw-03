import turtle


def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)


def draw_koch_curve(order, size=360):
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, size / 2)
    t.pendown()

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    turtle.Screen().bgcolor("white")
    turtle.done()


# Get user input for recursion depth
try:
    depth = int(input("Enter the recursion depth (0-6 recommended): "))
    if depth < 0:
        print("Please enter a positive integer.")
    else:
        draw_koch_curve(depth)
except ValueError:
    print("Invalid input. Please enter a positive integer.")
