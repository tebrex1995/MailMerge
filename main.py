PLACEHOLDER = "[name]"

#Extract names of the invited people
with open("Input/Names/invited_names.txt") as i:
    invited_names = i.readlines()
#Loop through extracted names
for n in invited_names:
    #Read starting letter template
    with open("Input/Letters/starting_letter.txt") as l:
        starting_letter = l.read()
        #Write letter for each name extracted
        with open(f"Output/ReadyToSend/{n.strip()}", mode="w") as nl:
            stripped_name = n.strip()
            nl.write(f"{starting_letter.replace(PLACEHOLDER, stripped_name)}")





