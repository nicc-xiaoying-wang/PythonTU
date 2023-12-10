import unittest
from ex_05 import *

freq_file_name = "freq_en_50k.txt"
prefix_freq_file_name = "freq_en_prefixes.txt"

class TestTask1(unittest.TestCase):
    
    def setUp(self):
        self.frequencies = read_frequency_file(freq_file_name)
    
    #Test 1: successful processing
    def test_read_frequency_file1(self):
        self.assertNotEqual(self.frequencies, None)
    
    #Test 2: result is a list
    def test_read_frequency_file2(self):
        self.assertIsInstance(self.frequencies, type([]))
    
    #Test 3: correct size of list
    def test_read_frequency_file3(self):
        self.assertEqual(len(self.frequencies), 50000)
    
    #Test 4: items on list are tuples
    def test_read_frequency_file4(self):
        self.assertIsInstance(self.frequencies[0], type(()))
        self.assertIsInstance(self.frequencies[1], type(()))
    
    #Test 5: tuples have correct length
    def test_read_frequency_file5(self):
        self.assertEqual(len(self.frequencies[0]), 2)
        self.assertEqual(len(self.frequencies[1]), 2)
    
    #Test 6: first element of tuple is a string
    def test_read_frequency_file6(self):
        self.assertIsInstance(self.frequencies[0][0], type(""))
        self.assertIsInstance(self.frequencies[1][0], type(""))
    
    #Test 7: second element of tuple is an integer
    def test_read_frequency_file7(self):
        self.assertIsInstance(self.frequencies[0][1], type(1))
        self.assertIsInstance(self.frequencies[1][1], type(1))

    #Test 8: list entries 1, 10, and 20 are correct
    def test_read_frequency_file8(self):
        self.assertEqual(self.frequencies[1], ("i", 19975318))
        self.assertEqual(self.frequencies[10], ("in", 5649786))
        self.assertEqual(self.frequencies[20], ("your", 3611383))


class TestTask2(unittest.TestCase):
    
    def setUp(self):
        self.frequencies = read_frequency_file(freq_file_name)
        self.thresholds = determine_decile_thresholds(self.frequencies)
    
    #Test 9: successful processing
    def test_determine_decile_thresholds1(self):
        self.assertNotEqual(self.thresholds, None)
    
    #Test 10: result is a list
    def test_determine_decile_thresholds2(self):
        self.assertIsInstance(self.thresholds, type([]))
    
    #Test 11: items on the list are integers
    def test_determine_decile_thresholds3(self):
        self.assertIsInstance(self.thresholds[0], type(1))
        self.assertIsInstance(self.thresholds[1], type(1))
    
    #Test 12: correct number of items on the list
    def test_determine_decile_thresholds4(self):
        self.assertEqual(len(self.thresholds), 9)
    
    #Test 13: thresholds are in ascending order
    def test_determine_decile_thresholds5(self):
        self.assertTrue(self.thresholds[0] < self.thresholds[1])
        self.assertTrue(self.thresholds[1] < self.thresholds[2])
        self.assertTrue(self.thresholds[2] < self.thresholds[3])
        self.assertTrue(self.thresholds[3] < self.thresholds[4])
        self.assertTrue(self.thresholds[4] < self.thresholds[5])
        self.assertTrue(self.thresholds[5] < self.thresholds[6])
        self.assertTrue(self.thresholds[6] < self.thresholds[7])
        self.assertTrue(self.thresholds[7] < self.thresholds[8])
    
    #Test 14: the first entry is in the correct range
    def test_determine_decile_thresholds6(self):
        self.assertIn(self.thresholds[0], [1, 2, 3])
    
    #Test 15: the last entry is in the correct range
    def test_determine_decile_thresholds7(self):
        self.assertIn(self.thresholds[8], [2614, 2615, 2616, 2617, 2618, 2619, 2620])
    
    #Test 16: complete identity with the expected thresholds
    def test_determine_decile_thresholds8(self):
        self.assertEqual(self.thresholds, [3, 8, 18, 34, 62, 115, 252, 662, 2617])

