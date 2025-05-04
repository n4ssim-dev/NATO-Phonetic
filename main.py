import pandas

# Import le fichier csv & stock ses éléments dans un dict
file_df = pandas.read_csv('nato_phonetic_alphabet.csv')
file_dict = {row.letter:row.code for index,row in file_df.iterrows()}

# Selectionne le mot choisi par l'user et le converti en list phonetique, gere aussi les KeyError(nombre, symboles, etc...)
def prompt_user():
    try:
        user_input = input("Choose a word:\n").upper()
        user_dict = [file_dict[letter] for letter in user_input]
        print(user_dict)
    except KeyError as key_error:
        print(f"{key_error} is not a correct value.")
    finally:
        prompt_user()

prompt_user()
