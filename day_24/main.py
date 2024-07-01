# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# Open names file and split lines into a list
with open("Input/Names/invited_names.txt") as names_data:
    names = (names_data.read()).splitlines()

with open("Input/Letters/starting_letter.txt") as template_data:
    template = template_data.read()

for name in names:
    letter = template.replace("[name]", name)
    with open(f"Output/ReadyToSend/{name}.txt", mode="w") as invite_data:
        invite_data.write(letter)
