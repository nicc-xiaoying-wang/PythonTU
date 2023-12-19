"""
Python 2023 Assignment 06
"""

# IMPORTANT: assign the parts of your name and your student ID to these variables!
first_name = "Xiaoying"
family_name = "Wang"
student_id = "6802277"


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
    th_eng_dict = {}
    with open(input_file, 'r') as file: 
        for line in file: 
            columns = line.strip().split('\t')
            key = columns[0]
            value = tuple(columns[1:4])
            th_eng_dict[key] = value
    return th_eng_dict

# read_file_to_dict("th-eng-dict.tsv")
# print(read_file_to_dict("th-eng-dict.tsv"))

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
    token_list =[]
    position = 0
    length = len(sentence)

    while position < length:
        found = False
        for word_length in range (1, length-position + 1):
            thai_word = sentence[position:position+word_length]
            if thai_word in th_dict:
                translation, category, english_glosses = th_dict[thai_word]
                token_list.append((thai_word, translation, category, english_glosses))
                position += word_length
                found = True
                break

        if not found:
            position += 1
    return token_list

# th_eng_dict = read_file_to_dict("th-eng-dict.tsv")
# sentence = "ดาวอังคารเป็นดาวเคราะห์ลำดับที่สี่จากดวงอาทิตย์"

# xx = simple_tokenizer(th_eng_dict, sentence)
# print(xx[5])


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
    token_list = []
    tokens = simple_tokenizer(th_dict, sentence)
    for token in tokens:
        token_list.append(token[0])  
    print(token_list)
    return token_list
    
#tokens = th_tokens(read_file_to_dict("th-eng-dict.tsv"), "ดาวอังคารเป็นดาวเคราะห์ลำดับที่สี่จากดวงอาทิตย์")


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
    token_list = []
    tokens = simple_tokenizer(th_dict, sentence)
    for token in tokens:
        token_list.append(token[1])  
    print(token_list)
    return token_list
    
# tokens = th_translit(read_file_to_dict("th-eng-dict.tsv"), "ดาวอังคารเป็นดาวเคราะห์ลำดับที่สี่จากดวงอาทิตย์")




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
    token_list = []
    tokens = simple_tokenizer(th_dict, sentence)
    for token in tokens:
        token_list.append(token[2])  
    print(token_list)
    return token_list
    
# tokens = th_pos(read_file_to_dict("th-eng-dict.tsv"), "ดาวอังคารเป็นดาวเคราะห์ลำดับที่สี่จากดวงอาทิตย์")


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
    token_list = []
    tokens = simple_tokenizer(th_dict, sentence)
    for token in tokens:
        token_list.append(token[3])  
    print(token_list)
    return token_list

# tokens = th_gloss(read_file_to_dict("th-eng-dict.tsv"), "ดาวอังคารเป็นดาวเคราะห์ลำดับที่สี่จากดวงอาทิตย์")


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
    token_list = []
    position = 0
    length = len(sentence)

    while position < length:
        found = False
        for end in range(length, position, -1):
            thai_word = sentence[position:end]
            if thai_word in th_dict:
                translation, category, english_glosses = th_dict[thai_word]
                token_list.append((thai_word, translation, category, english_glosses))
                position = end  
                found = True
                break  

        if not found:
            position += 1

    return token_list

# tokens = greedy_tokenizer(read_file_to_dict("th-eng-dict.tsv"), "ดาวอังคารเป็น")
# print(tokens)


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
    token_list = []
    tokens = greedy_tokenizer(th_dict, sentence)
    for token in tokens:
        token_list.append(token[0])  
    print(token_list)
    return token_list

# tokens = th_tokens_greedy(read_file_to_dict("th-eng-dict.tsv"), "ดาวอังคารเป็น")
# print(tokens)


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
    token_list = []
    tokens = greedy_tokenizer(th_dict, sentence)
    for token in tokens:
        token_list.append(token[1])  
    print(token_list)
    return token_list

# tokens = th_translit_greedy(read_file_to_dict("th-eng-dict.tsv"), "ดาวอังคารเป็น")
# print(tokens)


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
    token_list = []
    tokens = greedy_tokenizer(th_dict, sentence)
    for token in tokens:
        token_list.append(token[2])  
    print(token_list)
    return token_list

# tokens = th_pos_greedy(read_file_to_dict("th-eng-dict.tsv"), "ดาวอังคารเป็น")
# print(tokens)




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
    token_list = []
    tokens = greedy_tokenizer(th_dict, sentence)
    for token in tokens:
        token_list.append(token[3])  
    print(token_list)
    return token_list

# tokens = th_gloss_greedy(read_file_to_dict("th-eng-dict.tsv"), "ดาวอังคารเป็น")
# print(tokens)
    pass

if __name__ == '__main__':
    file_name = "th-eng-dict.tsv"
    example = "ดาวอังคารเป็นดาวเคราะห์ลำดับที่สี่จากดวงอาทิตย์"
    pass