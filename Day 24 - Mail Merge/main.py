from pathlib import Path

name_list = []
with open("./Day 24 - Mail Merge/input/names/name_list.txt",mode="r") as names_in_file:
    for name in names_in_file.readlines():
        name_list.append(name.strip('\n'))


for name in name_list:
    output_file_path = Path(f"./Day 24 - Mail Merge/Output/ready_to_send/{name}_letter.txt")
    if output_file_path.exists():
        print(f"Letter for {name} exists.")
    else:
        with open("./Day 24 - Mail Merge/input/letter/starting_letter.txt",mode="r") as letter:
            for line in letter.readlines():
                with open(f"./Day 24 - Mail Merge/Output/ready_to_send/{name}_letter.txt",mode="a") as ready_to_send_letters:
                    if 'Dear [name],' in line:
                        ready_to_send_letters.write(f"Dear {name},\n")
                    else:
                        ready_to_send_letters.write(line)
       
                
