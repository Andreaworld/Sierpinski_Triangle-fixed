import turtle

def Sierpinski_Triangle(t, length, depth):
    if depth == 1:
        for _ in range(3):
            t.fd(length)
            t.lt(120)
    else:
        for _ in range(3):
            Sierpinski_Triangle(t, length // 2, depth - 1)
            t.fd(length)
            t.lt(120)

if __name__ == "__main__":
    L = input("Length: ")
    D = input("Depth: ")

    screen = turtle.Screen()
    t = turtle.Turtle()
    Sierpinski_Triangle(t, int(L), int(D))
    turtle.done()
