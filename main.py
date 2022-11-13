from time import sleep
import colorsys, random
from turtle import *
from tqdm import tqdm
print("Welcome to Satisfier")
s_mode = input("Press 1 for the progress bar, 2 for a satisfying star, 3 for a circle made of straight lines, 4 for a rainbow benzene, 5 for a cool circle, 6 for among us, 7 for an infinite square, or 8 for a random one: ")

if s_mode == "8":
    s_mode = random.randint(1,7)   
if s_mode == "1" or 1:
    for i in tqdm(range(1000)):
        print()
        sleep(0.01)
    sleep(100)
if s_mode == "2" or 2:
    color('red', 'yellow')
    begin_fill()
    while True:
        forward(200)
        left(170)
        if abs(pos()) < 1:
            break
    end_fill()
    done()
if s_mode == "3" or 3:
    t = Turtle() 
    Screen().bgcolor("black") 
    t.speed(100) 
    n = 36 
    h = 0 
    for i in range(460): 
        c = colorsys.hsv_to_rgb(h,1,0.9) 
        h+=1/n 
        t.color(c) 
        t.left(145) 
        for i in range(5): 
            t.forward(300) 
            t.left(150) 
    done() 
if s_mode == "4" or 4:
    colors= ['red','purple','blue','green','orange','yellow',]

    t= Pen()

    bgcolor('black')

    t.speed(50)

    for x in range(200):

            t.pencolor(colors[x%6])

            t.width(x/100+1)

            t.forward(x)

            t.left(59)

    hideturtle()

    mainloop()
if s_mode == "5" or 5:
    ninja = Turtle() 
    ninja.speed(100)  
    for i in range(180): 
        ninja.forward(100) 
        ninja.right(30) 
        ninja.forward(20) 
        ninja.left(60) 
        ninja.forward(50) 
        ninja.right(30) 
        ninja.penup() 
        ninja.setposition(0, 0) 
        ninja.pendown() 
        ninja.right(2) 
    done() 
if s_mode == "6" or 6:


    BODY_COLOR = 'red' 

    BODY_SHADOW = ''

    GLASS_COLOR = '#9acedc'

    GLASS_SHADOW = ''

    s = getscreen()

    t = Turtle()

    # it can move forward backward left right

    def body():

        """ draws the body """

        t.pensize(20)

        #t.speed(15)

        t.fillcolor(BODY_COLOR)

        t.begin_fill()

        # right side

        t.right(90)

        t.forward(50)

        t.right(180)

        t.circle(40, -180)

        t.right(180)

        t.forward(200)

        # head curve

        t.right(180)

        t.circle(100, -180)

        # left side

        t.backward(20)

        t.left(15)

        t.circle(500, -20)

        t.backward(20)

        #t.backward(200)

        t.circle(40, -180)

        #t.right(90)

        t.left(7)

        t.backward(50)

        # hip

        t.up()

        t.left(90)

        t.forward(10)

        t.right(90)

        t.down()

        #t.right(180)

        #t.circle(25, -180)

        t.right(240)

        t.circle(50, -70)

        t.end_fill()

    def glass():

        t.up()

        #t.right(180)

        t.right(230)

        t.forward(100)

        t.left(90)

        t.forward(20)

        t.right(90)

        t.down()

        t.fillcolor(GLASS_COLOR)

        t.begin_fill()

        t.right(150)

        t.circle(90, -55)

        t.right(180)

        t.forward(1)

        t.right(180)

        t.circle(10, -65)

        t.right(180)

        t.forward(110)

        t.right(180)

        #t.right(180)

        t.circle(50, -190)

        t.right(170)

        t.forward(80)

        t.right(180)

        t.circle(45, -30)

        t.end_fill()

    def backpack():

        t.up()

        t.right(60)

        t.forward(100)

        t.right(90)

        t.forward(75)

        t.fillcolor(BODY_COLOR)

        t.begin_fill()

        t.down()

        t.forward(30)

        t.right(255)

        t.circle(300, -30)

        t.right(260)

        t.forward(30)

        t.end_fill()

    body()

    glass()

    backpack()

    t.screen.exitonclick()