class TestTask3(unittest.TestCase):
    
    def setUp(self):
        self.frequencies = read_frequency_file(freq_file_name)
        self.prefix_frequencies = sorted(get_prefix_frequencies(self.frequencies))

    #Test 17: successful processing
    def test_get_prefix_frequencies1(self):
        self.assertNotEqual(self.prefix_frequencies, None)
    
    #Test 18: result is a list of tuples
    def test_get_prefix_frequencies2(self):
        self.assertIsInstance(self.prefix_frequencies, type([]))
        self.assertIsInstance(self.prefix_frequencies[0], type(()))
        self.assertIsInstance(self.prefix_frequencies[1], type(()))

    #Test 19: correct counts for first four prefixes
    def test_get_prefix_frequencies3(self):
        self.assertEqual(self.prefix_frequencies[0], ("a", 45546869))
        self.assertEqual(self.prefix_frequencies[1], ("aa", 55975))
        self.assertEqual(self.prefix_frequencies[2], ("aaa", 7478))
        self.assertEqual(self.prefix_frequencies[3], ("aaaa", 2175))
        self.assertEqual(self.prefix_frequencies[4], ('aaaaa', 774))
        self.assertEqual(self.prefix_frequencies[5], ('aaaaaa', 324))
        self.assertEqual(self.prefix_frequencies[6], ('aaaaaaa', 132))
    
    #Test 20: correct counts for all remaining prefixes starting in aaaa
    def test_get_prefix_frequencies4(self):
        self.assertEqual(self.prefix_frequencies[7], ('aaaaaaah', 132))
        self.assertEqual(self.prefix_frequencies[8], ('aaaaaah', 192))
        self.assertEqual(self.prefix_frequencies[9], ('aaaaah', 450))
        self.assertEqual(self.prefix_frequencies[10], ('aaaag', 110))
        self.assertEqual(self.prefix_frequencies[11], ('aaaagh', 110))
        self.assertEqual(self.prefix_frequencies[12], ('aaaah', 1092))
        self.assertEqual(self.prefix_frequencies[13], ('aaaar', 199))
        self.assertEqual(self.prefix_frequencies[14], ('aaaarg', 199))
        self.assertEqual(self.prefix_frequencies[15], ('aaaargh', 199))
    
    #Test 21: correct counts for additional block of prefixes (the word aaliyah)
    def test_get_prefix_frequencies5(self):
        self.assertEqual(self.prefix_frequencies[37], ('aal', 110))
        self.assertEqual(self.prefix_frequencies[38], ('aali', 110))
        self.assertEqual(self.prefix_frequencies[39], ('aaliy', 110))
        self.assertEqual(self.prefix_frequencies[40], ('aaliya', 110))
        self.assertEqual(self.prefix_frequencies[41], ('aaliyah', 110))
    
    #Test 22: no prefix is stored more than once
    def test_get_prefix_frequencies6(self):
        prefixes = set()
        for prefix, _ in self.prefix_frequencies:
             prefixes.add(prefix)
        self.assertEqual(len(prefixes),len(self.prefix_frequencies))
    
    #Test 23: whenever one prefix is a prefix of another, the count of the first one should be higher
    def test_get_prefix_frequencies7(self):
        for i in range(1000, 2000):
            if self.prefix_frequencies[i][0].startswith(self.prefix_frequencies[i - 1][0]):
                self.assertTrue(self.prefix_frequencies[i - 1][1] >= self.prefix_frequencies[i][1])
    
    #Test 24: correct size of list
    def test_get_prefix_frequencies8(self):
        self.assertEqual(len(self.prefix_frequencies), 115117)
    

class TestTask4(unittest.TestCase):
    
    def setUp(self):
        #parse submitted file for analysis
        with open(prefix_freq_file_name, "r") as f:
            self.lines = f.readlines()
    
    #Test 25: successful processing
    def test_store_frequencies_alphabetically1(self):
        self.assertNotEqual(self.lines, None)
    
    #Test 26: lines are separated by a space
    def test_store_frequencies_alphabetically2(self):
        self.assertEqual(len(self.lines[0].split(" ")), 2)
    
    #Test 27: first column contains strings (= not parsable as positive integer)
    def test_store_frequencies_alphabetically3(self):
        for i in range(10, 30):
            prefix = self.lines[i].split(" ")[0]
            self.assertFalse(prefix.isdigit())
    
    #Test 28: second column contains integers (= parsable as positive integer)
    def test_store_frequencies_alphabetically4(self):
        for i in range(10, 30):
            count = self.lines[i].split(" ")[1][:-1]
            self.assertTrue(count.isdigit())
    
    #Test 29: keys are in alphabetical order (check three positions)
    def test_store_frequencies_alphabetically5(self):
        for i in range(10,30):
            prefix1 = self.lines[i].split(" ")[0]
            prefix2 = self.lines[i + 1].split(" ")[0]
            self.assertTrue(prefix1 < prefix2)
    
    #Test 30: first and second lines are correct
    def test_store_frequencies_alphabetically6(self):
        self.assertEqual(self.lines[0], "a 45546869\n")
        self.assertEqual(self.lines[1], "aa 55975\n")
    
    #Test 31: line 20 and 21 are correct
    def test_store_frequencies_alphabetically7(self):
        self.assertEqual(self.lines[16], "abandone 11896\n")
        self.assertEqual(self.lines[17], "abandoned 11896\n")
    
    #Test 32: no number among the first 200 is <= 1000
    def test_store_frequencies_alphabetically8(self):
        min_count = 1000
        for i in range(200):
            count = int(self.lines[i].split(" ")[1])
            if count < min_count:
                min_count = count
        self.assertEqual(min_count,1000)


if __name__ == '__main__':
    unittest.main()