PLACE_HOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as name_file:
    recievers = name_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letters = letter_file.read()
    for name in recievers:
        stripped_name = name.strip()
        new_letter = letters.replace(PLACE_HOLDER, stripped_name)
        print(new_letter) 
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)