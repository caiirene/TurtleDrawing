"""
    IRENE CAI
    CS5001 FALL2022
    FINAL PROJECT
    drawing moudle -- curvy_flower
"""


def curvy_flower_draw(parameter_1, parameter_2):
    """ drawing function """

    import turtle
    import colorsys
    import time

    # 生成真实参数(好像不用int()也可以)
    # generate real parameter that fit to each drawing function
    a = int((parameter_1 * parameter_2) ** parameter_1 % 60)
    b = int((parameter_1 * parameter_2) ** parameter_2 %200)
    cc = int((parameter_1 * parameter_1) ** (parameter_1 + parameter_2)) % 180 + 90
    time_difference = int((parameter_1 ** parameter_2) % 100)

    # 基础设置 set up
    t = turtle.Turtle()
    t2 = turtle.Turtle()

    t.ht()
    t2.ht()
    
    turtle.tracer(200)

    t.speed(0)
    t2.speed(0)

    h = 1

    t.goto(0,0)
    t2.goto(0,0)

    # 开始绘图 drawing
    for i in range(time_difference):

        t.pensize(i/80+1)
        c=colorsys.hsv_to_rgb(h,1,1)
        bgc = colorsys.hls_to_rgb(h,0.9,1)
        
        t.pencolor(c)
        turtle.Screen().bgcolor(bgc)

        t.left(a)
        
        t.circle(i*0.4, b)
        
        t.circle(-i * 0.4, cc)
        
        t.circle(i * 0.4, 90)

        t.circle(i, -1*cc)
        
        h += 0.005

    for i in range(time_difference, 200):

        i2 = i - time_difference
        
        t.pensize(i/80+1)
        t2.pensize(i2/80+1)
        
        c=colorsys.hsv_to_rgb(h,1,1)
        bgc = colorsys.hls_to_rgb(h,0.9,1)
        
        t.pencolor(c)
        t2.pencolor(bgc)
        
        turtle.Screen().bgcolor(bgc)

        t.left(a)
        t2.left(a)
        
        t.circle(i*0.4, b)
        t2.circle(i2*0.4, b)
        
        t.circle(-i * 0.4, cc)
        t2.circle(-1*i2 * 0.4, cc)
        
        t.circle(i * 0.4, 90)
        t2.circle(i2 * 0.4, 90)

        t.circle(i, -1*cc)
        t2.circle(i2, -1*cc)
        
        h += 0.005

    for i in range(200,200+time_difference+1):

        i2 = i-time_difference

        t2.pensize(i2/80+1)
        
        c=colorsys.hsv_to_rgb(h,1,1)
        bgc = colorsys.hls_to_rgb(h,0.9,1)
        
        t2.pencolor(bgc)
        turtle.Screen().bgcolor(bgc)

        t2.left(a)
        
        t2.circle(i2*0.4, b)
        
        t2.circle(-1*i2 * 0.4, cc)
        
        t2.circle(i2 * 0.4, 90)

        t2.circle(i2, -1*cc)
        
        h += 0.005

    # 结尾 ending
    time.sleep(0.2)
    t.clear()
    t2.clear()
    turtle.bgcolor("white")
    t.reset()
    t2.reset()


if __name__ == "__main__":
    curvy_flower_draw(1, 2)
