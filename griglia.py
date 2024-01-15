import turtle

def disQuadr(d, t):
    for _ in range(4):
        t.forward(d)
        t.left(90)
    t.forward(d)

def main():
    finestra = turtle.Screen()
    t = turtle.Turtle()
    SPOST = 10
    for _ in range(4):
        for _ in range(4):
            disQuadr(SPOST, t)
        t.left(90)
        t.forward(SPOST)
        t.left(90)
        t.forward(SPOST*4)
        t.left(180)       
    finestra.mainloop()

if __name__ == "__main__":
    main()