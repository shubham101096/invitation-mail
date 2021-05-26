with open("Input/Names/invited_names.txt") as file:
    names = file.readlines()

with open("Input/Letters/starting_letter.txt") as starting_letter:
    for name in names:
        letter = starting_letter.read()
        new_letter = letter.replace("[name]", name.strip())
        with open(f"Output/ReadyToSend/letterfor{name.strip()}.txt", "w") as file:
            file.write(new_letter)



