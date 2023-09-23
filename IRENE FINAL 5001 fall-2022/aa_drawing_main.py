"""
    Irene Cai
    CS5001 Fall 2022
    Final project -- main()02

    This py file is the drawing file, run it, it will give you turtle parttern

    step 1: read task list
    step 2: determent there is enough task for turtle to draw, if not,just wait or repeat
    step 3: once finish one task and there are more, then remove the finished task from txt
"""


import curvy_flower
import leaves
import rotating_flower
import spider_web
import tai_chi

import turtle
import colorsys
import json
import time


def find_the_right_function_and_draw(each_task_split_list):
    """
        take task_list,
        index 0 is the drawing function pointed
        index 1 and 2 are parameter for those drawing functions
        parameter: list of three int form string, so string
        return: no
        unittest include
    """

    # 虽然不可能，但万一输入了奇怪的list，直接pass，以防止index error
    # in case some strange thing in my txt
    if len(each_task_split_list) != 3:
        return "参数少于3个，parameter less than three, something wrong with txt"

    # 因为txt读取到的都是str，所以这里先转化为int. Change txt str into int
    # 虽不可能，但防万一 Make sure the parameters are int
    try:
        parameter_1 = int(each_task_split_list[1])
        parameter_2 = int(each_task_split_list[2])
    except ValueError:
        return "not int"
    except:
        return "some other error"

    # 此处排出[0]不能被转换成int的情况，或者是负数，小数 (check index 0 is ok to be int or negetive or float)
    if not each_task_split_list[0].isnumeric():
        return "main parameter not int"

    ###### 开始画图了 ######
    ###### drawing start #######
    if int(each_task_split_list[0]) == 1:
        curvy_flower.curvy_flower_draw(parameter_1, parameter_2)
        #print(1) -- assertEqual(find_the_right_function_and_draw([1,2,3]),1)
    
    elif int(each_task_split_list[0]) == 2:
        leaves.leaves_draw(parameter_1, parameter_2)

    elif int(each_task_split_list[0]) == 3:
        rotating_flower.rotating_flower_draw(parameter_1, parameter_2)

    elif int(each_task_split_list[0]) == 4:
        spider_web.spider_web_draw(parameter_1, parameter_2)

    elif int(each_task_split_list[0]) == 5:
        tai_chi.tai_chi_draw(parameter_1, parameter_2)

    else: # 这里是排出掉如果[0]不在1到5之中
        return "no suitable translation yet"
        

if __name__ == "__main__":
    
    def main():
        """迫不得已把函数写在这里，因为不会快速删除每行的前四个空格，就只好这样了"""

        # First, read task.txt
        # if file not found, just wait
        try:            
            f = open("task_list.txt", "r")
            task_list = f.readlines()
            print(task_list)
            f.close()
        except:
            time.sleep(1)
            return

        # 如果文件为空，就等等 if file empty, just wait
        if len(task_list) == 0:
            time.sleep(1)
            return

        # 如果txt里面只有一个任务，就循环做这个任务
        # if only one task in txt, then loop
        if len(task_list) == 1:
            each_task_split_list = task_list[0].split() #请注意，这里的element是string(element here is str)
            print(each_task_split_list)
            find_the_right_function_and_draw(each_task_split_list)

        # 如果任务数量大于等于2，做完一个删一个（画图开始前，先处理文件的原因是，不要一直占用着文件，input那边还要用这个txt呢）
        # If the number of tasks is greater than or equal to 2, delete one after it recored
        elif len(task_list) >= 2:
            # 先把文件覆盖写入剩余任务，记住当前任务，等写完再执行绘图
            current_task = task_list[0] #这里是一个string
            remain_task = task_list[1:] #这里应该是一个列表
            #print(remain_task)

            # 这里用for循环，是因为txt无法写入list，写进去就是空的
            # make list to string, in order to write in txt
            remain_task_string = ""
            for task in remain_task:
                remain_task_string += task
                
            # 这里需要加一个while loop吗？如果OSError发生，就再来一遍？但是是不是速度太快了？
            # in case file in used by another py program
            try:
                fa = open("task_list.txt", "w", encoding="utf-8")
                fa.write(remain_task_string)
                fa.close()
                print("覆盖完成......")
            except OSError:
                return

            # 开始执行当前绘图
            # start drawing
            each_task_split_list = current_task.split() # list of string here
            find_the_right_function_and_draw(each_task_split_list)

    while True:
        main()
