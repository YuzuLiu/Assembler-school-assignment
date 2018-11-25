from instructions import *
from code_to_address import *
import run_first
import sys, os

def main():
    current_address = 0
#    instruct_address_dict = {}
    content = []
    output_content = ""
    print("What is your filename? (with file format)")
    filename = input()
    file_content = open(os.path.join(sys.path[0], str(filename)))
#    file_content = open(str(filename), "r")                   # open file
    content = file_content.readlines()                        # split each lines and store in a list

    run_first.run_file(content)

    if 'ORG' in content[0]:
        new_content = content[0].strip()
        new_content = new_content[3:]
        new_content = new_content.strip()
        new_content = new_content[:-1]
        current_address = int(new_content, 16)

        content = content[1:]

    for line in content:
        line = line.replace('\n', '')
        line = line.lstrip()

        if 'DEC' in line and 'R' in line:     
            R_index = line.find('R')
            direct_address = line[R_index] + line[R_index + 1]
            output_content += DEC_Rn_table.get(direct_address)

            current_address += 1
        
        elif 'XRL' in line and 'A' in line and 'R' in line:     
            direct_address = line[-2] + line[-1]

            output_content += str(XRL_A_Rn_table.get(direct_address))

            current_address += 1

        elif 'LJMP' in line:
            line = line[4:]
            destination_name = line.lstrip()
            destination_name += ":"
            destination_address = instruct_address_dict[destination_name]
            output_content += LJMP_addr16_table(destination_address)

            current_address += 3

        elif 'DJNZ' in line and 'R' not in line:
            if 'H' in line:
                H_index = line.find('H')
                direct_address = line[H_index - 2] + line[H_index - 1]
            elif 'P' in line:
                P_index = line.find('P')
                direct_address = line[P_index] + line[P_index + 1]

            comma_index = line.find(',')
            function_name = line[comma_index + 1 :]
            function_name = function_name + ':'
            function_address = instruct_address_dict[function_name]

            print(function_address)
            print(current_address)

            output_content += DJNZ_direct_offset(direct_address, current_address, function_address)
            current_address += 3


        elif 'MOV' in line and '#' in line and 'H' in line:
            hashtag_index = line.find('#')
            H_index = line.find('H')
            if line[hashtag_index + 1] == 0 and line[hashtag_index + 2] == None:
                immed = '00'
            else:
                immed = line[hashtag_index + 1 : H_index]

            if immed[0] == '0':
                immed = immed[1:]

            output_content += mov_A_immed(immed)

            current_address += 2


        elif 'MOV' in line and 'A' in line and line[-1] != 'A':
            if 'H' in line:
                H_index = line.find('H')
                direct_address = line[H_index - 2] + line[H_index - 1]
            elif 'P' in line:
                P_index = line.find('P')
                direct_address = line[P_index] + line[P_index + 1]

            output_content += mov_A_direct(direct_address)

            current_address += 2

        elif 'MOV' in line and 'A' in line and line[-1] == 'A':
            if 'H' in line:
                H_index = line.find('H')
                direct_address = line[H_index - 2] + line[H_index - 1]
            elif 'P' in line:
                P_index = line.find('P')
                direct_address = line[P_index] + line[P_index + 1]

            output_content += mov_direct_A(direct_address)

            current_address += 2

        elif 'MOV' in line and 'R' in line:
            if 'H' in line:
                H_index = line.find('H')
                direct_address = line[H_index - 2] + line[H_index - 1]
            elif 'P' in line:
                P_index = line.find('P')
                direct_address = line[P_index] + line[P_index + 1]

            R_index = line.find('R')
            rn = line[R_index] + line[R_index + 1]

            output_content += mov_Rn_direct(rn, direct_address)

            current_address += 2

        elif 'NOP' in line:                                     # see if line match NOP
            output_content += nop()

            current_address += 1

#        instruct_address_dict[line] = current_address

    output_content = output_content.strip()                   # remove extra whitespace

    file_content.close()                                      # close file

    filename = filename[:-4]
    new_file = open(filename + "-output.txt", "w")            # open new file
    print("Creating output file " + filename + " ...")
    new_file.write(output_content)
    print("Writing machine code ...")
    new_file.close()
    print("Finished! Please check your output file in the same directory.")

main()
input()