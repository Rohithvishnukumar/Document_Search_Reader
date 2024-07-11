# import pkg_resources
# from symspellpy import SymSpell, Verbosity
# import string

# spellDic = {}   # initialize empty dictionary 

# text = " 'Python' but Hello. Foru mes it is nota goood"

# def spellCheck(text):
#     sym_spell = SymSpell(max_dictionary_edit_distance=3, prefix_length=7)
#     dictionary_path = pkg_resources.resource_filename("symspellpy", "frequency_dictionary_en_82_765.txt")
#     sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1)

#     input_terms = separate_words(text)  # Separate words from text

#     for input_term in input_terms:
#         suggestions = sym_spell.lookup(input_term, Verbosity.CLOSEST, max_edit_distance=2, transfer_casing=True, include_unknown=True)

#         if len(suggestions) > 0 and input_term != suggestions[0].term:
#             if input_term not in spellDic.values():
#                 if spellDic:
#                     last_key = max(spellDic.keys()) + 1
#                 else:
#                     last_key = 0
#                 spellDic[last_key] = input_term

#         print(spellDic)

# def separate_words(text):
#     # Remove punctuation (including apostrophes)
#     translator = str.maketrans('', '', string.punctuation)
#     clean_text = text.translate(translator)
    
#     # Split the text into words
#     words = clean_text.split()
#     return words

# spellCheck(text)


















import pkg_resources
from symspellpy import SymSpell, Verbosity
import string

spellDic = {}   # initialize empty dictionary 

text = " 'Python' but Hello. Foru mes it is nota goood"

def spellCheck(text):
    sym_spell = SymSpell(max_dictionary_edit_distance=3, prefix_length=7)
    dictionary_path = pkg_resources.resource_filename("symspellpy", "frequency_dictionary_en_82_765.txt")
    sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1)

    input_terms = separate_words(text)  # Separate words from text

    for input_term in input_terms:
        suggestions = sym_spell.lookup(input_term, Verbosity.CLOSEST, max_edit_distance=2, transfer_casing=True, include_unknown=True)

        if len(suggestions) > 0 and input_term != suggestions[0].term:
            if input_term not in spellDic.values():
                if spellDic:
                    last_key = max(spellDic.keys()) + 1
                else:
                    last_key = 0
                spellDic[last_key] = input_term

        print(spellDic)

def separate_words(text):
    # Remove punctuation (including apostrophes)
    translator = str.maketrans('', '', string.punctuation)
    clean_text = text.translate(translator)
    
    # Split the text into words
    words = clean_text.split()
    return words

spellCheck(text)












