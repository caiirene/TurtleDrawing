"""
    << Engilsh translate to Turtle dictionary >>
    The main function of this py file is to convert all the words in the Oxford dictionary into the form I need.
    step 1: delete all translation part of Oxford dictionary.
    step 2: keep Word type as future use.
    step 3: add all possiable deformation of words, such as ed ing s es...
    step 4: generate a number for each word, and that num will become the turtle translation.(English translate to turtle)
    step 5: Leak filling (adding special words)
    step 5: save this dictionary to json file
"""


from collections import defaultdict
import random
import json


if __name__ == "__main__":

    # open the txt file
    f = open("all.txt", "r", encoding = "UTF-8")
    all_content = f.read()
    f.close()

    linelist = all_content.splitlines()
    # 首先，把文件变成列表 change txt string into a list by lines

    dicc = defaultdict(list)
    # 此处创建一个默认列表的字典 create a defaultdict in case of any accident

    # for list of lines, we need to split each line into at least two parts
    for i in range(len(linelist)):
        # 把文件大列表，的每一个元素，分割成两部分
        each_linelist = linelist[i].split()
        #print(each_linelist, i)

        key = each_linelist[0] # 这就是单词本身 index 0 is the english word

        raw_value = each_linelist[1] # 找出词型 index 1 is Word type

        # 根据词型，创造词汇的不同形式 generate different tense by word type #

        ### 动词 verb
        if "v." in raw_value:

            real_value = "v."

            # generate turtle translate num here
            assigned_num = random.randint(1,5) # 这里，统一生成一个随机数，分配给这个词，该词的变形也将使用这个随机数，以确保同义词指向相同的turtle翻译
            dicc[key] = [real_value, assigned_num] # 原型加入字典 put the original word into dictionary

            # 复数 third person singular
            if len(key) > 2:

                if key[-1] in "sxo" or key[-2:] == "sh" or key[-2:] == "ch":
                    复数_key = key + "es"
                elif key[-2] not in "aeiou" and key[-1] == "y":
                    复数_key = key[:-1] + "ies"
                else:
                    复数_key = key + "s"

                dicc[复数_key] = [real_value, assigned_num] # put into dict
            

            # 现在进行式 present tense
            if len(key) > 2:

                if key[-1] == "e" and key[-2] not in "aeiou":
                    进行式_key = key[:-1] + "ing" # 去掉e加ing
                elif key[-3::2] not in "aeiou" and key[-2] in "aeiou":
                    进行式_key = key + key[-1] + "ing"
                elif key[-2:] == "ie":
                    进行式_key = key[:-2] + "ing"
                else:
                    进行式_key = key + "ing"

                dicc[进行式_key] = [real_value, assigned_num] # put into dict

            # 过去式 past tense
            if len(key) > 2:

                if key[-1] == "e":
                    过去式_key = key + "d"
                else:
                    过去式_key = key + "ed"

                dicc[过去式_key] = [real_value, assigned_num] # put into dict

            # 过去分词太复杂了，不写了，爱咋滴咋滴 not past participle yet

        ### 名词 noun
        elif "n." in raw_value:

            real_value = "n."
            # 名词在动词之后elif，因为动词变化比名词多 Since verb has more variants, and some english word both verb and noun, real value goes to v.instead of n.

            # generate turtle translate num here
            assigned_num = random.randint(1,5)
            dicc[key] = [real_value, assigned_num] # 原型加入字典 put the original word into dictionary

            # 复数 plural
            if len(key) > 2:

                if key[-1] in "sxo" or key[-2:] == "sh" or key[-2:] == "ch":
                    复数_key = key + "es"
                elif key[-2] not in "aeiou" and key[-1] == "y":
                    复数_key = key[:-1] + "ies"
                elif key[-1] == "f":
                    复数_key = key[:-1] + "ves"
                elif key[-2:-1] == "fe":
                    复数_key = key[:-2] + "ves"
                else:
                    复数_key = key + "s"

                dicc[复数_key] = [real_value, assigned_num] # put into dict

        ### 形容词 adj.
        elif "adj." in raw_value:

            real_value = "adj."

            # generate turtle translate num here
            assigned_num = random.randint(1,5)        
            dicc[key] = [real_value, assigned_num] # put into dict

            if len(key) > 2:
                
                # 比较式
                if key[-1] == "e":
                    比较级_key = key + "r"
                elif key[-2] not in "aeiou" and key[-1] == "y":
                    比较级_key = key[:-1] + "ier"
                else:
                    比较级_key = key + "er"
                dicc[比较级_key] = [real_value, assigned_num] # put into dict

        ### 副词 adv.
        elif "adv." in raw_value:

            real_value = "adv."
            # generate turtle translate num  and put into dict
            dicc[key].append(real_value)
            dicc[key].append(random.randint(1,5))

        ### 其它 all others
        else:
            
            real_value = "other"
            dicc[key].append(real_value)
            dicc[key].append(random.randint(1,5))

    # 开始添加常用单词 add Common Words
    useful_vocabulary = ["a", "is", "am", "are", "was", "were", "done", "has", "haven't",
                         "an", "got", "taken", "took", "further", "farthest", "furthest"]

    for word in useful_vocabulary:
        dicc[word] = ["other", random.randint(1,5)]

    # 补充长度短于2的单词的变形 add words has len<2, (these words are searched by another py file)
    length_less_than_2 = ["goes", "gone", "going", "went", "oxen", "contour"]
    for word in length_less_than_2:
        dicc[word] = ["other", random.randint(1,5)]


    # 把创建的字典存起来 save the dictionary into json file
    with open("json_dic.json","w") as fa:
        json.dump(dicc,fa)
        print("加载入文件完成...")