if s_mode == "7" or 7:
    reset()
    hideturtle()
    speed(0)

    # bgcolor('black')

    c = 0
    x = 0

    colors = [
    #reddish colors
        (1.00, 0.00, 0.00),(1.00, 0.03, 0.00),(1.00, 0.05, 0.00),(1.00, 0.07, 0.00),(1.00, 0.10, 0.00),(1.00, 0.12, 0.00),(1.00, 0.15, 0.00),(1.00, 0.17, 0.00),(1.00, 0.20, 0.00),(1.00, 0.23, 0.00),(1.00, 0.25, 0.00),(1.00, 0.28, 0.00),(1.00, 0.30, 0.00),(1.00, 0.33, 0.00),(1.00, 0.35, 0.00),(1.00, 0.38, 0.00),(1.00, 0.40, 0.00),(1.00, 0.42, 0.00),(1.00, 0.45, 0.00),(1.00, 0.47, 0.00),
        #orangey colors
        (1.00, 0.50, 0.00),(1.00, 0.53, 0.00),(1.00, 0.55, 0.00),(1.00, 0.57, 0.00),(1.00, 0.60, 0.00),(1.00, 0.62, 0.00),(1.00, 0.65, 0.00),(1.00, 0.68, 0.00),(1.00, 0.70, 0.00),(1.00, 0.72, 0.00),(1.00, 0.75, 0.00),(1.00, 0.78, 0.00),(1.00, 0.80, 0.00),(1.00, 0.82, 0.00),(1.00, 0.85, 0.00),(1.00, 0.88, 0.00),(1.00, 0.90, 0.00),(1.00, 0.93, 0.00),(1.00, 0.95, 0.00),(1.00, 0.97, 0.00),
        #yellowy colors
        (1.00, 1.00, 0.00),(0.95, 1.00, 0.00),(0.90, 1.00, 0.00),(0.85, 1.00, 0.00),(0.80, 1.00, 0.00),(0.75, 1.00, 0.00),(0.70, 1.00, 0.00),(0.65, 1.00, 0.00),(0.60, 1.00, 0.00),(0.55, 1.00, 0.00),(0.50, 1.00, 0.00),(0.45, 1.00, 0.00),(0.40, 1.00, 0.00),(0.35, 1.00, 0.00),(0.30, 1.00, 0.00),(0.25, 1.00, 0.00),(0.20, 1.00, 0.00),(0.15, 1.00, 0.00),(0.10, 1.00, 0.00),(0.05, 1.00, 0.00),
        #greenish colors
        (0.00, 1.00, 0.00),(0.00, 0.95, 0.05),(0.00, 0.90, 0.10),(0.00, 0.85, 0.15),(0.00, 0.80, 0.20),(0.00, 0.75, 0.25),(0.00, 0.70, 0.30),(0.00, 0.65, 0.35),(0.00, 0.60, 0.40),(0.00, 0.55, 0.45),(0.00, 0.50, 0.50),(0.00, 0.45, 0.55),(0.00, 0.40, 0.60),(0.00, 0.35, 0.65),(0.00, 0.30, 0.70),(0.00, 0.25, 0.75),(0.00, 0.20, 0.80),(0.00, 0.15, 0.85),(0.00, 0.10, 0.90),(0.00, 0.05, 0.95),
        #blueish colors
        (0.00, 0.00, 1.00),(0.05, 0.00, 1.00),(0.10, 0.00, 1.00),(0.15, 0.00, 1.00),(0.20, 0.00, 1.00),(0.25, 0.00, 1.00),(0.30, 0.00, 1.00),(0.35, 0.00, 1.00),(0.40, 0.00, 1.00),(0.45, 0.00, 1.00),(0.50, 0.00, 1.00),(0.55, 0.00, 1.00),(0.60, 0.00, 1.00),(0.65, 0.00, 1.00),(0.70, 0.00, 1.00),(0.75, 0.00, 1.00),(0.80, 0.00, 1.00),(0.85, 0.00, 1.00),(0.90, 0.00, 1.00),(0.95, 0.00, 1.00)
    ]

    while x < 1000:
        idx = int(c)
        colore = colors[idx]
        color(colore)
        forward(x)
        right(98)
        x = x + 1
        c = c + 0.1

    exitonclick()
