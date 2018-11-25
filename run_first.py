from code_to_address import instruct_address_dict

def run_file(content):
    current_address = 0

    if 'ORG' in content[0]:
        new_content = content[0].strip()
        new_content = new_content[3:]
        new_content = new_content.lstrip()
        new_content = new_content[:-1]
        current_address = int(new_content, 16)

        content = content[1:]

    for line in content:
        line = line.replace('\n', '')
        line = line.lstrip()

        if 'DEC' in line and 'R' in line:     
            current_address += 1
        
        elif 'XRL' in line and 'A' in line and 'R' in line:
            current_address += 1

        elif 'LJMP' in line:
            current_address += 3

        elif 'DJNZ' in line and 'R' not in line:
            current_address += 3


        elif 'MOV' in line and '#' in line and 'H' in line:
            current_address += 2


        elif 'MOV' in line and 'A' in line and line[-1] != 'A':
            current_address += 2

        elif 'MOV' in line and 'A' in line and line[-1] == 'A':
            current_address += 2

        elif 'MOV' in line and 'R' in line:
            current_address += 2

        elif 'NOP' in line:                                     # see if line match NOP
            current_address += 1

        instruct_address_dict[line] = current_address