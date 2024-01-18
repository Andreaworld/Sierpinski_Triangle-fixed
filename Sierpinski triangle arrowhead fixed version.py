import turtle

def Sierpinski_Triangle_Arrowhead(t, length, depth, direction=True):
    if depth == 0:
        t.fd(length)
    else:
        turn(t, 60, (not direction))
        Sierpinski_Triangle_Arrowhead(t, length // 2, depth - 1, (not direction))
        turn(t, 60, direction)
        Sierpinski_Triangle_Arrowhead(t, length // 2, depth - 1, direction)
        turn(t, 60, direction)
        Sierpinski_Triangle_Arrowhead(t, length // 2, depth - 1, (not direction))
        turn(t, 60, (not direction))

def turn(t, angle, direction):
    if direction:
        t.rt(angle)
    else:
        t.lt(angle)

if __name__ == "__main__":
    L = input("Length: ")
    D = input("Depth: ")

    screen = turtle.Screen()
    t = turtle.Turtle()
    Sierpinski_Triangle_Arrowhead(t, int(L), int(D))

    turtle.done()
