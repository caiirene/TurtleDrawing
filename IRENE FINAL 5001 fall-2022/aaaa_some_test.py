""""
    CS5001 Fall 2022
    FINAL PROJECT -- TEST FILE
    Irene Cai
"""

import unittest
import a_user_input
import aa_drawing_main
import json

# I need dicc
with open('json_dic.json', 'r') as f:
    dicc = json.load(f)
    

class FinalProjectTest(unittest.TestCase):

    def test_remove_punctuation(self):

        sentence = "Hello, my name is Irene. I don't want to write any test."
        result = a_user_input.remove_punctuation(sentence, dicc)
        self.assertEqual(result, ["hello", "my", "name", "is", "i", "want", "to", "write", "any", "test"])

    def test_calculate_word_weight(self):

        sentence_list = ["hello", "my", "name", "is", "i", "want", "to", "write", "any", "test"]
        return_list = a_user_input.calculate_word_weight(sentence_list, dicc)
        self.assertEqual(return_list, [4, 9, 7])

    def test_find_the_right_function_and_draw(self):

        test_1 = ["2", "abc", 12]
        self.assertEqual(aa_drawing_main.find_the_right_function_and_draw(test_1), "not int")

        test_2 = ["23", 12, 12]
        self.assertEqual(aa_drawing_main.find_the_right_function_and_draw(test_2), "no suitable translation yet")

        test_3 = [3, 8]
        self.assertEqual(aa_drawing_main.find_the_right_function_and_draw(test_3), "参数少于3个，parameter less than three, something wrong with txt")

        test_4 = ["10", "12", "9"]
        self.assertEqual(aa_drawing_main.find_the_right_function_and_draw(test_4), "no suitable translation yet")

        test_5 = ["aaa", "12", "9"]
        self.assertEqual(aa_drawing_main.find_the_right_function_and_draw(test_5), "main parameter not int")


def main():
    unittest.main(verbosity = 3)


if __name__ == '__main__':
    main()
