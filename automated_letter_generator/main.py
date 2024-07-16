PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as invited_names:
    names = invited_names.readlines()
    print(names)

with open("./Input/Letters/starting_letter.txt") as starting_letter:
    letter_contents = starting_letter.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", "w") as completed_letters:
            completed_letters.write(new_letter)
