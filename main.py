with open("Input/Names/invited_names.txt") as file:
    names = file.readlines()

print(names)

for name in names:
    with open("Input/Letters/starting_letter.txt") as starting_letter:
        letter = starting_letter.read()
        print(name)
        new_letter = letter.replace("[name]", name.strip())
        print(letter)
        print(new_letter)
        with open(f"Output/ReadyToSend/letterfor{name.strip()}.txt", "w") as file:
            file.write(new_letter)
