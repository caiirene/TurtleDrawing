"""
    Irene Cai
    CS5001 Fall 2022
    Final project -- main()01

    This py file mainly collecting user's input and store them as task list into txt

    step 1: input
    step 2: remove punctuations and make a word list
    step 3: calculate the weight of each word
    step 4: get the top 3
    step 5: store thoes top 3 as task list
    step 6: write into txt as 'a'
"""


from collections import defaultdict
import random
import json


def remove_punctuation(sentence, dicc):
    """
        *unittest include
        This function remove all punctuations and turn all character into lower case
        剔除标点符号
        parameter: string and dict
        return: list
    """
    PUNCTUATION = ".,!?-:;\t\n()[]{}@#\\$%^*-_+= /'\"|~<>”“‘’？（），。、！"

    for punc in PUNCTUATION:
        sentence = sentence.replace(punc, " ")

    sentence = sentence.lower()
    old_sentence_list = sentence.split()

    sentence_list = []

    # check is the word searchable in the dictionary I just created
    # for thoes words not in my dictionary, I just ignore them, so no error will be raised
    for word in old_sentence_list:
        if word in dicc:
            sentence_list.append(word)
            
    return sentence_list


def calculate_word_weight(sentence_list, dicc):
    """
        计算每个单词的权重，并找出前三名
        *unittest included
        calculate the weight for each word
        parameter: list of strings, and the dictionary
        return: list of ints
    """

    # 这里提前设置前三名的初始值，防止有些句子少于三个单词
    # set up three positions for top three words
    maxx = 0
    maxx2 = 0
    maxx3 = 0
    choice = []
    choice_2 = []
    choice_3 = []

    # 设置字典为默认列表，甚防意外
    # set a default dictionary as list
    dicc_排行 = defaultdict(list)


    ### 开始计算 calculation start
    for i in range(len(sentence_list)):

        # 名词 noun
        if dicc[sentence_list[i]][0] == "n.":
            分数 = 5
            
            if i >= 1:
                if dicc[sentence_list[i-1]][0] == "adj.":
                    分数 += 4
                elif dicc[sentence_list[i-1]][0] == "v.":
                    分数 += 3
                elif dicc[sentence_list[i-1]][0] == "other":
                    分数 += 2
            if i < len(sentence_list)-2:
                if dicc[sentence_list[i+1]][0] == "v.":
                    分数 += 2
                elif dicc[sentence_list[i+1]][0] == "adj.":
                    分数 += -1
                elif dicc[sentence_list[i+1]][0] == "adv.":
                    分数 += 1
                elif dicc[sentence_list[i+1]][0] == "other":
                    分数 += 1

        # 动词 verb
        elif dicc[sentence_list[i]][0] == "v.":
            分数 = 4

            if i >= 1:
                if dicc[sentence_list[i-1]][0] == "other":
                    分数 += 4
                elif dicc[sentence_list[i-1]][0] == "adv.":
                    分数 += 3
                elif dicc[sentence_list[i-1]][0] == "n.":
                    分数 += 2
            if i < len(sentence_list)-2:
                if dicc[sentence_list[i+1]][0] == "other":
                    分数 += 2
                elif dicc[sentence_list[i+1]][0] == "adv.":
                    分数 += -2
                elif dicc[sentence_list[i+1]][0] == "adj.":
                    分数 += 1
                elif dicc[sentence_list[i+1]][0] == "n.":
                    分数 += 1

        # 形容词 adj.
        elif dicc[sentence_list[i]][0] == "adj.":
            分数 = 3

            if i >= 1:
                if dicc[sentence_list[i-1]][0] == "v.":
                    分数 += 4
                elif dicc[sentence_list[i-1]][0] == "other":
                    分数 += 3
                elif dicc[sentence_list[i-1]][0] == "adv.":
                    分数 += 2
                elif dicc[sentence_list[i-1]][0] == "n.":
                    分数 += 1
            if i < len(sentence_list)-2:
                if dicc[sentence_list[i+1]][0] == "adv.":
                    分数 += 2
                elif dicc[sentence_list[i+1]][0] == "other":
                    分数 += 1
                elif dicc[sentence_list[i+1]][0] == "v.":
                    分数 += -1
                elif dicc[sentence_list[i+1]][0] == "n.":
                    分数 += -2

        # 副词 adv.
        elif dicc[sentence_list[i]][0] == "adv.":
            分数 = 2

            if i >= 1:
                if dicc[sentence_list[i-1]][0] == "adj.":
                    分数 += 4
                elif dicc[sentence_list[i-1]][0] == "other":
                    分数 += 3
                elif dicc[sentence_list[i-1]][0] == "n.":
                    分数 += 2
                elif dicc[sentence_list[i-1]][0] == "v.":
                    分数 += 1
            if i < len(sentence_list)-2:
                if dicc[sentence_list[i+1]][0] == "v.":
                    分数 += 2
                elif dicc[sentence_list[i+1]][0] == "other":
                    分数 += 1
                elif dicc[sentence_list[i+1]][0] == "adv.":
                    分数 += -1
                elif dicc[sentence_list[i+1]][0] == "n.":
                    分数 += -2

        # 其它 others
        elif dicc[sentence_list[i]][0] == "other":
            分数 = 1


        ### 开始选出前三 choose tope three
        # 使用依次推进的方式 push one by one
        if 分数 >= maxx:

            maxx3 = maxx2
            choice_3 = choice_2
            
            maxx2 = maxx
            choice_2 = choice
            
            maxx = 分数
            choice = sentence_list[i]

    #print(choice, dicc[choice], maxx)

    # 列表记录：【函数选择dicc[choice][1], 次选生成参数, 三选生成参数】 generate the task list
    new_task = [dicc[choice][1], maxx2, maxx3]
    #print(new_task)

    return new_task
    
    

def main():
    """
        get input, generate task list, and then write it into txt
        parameter: no
        return: no
    """
    
    while True:
        # First, ask the sentense input
        print("Enter any sentence. 'Q' to stop.")
        sentence = input("Enter: ")
        if sentence == "Q":
            return False

        # Second, download dictionary
        with open('json_dic.json', 'r') as f:
            dicc = json.load(f)

        # remove all punctuation and make a list that has word in dicc, no worry about error here, because all input is string, even empty str
        sentence_list = remove_punctuation(sentence, dicc)

        # 这里用try/except是因为有些句子太短，无法使用calculate_word_weight函数
        # try/except here because if the sentence_list is empty, the calculate_word_weight function won't work
        # and sometime the txt file is under controled by another py file
        try:
            
            # 生成要写入task文件的内容（单个列表）
            new_task = calculate_word_weight(sentence_list,dicc)
            string_task = f'{str(new_task[0])} {str(new_task[1])} {str(new_task[2])} \n'

            # 写入
            f = open("task_list.txt", "a", encoding="utf-8")
            f.write(string_task)
            print("载入内容完成......")
            f.close()

        except:
            pass # 对，就是pass，比起缺少一两个input，error可难看太多了
            

if __name__ == "__main__":
    main()
