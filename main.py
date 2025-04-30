import pandas

# Import le fichier csv & stock ses éléments dans un dict
file_df = pandas.read_csv('nato_phonetic_alphabet.csv')
file_dict = {row.letter:row.code for index,row in file_df.iterrows()}

# Prend en compte l'user input et créer un dict comprenant comme key les lettres du mot et en value le mot associé en NATO Phonetic
user_input = input("Choose a word:\n").upper()
user_dict = {letter: file_dict[letter] for letter in user_input if letter in file_dict}
print(user_dict)