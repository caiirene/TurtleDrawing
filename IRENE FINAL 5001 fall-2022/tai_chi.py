"""
    IRENE CAI
    CS5001 FALL2022
    FINAL PROJECT
    drawing moudle -- tai_chi
"""


def tai_chi_draw(parameter_1, parameter_2):
    """ drawing function """

    import turtle
    import colorsys
    import time

    # 判断真实参数
    # generate real parameter that fit to each drawing function
    a = ((parameter_1 * parameter_2) % 7 + 2) * 0.1
    b = ((parameter_1 * parameter_2) % 7 + 2) * 0.1

    # 基础
    # set up
    turtle.tracer(200)
    h = 0.1

    t = turtle.Turtle()

    t.hideturtle()

    t.pensize(7)

    t.up()

    t.goto(-40,-320)

    t.down()

    color_choice = ["red","yellow"]

    t.rt(4)

    # 开始绘图 drawing
    for i in range(600):

        if (parameter_1 % 2) == 0:
            bgc = colorsys.hls_to_rgb(h, a, b)
        elif (parameter_1 % 2) == 1:
            bgc = colorsys.hsv_to_rgb(h, a, b)

        h += 0.005

        turtle.bgcolor(bgc)

        if (parameter_2 % 2) == 0:
            t.color(color_choice[i%2])
        elif (parameter_2 % 2) == 1:
            t.color(bgc)

        t.up()
        t.circle(300-i, 90)
        t.down()
        t.circle(300-i, 92)



    # 结尾 ending
    time.sleep(0.2)
    t.clear()
    turtle.bgcolor("white")
    t.reset()


if __name__ == "__main__":
    tai_chi_draw(9, 8)
