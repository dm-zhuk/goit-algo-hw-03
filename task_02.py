import turtle


def koch_curve(t, depth, length):
    if depth == 0:
        t.forward(length)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, depth - 1, length / 3)
            t.left(angle)


def draw_koch_curve(depth, length=360):
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-length / 2, length / 2)
    t.pendown()

    for _ in range(3):
        koch_curve(t, depth, length)
        t.right(120)

    turtle.Screen().bgcolor("white")
    turtle.done()


# Get user input for recursion depth
try:
    depth = int(input("Enter the recursion depth (optimal range 1-4): "))
    if depth < 0:
        print("Please enter a positive integer.")
    elif depth > 6:
        print("Depth too high (might be slow or too detailed). Using 6 instead.")
        depth = 6

    draw_koch_curve(depth)

except ValueError:
    print("Invalid input. Please enter a positive integer.")
