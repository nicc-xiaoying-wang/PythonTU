import pickle
import itertools

"""
Python 2023 Assignment 04
"""

# IMPORTANT: assign the parts of your name and your student ID to these variables!
first_name = "Xiaoying"
family_name = "Wang"
student_id = "6802277"

import pickle


def read_dict(file_name):
    """
    IMPORTANT! You don't have to change anything
    in this helper function.

    Read a dictionary from a pickled file.

    :param file_dir: directory of a pickled file
    :type file_dir: str
    :return: dictionary
    :rtype: dict
    """
    with open(file_name, 'rb') as handle:
        return pickle.load(handle)


#
# def read_dict(file_name):
#     with open(file_name, 'rb') as file:
#         ind_eng_dict = pickle.load(file)
#     return ind_eng_dict


def tokenize(sentence):
    """
    IMPORTANT! You don't have to change anything
    in this helper function.

    Tokenize the sentence into tokens (words, punctuation).

    :param sentence: sentence to be split.
    :type sentence: str
    :return: list of tokens
    :rtype: list(str)
    """
    tokens = []

    for word in sentence.split():
        if word[-1] in ".,!?;":
            tokens.extend([word[:-1], word[-1]])
        else:
            tokens.append(word)

    return tokens


def translate_ind_eng(sentence, lang_dict):
    translated_sentence = []
    s = read_dict(lang_dict)
    words = tokenize(sentence)

    for i, word in enumerate(words):
        punctuation = ''
        if word[-1] in ".,!?;":
            punctuation = word[-1]
            words[i] = word[:-1]

        translated_word = s.get(words[i], words[i])
        translated_sentence.append(translated_word)

        # Add space if the next word exists and it's not a punctuation mark
        if i < len(words) - 1 and words[i + 1][-1] not in ".,!?;":
            translated_sentence.append(' ')

        translated_sentence.append(punctuation)

    final_sentence = ''.join(translated_sentence)
    return final_sentence


    pass

#translate_ind_eng("ibu dan ayah saya tidak di rumah sekarang.", "ind_eng_dict.pickle")

# translated_sentence = translate_ind_eng("ibu dan ayah saya tidak di rumah sekarang.", "ind_eng_dict.pickle")
# #print(translated_sentence)

def build_data_structure(sentence, lang_dict):
    tokens = tokenize(sentence)
    data_nest = []
    ind_eng_dict = read_dict(lang_dict)

    for token in tokens:
        if token in ind_eng_dict:
            translated_token = ind_eng_dict[token].split('/')
            data_nest.append((token, translated_token))
    return data_nest

    """
    Tokenize and create a data structure which contains a tokenization

    of the Indonesian input sentence with glosses in English.
    The function needs to ignore punctuation.
    """
    pass

#build_data_structure("ibu dan ayah saya tidak di rumah sekarang.","ind_eng_dict.pickle")

def get_possible_glosses(sentence, lang_dict):
    """
    Get all the possible glosses.
    """

    # --------------- write and edit the code only in the block below ---------------
    data_str = build_data_structure(sentence, lang_dict)
    ind_eng_dict = read_dict(lang_dict)

    # TODO: retrieve Indonesian words and their English translations from data_str
    ind_words = [item[0] for item in data_str]
    eng_trans1 = [item[1][0] if len(item[1]) > 0 else " " for item in data_str]
    eng_trans2 = [item[1][1] if len(item[1]) > 1 else " " for item in data_str]
    # print(ind_words)
    # print(eng_trans1)
    # print(eng_trans2)

    # TODO: get the number of columns for the matrix
    n_columns = len(ind_words)
    # TODO: get the number of rows for the matrix
    n_rows = 3

    # initialize the matrix. IMPORTANT! You should not change anything in this line.
    matrix = [["" for column in range(n_columns)] for row in range(n_rows)]

    # TODO: create a nested for loop which fill in the matrix
    for i, (word, trans1, trans2) in enumerate(zip(ind_words, eng_trans1, eng_trans2)):
        matrix[0][i] = word
        matrix[1][i] = trans1
        matrix[2][i] = trans2

    # --------------- write and edit the code only in the block above ---------------
    possible_glosses = [list(ind_words)] + matrix
    # merge Indonesian sentence with its possible translations
    print(possible_glosses)
    return possible_glosses


get_possible_glosses("ibu dan ayah saya tidak di rumah sekarang.", "ind_eng_dict.pickle")


def print_possible_glosses(possible_glosses):
    """
    Helper method.
    Print the output of get_possible_glosses function.

    :param possible_glosses: output of get_possible_glosses() function
    :type possible_glosses: list(list(str))
    """
    n_columns = len(possible_glosses[0])

    # create a template for the output
    output_template = "{:<10s}" * n_columns

    matrix = [output_template.format(*row) for row in possible_glosses]

    for row in matrix:
        return row

    return matrix


def get_all_translations(sentence, lang_dict):
    """
    Get all the possible translations of the Indonesian sentence to English.

    :param sentence: Indonesian sentence
    :type sentence: str
    :param lang_dict: dictionary with word translations from Indonesian to English
    :type lang_dict: dict{str: list[str]}
    :return: list of all possible translations
    :rtype: list[str]
    """
    translate_sentence = build_data_structure(sentence, lang_dict)

    translations = [item[1] for item in translate_sentence]
    cartesian_product = list(itertools.product(*translations))
    all_sentences = [" ".join(i) for i in cartesian_product]

    print(all_sentences)

    pass

#get_all_translations("ibu dan ayah saya tidak di rumah sekarang.", "ind_eng_dict.pickle")

if __name__ == '__main__':
    example = "ayah saya tidak di rumah sekarang."
    ind_eng_dict = read_dict("ind_eng_dict.pickle")
