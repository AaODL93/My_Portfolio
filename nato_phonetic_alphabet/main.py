import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")

phonetic_dictionary = {row.letter: row.code for (index, row) in data.iterrows()}

word = input("Enter a word: ").upper()
result = [phonetic_dictionary[letter] for letter in word if letter in phonetic_dictionary]
print(f"Phonetic code = {result}")
