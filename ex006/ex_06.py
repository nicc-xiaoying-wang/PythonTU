"""
Python 2023 Assignment 06
"""

# IMPORTANT: assign the parts of your name and your student ID to these variables!
first_name = "Jane"
family_name = "Doe"
student_id = "12345678"


def read_file_to_dict(input_file):
    """
    Read in the contents of the input file in such a way 
    that you can retrieve the contents of columns 2, 3, and 4 
    by the (unique) values in column 1.

    :param input_file: Directory of the text file which contains Thai-English 
    dictionary consisting of 4 columns which represent Thai lexicon, 
    its transcription, category and glosses
    :type input_file: str
    :return: th_eng_dict: Thai-English dictionary
    :rtype: dict{str: (str, str, str)}
    """
    pass


def simple_tokenizer(th_dict, sentence):
    """
    Simple tokenizer, transliterator, part-of-speech tagger and glosser 
    that correctly analyses the example text based on the dictionary data.

    :param th_dict: Thai dictionary
    :type th_dict: dict
    :param sentence: Thai sentence
    :type sentence: str
    :return: list of tuples of format 
    (Thai token, transliteration, POS, English glosses)
    :rtype: list[tuple(str, str, str, str)]
    """
    pass


def th_tokens(th_dict, sentence):
    """
    Get the tokens of the Thai sentence using simple tokenizer.

    :param th_dict: Thai dictionary
    :type th_dict: dict
    :param sentence: Thai sentence
    :type sentence: str
    :return: list of tokens
    :rtype: list[str]
    """
    pass


def th_translit(th_dict, sentence):
    """
    Get the transliteration of Thai sentence tokens using simple tokenizer.

    :param th_dict: Thai dictionary
    :type th_dict: dict
    :param sentence: Thai sentence
    :type sentence: str
    :return: list of transliterations
    :rtype: list[str]
    """
    pass


def th_pos(th_dict, sentence):
    """
    Get the list of part of speech tags 
    of Thai sentence tokens using simple tokenizer.

    :param th_dict: Thai dictionary
    :type th_dict: dict
    :param sentence: Thai sentence
    :type sentence: str
    :return: list of POS tags
    :rtype: list[str]
    """
    pass


def th_gloss(th_dict, sentence):
    """
    Get the English glosses of Thai sentence tokens using simple tokenizer.

    :param th_dict: Thai dictionary
    :type th_dict: dict
    :param sentence: Thai sentence
    :type sentence: str
    :return: list of English glosses
    :rtype: list[str]
    """
    pass


def greedy_tokenizer(th_dict, sentence):
    """
    Greedy tokenizer, transliterator, part-of-speech tagger and glosser 
    that correctly analyses the example text based on the dictionary data. 
    Always find the longest chunk of characters starting at the current position 
    which can be found in the dictionary ("greedy search").

    :param th_dict: Thai dictionary
    :type th_dict: dict
    :param sentence: Thai sentence
    :param sentence: str
    :return: list of tuples of format 
    (Thai token, transliteration, POS, English glosses)
    :rtype: list[tuple(str, str, str, str)]
    """
    pass


def th_tokens_greedy(th_dict, sentence):
    """
    Get the tokens of Thai sentence using greedy tokenizer.

    :param th_dict: Thai dictionary
    :type th_dict: dict
    :param sentence: Thai sentence
    :type sentence: str
    :return: list of tokens
    :rtype: list[str]
    """
    pass


def th_translit_greedy(th_dict, sentence):
    """
    Get the transliteration of Thai sentence tokens using greedy tokenizer.

    :param th_dict: Thai dictionary
    :type th_dict: dict
    :param sentence: Thai sentence
    :type sentence: str
    :return: list of transliterations
    :rtype: list[str]
    """
    pass


def th_pos_greedy(th_dict, sentence):
    """
    Get the part of speech tags of Thai sentence tokens using greedy tokenizer.

    :param th_dict: Thai dictionary
    :type th_dict: dict
    :param sentence: Thai sentence
    :type sentence: str
    :return: list of POS tags
    :rtype: list[str]
    """
    pass


def th_gloss_greedy(th_dict, sentence):
    """
    Get the English glosses of Thai sentence tokens using greedy tokenizer.

    :param th_dict: Thai dictionary
    :type th_dict: dict
    :param sentence: Thai sentence
    :type sentence: str
    :return: list of English glosses
    :rtype: list[str]
    """
    pass


if __name__ == '__main__':
    file_name = "th-eng-dict.tsv"
    example = "ดาวอังคารเป็นดาวเคราะห์ลำดับที่สี่จากดวงอาทิตย์"
    pass