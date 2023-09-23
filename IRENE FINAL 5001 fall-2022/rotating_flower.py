"""
    IRENE CAI
    CS5001 FALL2022
    FINAL PROJECT
    drawing moudle -- rotating flower
"""


def draw(turtle_name,angle, n):
    """内部使用的小函数"""
    """ not important to understand """
    turtle_name.circle(5+n, 60)
    turtle_name.left(angle)
    turtle_name.circle(5+n, 60)


def rotating_flower_draw(parameter_1, parameter_2):
    """ drawing function """

    import turtle
    import colorsys
    import time

    # 生成真实参数
    # generate real parameter that fit to each drawing function
    a = int((parameter_1 * parameter_2) % 20 + 90)
    b = int((parameter_1 * parameter_2) % 30 + 90)
    cc = int((parameter_1 * parameter_1) ** 2 % 180 + 90)
    #print(cc) # 这里！！！！注意！！！c是用来表示颜色的变量名，不可占用
    d = int((parameter_2 * parameter_2) ** 2 % 180 + 90)
    time_difference = int((parameter_1 ** parameter_2) % 100)


    # 基础
    # set up
    turtle.tracer(150)
    h = 0.1

    t = turtle.Turtle()
    t2 = turtle.Turtle()

    t.hideturtle()
    t2.hideturtle()

    t.pensize(4)
    t2.pensize(4)

    t.goto(0,0)
    t2.goto(0,0)

    # 开始绘图
    # drawing
    for i in range(time_difference):
        c = colorsys.hls_to_rgb(h, 0.9, 1)
        h += 0.005
        
        t.pencolor(c)

        turtle.bgcolor(c)

        t.penup()
        draw(t, a, i)
        draw(t, cc, i)
        t.down()

        draw(t, 1/2, i-i)
        draw(t, d, i)
        draw(t, b, i)

    for i in range(time_difference,200):
        i2 = i-time_difference
        c = colorsys.hls_to_rgb(h, 0.9, 1)
        t.pencolor(c)
        
        h += 0.005
        h2 = h-0.015
        c2 = colorsys.hls_to_rgb(h, 0.9, 1)
        t2.pencolor(c2)
        
        t.pencolor(c)
        
        turtle.bgcolor(c)

        t.penup()
        t2.penup()
        
        draw(t, a, i)
        draw(t2, a, i2)
        
        draw(t, cc, i)
        draw(t2, cc, i2)

        
        t.pendown()
        t2.pendown()

        draw(t, 1/2, i-i)
        draw(t2, 1/2, i2-i2)
        
        draw(t, d, i)
        draw(t2, d, i2)
        
        draw(t, b, i)
        draw(t2, b, i2)



    for i in range(200,201+time_difference):
        i2 = i-time_difference
        c = colorsys.hls_to_rgb(h, 0.9, 1)
        h += 0.005

        h2 = h-0.015
        c2 = colorsys.hls_to_rgb(h, 0.9, 1)
        t2.pencolor(c2)

        turtle.bgcolor(c)

        t2.penup()
        draw(t2, a, i2)
        draw(t2, cc, i2)
        t2.down()

        draw(t2, 1/2, i2-i2)
        draw(t2, d, i2)
        draw(t2, b, i2)


    # 结尾
    # ending
    time.sleep(0.2)
    t.clear()
    t2.clear()
    turtle.bgcolor("white")
    t.reset()
    t2.reset()


if __name__ == "__main__":
    rotating_flower_draw(12, 8)
