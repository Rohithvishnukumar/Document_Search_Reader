 # doc = Document(file_path)
    # full_text = []
    # for para in doc.paragraphs:
    #     text = []
    #     for run in para.runs:
    #         text.append(run.text)
    #     full_text.append(''.join(text))
    # print('\n'.join(full_text))
    # return '\n'.join(full_text)


    # doc = Document(file_path)
    # extracted_text = []

    # for para in doc.paragraphs:
    #     paragraph_text = ""
    #     for run in para.runs:
    #         paragraph_text += run.text
        
    #     # Determine paragraph alignment
    #     alignment = para.alignment
    #     if alignment is None:  # Default to left alignment if not specified
    #         alignment = 'left'
        
    #     # Append paragraph text with alignment info
    #     extracted_text.append((paragraph_text, alignment))

    # return display_extracted_text(extracted_text)



# def display_extracted_text(extracted_text):
#     for text, alignment in extracted_text:
#         # Display text with the original alignment
#         if alignment == 'left':
#             print(text)
#         elif alignment == 'center':
#             print(text.center(80))  # Adjust width as needed
#         elif alignment == 'right':
#             print(text.rjust(80))  # Adjust width as needed
#         elif alignment == 'both' or alignment == 'justify':
#             # Justification can be complex; for simplicity, print left-aligned
#             print(text)

#         print() 







# s = "Rohith"

# for i ,s in enumerate(s):
#     print(i ,  " " , s )

# b = enumerate(s)

# print(list(b))
# print(tuple(b))
# print(dict(b))






# --- SPell checker

# import pkg_resources
# from symspellpy import SymSpell, Verbosity

# sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)
# dictionary_path = pkg_resources.resource_filename(
    # "symspellpy", "frequency_dictionary_en_82_765.txt")
# term_index is the column of the term and count_index is the
# column of the term frequency
# sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1)

# lookup suggestions for single-word input strings
# input_term = "storuns"
# max edit distance per lookup
# (max_edit_distance_lookup <= max_dictionary_edit_distance)
# suggestions = sym_spell.lookup(
#     input_term, Verbosity.CLOSEST, max_edit_distance=2, transfer_casing=True, include_unknown=True
# )
# display suggestion term, edit distance, and term frequency
# for suggestion in suggestions:
#     print(suggestion.term)

# print(suggestions[0].term)



# import random

# rand = random.random() * 1000000
# otp = int(rand)

# print(otp)


# data = {"plce": "kuiona"}

# print(data)

# # data = {
# #     "name" : "rohith"
# # }

# data.update({"name" : "pidj",
#              "ijfn" : 33 })

# print(data)



import os

file = "Test_Doc_01.docx"

os.remove(f"{file}.pdf")