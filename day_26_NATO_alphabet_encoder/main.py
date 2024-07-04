import pandas

# TODO 1: create dictionary
# {"A": "Alfa", "B", "Beta"}
nato_abc_df = pandas.read_csv("./nato_phonetic_alphabet.csv")
nato_abc = {row.letter: row.code for (i, row) in nato_abc_df.iterrows()}

# TODO 2: Create a list of the phonetic code words
# from a word that the user inputs
word_to_spell = input("Which word would you like to be spelled phonetically? : ")
word_phony = [nato_abc[letter.upper()] for letter in word_to_spell]

print(word_phony)
