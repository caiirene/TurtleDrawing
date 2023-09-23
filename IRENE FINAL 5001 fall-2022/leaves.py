"""
    IRENE CAI
    CS5001 FALL2022
    FINAL PROJECT
    drawing moudle -- leaves
"""


def leaves_draw(parameter_1, parameter_2):
    """ drawing function """

    import turtle
    import colorsys
    import time

    # 生成真实参数
    # generate real parameter that fit to each drawing function
    a = int((parameter_1 * parameter_2) % 10 + 5)
    b = int((parameter_1 ** parameter_2) % 300 + 600)
    time_difference = int((parameter_1 ** parameter_2) % 50 + 50)


    # 基础
    # set up
    turtle.tracer(150)
    h = 0.001
    n = 889

    turtle.bgcolor("black")

    t = turtle.Turtle()
    t2 = turtle.Turtle()

    t2.pencolor("black")

    t.hideturtle()
    t2.hideturtle()

    t.pensize(1)
    t2.pensize(1)

    t.goto(0,0)
    t2.goto(0,0)

    # 开始绘图
    # drawing
    for i in range(time_difference):
        
        c = colorsys.hsv_to_rgb(h, 1, 0.7)
        h += 0.005

        t.pencolor(c)

        t.up()
        t.goto(-8, -25)
        t.down()
        t.fd(i)
        t.rt(b)
        t.fillcolor(c)
        t.begin_fill()
        t.circle(a, 320)
        t.end_fill()
        t.fd(i)

        t.bk(1)
        t.rt(6)

    for i in range(time_difference,300):

        i2 = i - time_difference

        
        c = colorsys.hsv_to_rgb(h, 1, 0.7)
        h += 0.005

        t.pencolor(c)

        t.up()
        t2.up()
        
        t.goto(-8, -25)
        t2.goto(-8, -25)
        
        t.down()
        t2.down()
        
        t.fd(i)
        t2.fd(i2)
        
        t.rt(b)
        t2.rt(b)
        
        t.fillcolor(c)
        t2.fillcolor("black")
        
        t.begin_fill()
        t2.begin_fill()
        
        t.circle(a, 320)
        t2.circle(a, 320)
        
        t.end_fill()
        t2.end_fill()
        
        t.fd(i)
        t.fd(i2)

        t.bk(1)
        t2.bk(1)
        
        t.rt(6)
        t2.rt(6)

    for i in range(301, 301+time_difference):

        i2 = i - time_difference

        c = colorsys.hsv_to_rgb(h, 1, 0.7)
        h += 0.005

        t.pencolor(c)

        t2.up()
        t2.goto(-8, -25)
        t2.down()
        t2.fd(i2)
        t2.rt(b)
        t2.fillcolor("black")
        t2.begin_fill()
        t2.circle(a, 320)
        t2.end_fill()
        t2.fd(i2)

        t2.bk(1)
        t2.rt(6)

    # 结尾
    # ending
    time.sleep(0.2)
    t.clear()
    t2.clear()
    turtle.bgcolor("white")
    t.reset()
    t2.reset()


if __name__ == "__main__":
    leaves_draw(12,5) # just an example
