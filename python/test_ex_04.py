import unittest
from ex_04 import *

class TestTask1(unittest.TestCase):
    def test_translate_ind_eng_1(self):
        ind_eng_dict = read_dict("ind_eng_dict.pickle")
        sentence = "ibu dan ayah saya tidak di rumah sekarang."
        expected = "mother and father I/my not in/at house/home now."
        produced = translate_ind_eng(sentence, ind_eng_dict)
        self.assertEqual(expected, produced)


class TestTask2(unittest.TestCase):
    def test_build_data_structure_1(self):
        ind_eng_dict = read_dict("ind_eng_dict.pickle")        
        sentence = "ibu dan ayah saya tidak di rumah sekarang."
        expected = [("ibu", ["mother"]), ("dan", ["and"]), ("ayah", ["father"]), ("saya", ["I", "my"]),
                    ("tidak", ["not"]), ("di", ["in", "at"]), ("rumah", ["house", "home"]), ("sekarang", ["now"])]
        produced = build_data_structure(sentence, ind_eng_dict)
        self.assertEqual(expected, produced)

class TestTask3(unittest.TestCase):
    def test_get_possible_glosses_1(self):
        ind_eng_dict = read_dict("ind_eng_dict.pickle")
        sentence = "ibu dan ayah saya tidak di rumah sekarang."
        produced = get_possible_glosses(sentence, ind_eng_dict)
        self.assertEqual(produced[0], ["ibu", "dan", "ayah", "saya", "tidak", "di", "rumah", "sekarang"])
        self.assertEqual(produced[1], ["mother", "and", "father", "I", "not", "in", "house", "now"])
        self.assertEqual(produced[2], ["", "", "", "my", "", "at", "home", ""])

class TestTask4(unittest.TestCase):
    def test_get_all_translations_1(self):
        ind_eng_dict = read_dict("ind_eng_dict.pickle")
        sentence = "ibu dan ayah saya tidak di rumah sekarang."
        expected = ['mother and father I not at home now', 'mother and father I not at house now',
                    'mother and father I not in home now', 'mother and father I not in house now',
                    'mother and father my not at home now', 'mother and father my not at house now',
                    'mother and father my not in home now', 'mother and father my not in house now']

        produced = sorted(get_all_translations(sentence, ind_eng_dict))
        self.assertEqual(expected, produced)


if __name__ == '__main__':
    unittest.main()