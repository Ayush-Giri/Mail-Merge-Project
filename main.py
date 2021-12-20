# People to be invited

with open("Input/Names/invited_names.txt", mode="r") as names_file:
    people_name = names_file.readlines()
    people_name_list = []
    for name in people_name:
        people_name_list.append(name.strip("\n"))


# Reading the sample letter

with open("Output/ReadyToSend/example.txt", mode="r") as sample:
    sample_letter = sample.readlines()


# Creating letters for each person

for name in people_name_list:
    with open(f"Output/ReadyToSend/{name}.txt", mode="w") as invitation:
        final_message = []
        for message in sample_letter:
            if sample_letter.index(message) == 0:
                final_message.append(f"Dear {name},\n")

            elif sample_letter.index(message) == len(sample_letter) - 1:
                final_message.append("Ayush")

            else:
                final_message.append(message)

    with open(f"Output/ReadyToSend/{name}.txt", mode="a") as invitation:
        for words in final_message:
            invitation.write(words)





