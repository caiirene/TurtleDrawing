"""
    IRENE CAI
    CS5001 FALL2022
    FINAL PROJECT
    drawing moudle -- spider_web
"""


def spider_web_draw(parameter_1, parameter_2):
    """ drawing function """

    import turtle
    import colorsys
    import time

    # 生成真实参数
    # generate real parameter that fit to each drawing function
    a = int((parameter_1 * parameter_2) ** parameter_1 % 30)
    b = int((parameter_1 * parameter_2) ** parameter_2 % 360)
    cc = int((parameter_1 * parameter_1) ** 2 % 180 + 90)
    d = int((parameter_2 * parameter_2) ** 2 % 180 + 90)
    time_difference = int((parameter_1 ** parameter_2) % 100)

    # 设置初始数值
    # set up
    t = turtle.Turtle()
    t2 = turtle.Turtle()
    
    t.hideturtle()
    t2.hideturtle()

    t.pensize(2)
    t2.pensize(2)
    
    turtle.tracer(60)
    
    n = a #不大于30 (smaller than 30)
    c = 2
    L = b # 本质上这里就是0-360 (0-360)

    # drawing
    for i in range(time_difference):
        
        p = colorsys.hls_to_rgb(c,0.9,0.9)
        bgc = colorsys.hsv_to_rgb(c,0.2,0.4)
        
        t.pencolor(p)
        turtle.bgcolor(bgc)
        
        c += 0.004112
        
        t.circle(n)
        t.left(cc) # 不小于90 (bigger thann 90)
        t.circle(i,L)
        t.left(d) # 也是不小于90 (bigger than 90)
        t.circle(20 * c)

    for i in range(time_difference, 200):
        
        i2 = i - time_difference
        c2 = c - 2.148032000000004
        
        p = colorsys.hls_to_rgb(c,0.9,0.9)
        bgc = colorsys.hsv_to_rgb(c,0.2,0.4)

        t.pencolor(p)
        t2.pencolor(bgc)
        turtle.bgcolor(bgc)
        
        c += 0.004112
        
        t.circle(n)
        t2.circle(n)
        
        t.left(cc) # 不小于90
        t2.left(cc)
        
        t.circle(i,L)
        t2.circle(i2,L)
        
        t.left(d) # 也是不小于90
        t2.left(d)
        
        t.circle(20 * c)
        t2.circle(20 * c2)

    for i in range(200, 201+time_difference):

        i2 = i - time_difference
        c2 = c - 2.148032000000004
        
        p = colorsys.hls_to_rgb(c,0.9,0.9)
        bgc = colorsys.hsv_to_rgb(c,0.2,0.4)
        
        t2.pencolor(bgc)
        turtle.bgcolor(bgc)
        
        c += 0.004112
        
        t2.circle(n)
        t.undo()
        t.undo()
        t.undo()
        t.undo()
        t2.left(cc) # 不小于90
        t.undo()
        t.undo()
        t2.circle(i2,L)
        t.undo()
        t.undo()
        t.undo()
        t.undo()
        t.undo()
        t2.left(d) # 也是不小于90
        t.undo()
        t.undo()
        t.undo()
        t.undo()
        t2.circle(20 * c2)
        t.undo()
        t.undo()
        t.undo()
        t.undo()
        t.undo()
        t.undo()
        t.undo()
        t.undo()
        t.undo()
        t.undo()
        # so many undo for artistic only

    # 结尾
    time.sleep(0.2)
    t.clear()
    t2.clear()
    turtle.bgcolor("white")
    t.reset()
    t2.reset()


if __name__ == "__main__":
    spider_web_draw(122, 8)
