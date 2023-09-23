from collections import defaultdict
import random
import json



"""
    This file only used to check thoes word length less or equal to 2
    Not important
"""
if __name__ == "__main__":
    
    f = open("all.txt", "r", encoding = "UTF-8")
    all_content = f.read()
    f.close()

    linelist = all_content.splitlines()
    # 首先，把文件变成列表

    dicc = defaultdict(list)
    # 此处创建一个默认列表的字典

    for i in range(len(linelist)):
        # 把文件大列表，的每一个元素，分割成两部分
        each_linelist = linelist[i].split()
        #print(each_linelist, i)

        key = each_linelist[0] # 这就是单词本身
        if len(key) <=2:
            print(each_linelist)
