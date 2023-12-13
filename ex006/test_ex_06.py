import unittest
from ex_06 import *

file_name = "th-eng-dict.tsv"


class TestTask1(unittest.TestCase):

    def setUp(self):
        self.th_eng_dict = read_file_to_dict(file_name)

    # Test 1: successful processing:
    def test_read_file_to_dict1(self):
        self.assertNotEqual(self.th_eng_dict, None)

    # Test 2: result is a dictionary:
    def test_read_file_to_dict2(self):
        self.assertIsInstance(self.th_eng_dict, type(dict()))

    # Test 3: correct size of the dictionary
    def test_read_file_to_dict3(self):
        self.assertEqual(len(self.th_eng_dict), 43)

    # Test 4: correct mapping in the dictionary:
    def test_read_file_to_dict4(self):
        self.assertEqual(self.th_eng_dict["ใน"], ('nai', 'PRP', 'in'))


class TestTask2(unittest.TestCase):

    def setUp(self):
        self.th_eng_dict = read_file_to_dict(file_name)
        self.sentence = "ดาวอังคารเป็นดาวเคราะห์ลำดับที่สี่จากดวงอาทิตย์"
        self.tokenized_simply = simple_tokenizer(self.th_eng_dict, self.sentence)

    # Test 5: result is a list
    def test_simple_tokenizer1(self):
        self.assertIsInstance(self.tokenized_simply, type(list()))

    # Test 6: correct size of the list
    def test_simple_tokenizer2(self):
        self.assertEqual(len(self.tokenized_simply), 11)

    # Test 7: elements in the list are tuples
    def test_simple_tokenizer3(self):
        self.assertIsInstance(self.tokenized_simply[0], type(tuple()))
        self.assertIsInstance(self.tokenized_simply[1], type(tuple()))

    # Test 8: tuples in the list are of correct size
    def test_simple_tokenizer4(self):
        self.assertEqual(len(self.tokenized_simply[0]), 4)
        self.assertEqual(len(self.tokenized_simply[1]), 4)

    # Test 9: list entries 0 and 5 are correct
    def test_simple_tokenizer5(self):
        self.assertEqual(self.tokenized_simply[0], ('ดาว', 'daaw', 'N', 'star; spot'))
        self.assertEqual(self.tokenized_simply[5], ('ลำดับ', 'lamdǎp', 'N', 'sequence'))

    # Test 10: list entries 1 and 10 are correct
    def test_simple_tokenizer6(self):
        self.assertEqual(self.tokenized_simply[1], ('อังคาร', 'angkhaan', 'NE', 'Mars'))
        self.assertEqual(self.tokenized_simply[10], ('อาทิตย์', 'aathīt', 'N', 'week; sun'))


class TestTast3(unittest.TestCase):

    def setUp(self):
        self.th_eng_dict = read_file_to_dict(file_name)
        self.sentence = "ดาวอังคารเป็นดาวเคราะห์ลำดับที่สี่จากดวงอาทิตย์"
        self.simple_tokens = th_tokens(self.th_eng_dict, self.sentence)

    # Test 11: list entries 0 and 5 are correct
    def test_th_tokens1(self):
        self.assertEqual(self.simple_tokens[0], "ดาว")
        self.assertEqual(self.simple_tokens[5], "ลำดับ")

    # Test 12: list entries 1 and 10 are correct
    def test_th_tokens2(self):
        self.assertEqual(self.simple_tokens[1], "อังคาร")
        self.assertEqual(self.simple_tokens[10], "อาทิตย์")


class TestTask4(unittest.TestCase):

    def setUp(self):
        self.th_eng_dict = read_file_to_dict(file_name)
        self.sentence = "ดาวอังคารเป็นดาวเคราะห์ลำดับที่สี่จากดวงอาทิตย์"
        self.simple_translit = th_translit(self.th_eng_dict, self.sentence)

    # Test 13: list entries 0 and 5 are correct
    def test_th_translit1(self):
        self.assertEqual(self.simple_translit[0], "daaw")
        self.assertEqual(self.simple_translit[5], "lamdǎp")

    # Test 14: list entries 1 and 10 are correct
    def test_translit2(self):
        self.assertEqual(self.simple_translit[1], "angkhaan")
        self.assertEqual(self.simple_translit[10], "aathīt")


class TestTask5(unittest.TestCase):

    def setUp(self):
        self.th_eng_dict = read_file_to_dict(file_name)
        self.sentence = "ดาวอังคารเป็นดาวเคราะห์ลำดับที่สี่จากดวงอาทิตย์"
        self.simple_pos = th_pos(self.th_eng_dict, self.sentence)

    # Test 15: list entries 0 and 5 are correct
    def test_th_pos1(self):
        self.assertEqual(self.simple_pos[0], "N")
        self.assertEqual(self.simple_pos[5], "N")

    # Test 16: list entries 1 and 8 are correct
    def test_th_pos2(self):
        self.assertEqual(self.simple_pos[1], "NE")
        self.assertEqual(self.simple_pos[8], "PRP")

class TestTask6(unittest.TestCase):

    def setUp(self):
        self.th_eng_dict = read_file_to_dict(file_name)
        self.sentence = "ดาวอังคารเป็นดาวเคราะห์ลำดับที่สี่จากดวงอาทิตย์"
        self.simple_gloss = th_gloss(self.th_eng_dict, self.sentence)

    # Test 17: list entries 0 and 5 are correct
    def test_th_gloss1(self):
        self.assertEqual(self.simple_gloss[0], "star; spot")
        self.assertEqual(self.simple_gloss[5], "sequence")

    # Test 18: list entries 1 and 10 are correct
    def test_th_gloss2(self):
        self.assertEqual(self.simple_gloss[1], "Mars")
        self.assertEqual(self.simple_gloss[10], "week; sun")

