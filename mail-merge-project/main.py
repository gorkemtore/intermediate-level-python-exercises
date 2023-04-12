#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("./mail-merge-project/Input/Letters/starting_letter.txt") as mail:
    lines = mail.readlines()

with open("./mail-merge-project/Input/Names/invited_names.txt") as invited_names:
    names = invited_names.readlines()

for i in range(0, len(names)):

    name = names[i].split("\n")[0]
    first_raw = lines[0].split("[")
    first_raw = first_raw[0] + first_raw[1].replace("name]", name)

    new_mail = [first_raw]
    for line in lines[1:]:
        new_mail.append(line)

    with open (f"./mail-merge-project/Output/ReadyToSend/{name}.txt" ,"w") as send_mail:
        send_mail.writelines(new_mail)