class TestTask7(unittest.TestCase):

    def setUp(self):
        self.th_eng_dict = read_file_to_dict(file_name)
        self.sentence = "ดาวอังคารเป็นดาวเคราะห์ลำดับที่สี่จากดวงอาทิตย์"
        self.tokenized_greedy = greedy_tokenizer(self.th_eng_dict, self.sentence)

    # Test 19: result is a list
    def test_greedy_tokenizer1(self):
        self.assertIsInstance(self.tokenized_greedy, type(list()))

    # Test 20: correct size of the list
    def test_greedy_tokenizer2(self):
        self.assertEqual(len(self.tokenized_greedy), 6)

    # Test 21: elements in the list are tuples
    def test_greedy_tokenizer3(self):
        self.assertIsInstance(self.tokenized_greedy[0], type(tuple()))
        self.assertIsInstance(self.tokenized_greedy[1], type(tuple()))

    # Test 22: tuples in the list are of correct size
    def test_greedy_tokenizer4(self):
        self.assertEqual(len(self.tokenized_greedy[0]), 4)
        self.assertEqual(len(self.tokenized_greedy[1]), 4)

    # Test 23: list entries 0 and 3 are correct
    def test_greedy_tokenizer5(self):
        self.assertEqual(self.tokenized_greedy[0], ('ดาวอังคาร', 'daaw angkhaan', 'NE', 'Mars (planet)'))
        self.assertEqual(self.tokenized_greedy[3], ('ลำดับที่สี่', 'lamdǎp thìi sǐi', 'A', 'fourth in sequence'))

    # Test 24: list entries 1 and 5 are correct
    def test_greedy_tokenizer6(self):
        self.assertEqual(self.tokenized_greedy[1], ('เป็น', "bpe'n", 'VI', 'be'))
        self.assertEqual(self.tokenized_greedy[5], ('ดวงอาทิตย์', 'duang aathīt', 'NE', 'Sun'))


class TestTast8(unittest.TestCase):

    def setUp(self):
        self.th_eng_dict = read_file_to_dict(file_name)
        self.sentence = "ดาวอังคารเป็นดาวเคราะห์ลำดับที่สี่จากดวงอาทิตย์"
        self.greedy_tokens = th_tokens_greedy(self.th_eng_dict, self.sentence)

    # Test 25: list entries 0 and 4 are correct
    def test_th_tokens_greedy1(self):
        self.assertEqual(self.greedy_tokens[0], "ดาวอังคาร")
        self.assertEqual(self.greedy_tokens[4], "จาก")

    # Test 26: list entries 1 and 5 are correct
    def test_th_tokens_greedy2(self):
        self.assertEqual(self.greedy_tokens[1], "เป็น")
        self.assertEqual(self.greedy_tokens[5], "ดวงอาทิตย์")


class TestTask9(unittest.TestCase):

    def setUp(self):
        self.th_eng_dict = read_file_to_dict(file_name)
        self.sentence = "ดาวอังคารเป็นดาวเคราะห์ลำดับที่สี่จากดวงอาทิตย์"
        self.greedy_translit = th_translit_greedy(self.th_eng_dict, self.sentence)

    # Test 27: list entries 0 and 4 are correct
    def test_th_translit_greedy1(self):
        self.assertEqual(self.greedy_translit[0], "daaw angkhaan")
        self.assertEqual(self.greedy_translit[4], "djǎak")

    # Test 28: list entries 1 and 5 are correct
    def test_translit_greedy2(self):
        self.assertEqual(self.greedy_translit[1], "bpe'n")
        self.assertEqual(self.greedy_translit[5], "duang aathīt")


class TestTask9(unittest.TestCase):

    def setUp(self):
        self.th_eng_dict = read_file_to_dict(file_name)
        self.sentence = "ดาวอังคารเป็นดาวเคราะห์ลำดับที่สี่จากดวงอาทิตย์"
        self.greedy_pos = th_pos_greedy(self.th_eng_dict, self.sentence)
        self.greedy_pos = th_pos_greedy(self.th_eng_dict, self.sentence)

    # Test 29: list entries 0 and 4 are correct
    def test_th_pos_greedy1(self):
        self.assertEqual(self.greedy_pos[0], "NE")
        self.assertEqual(self.greedy_pos[4], "PRP")

    # Test 30: list entries 1 and 5 are correct
    def test_th_pos_greedy2(self):
        self.assertEqual(self.greedy_pos[1], "VI")
        self.assertEqual(self.greedy_pos[5], "NE")


class TestTask11(unittest.TestCase):

    def setUp(self):
        self.th_eng_dict = read_file_to_dict(file_name)
        self.sentence = "ดาวอังคารเป็นดาวเคราะห์ลำดับที่สี่จากดวงอาทิตย์"
        self.greedy_gloss = th_gloss_greedy(self.th_eng_dict, self.sentence)

    # Test 31: list entries 0 and 4 are correct
    def test_th_gloss1(self):
        self.assertEqual(self.greedy_gloss[0], "Mars (planet)")
        self.assertEqual(self.greedy_gloss[4], "from")

    # Test 32: list entries 1 and 5 are correct
    def test_th_gloss2(self):
        self.assertEqual(self.greedy_gloss[1], "be")
        self.assertEqual(self.greedy_gloss[5], "Sun")


if __name__ == '__main__':
    unittest.main()