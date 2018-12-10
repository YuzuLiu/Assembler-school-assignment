DEC_Rn_table = {
    'R0' : '18\n',
    'R1' : '19\n',
    'R2' : '1A\n',
    'R3' : '1B\n',
    'R4' : '1C\n',
    'R5' : '1D\n',
    'R6' : '1E\n',
    'R7' : '1F\n'
}

XRL_A_Rn_table = {
    'R0' : '68\n',
    'R1' : '69\n',
    'R2' : '6A\n',
    'R3' : '6B\n',
    'R4' : '6C\n',
    'R5' : '6D\n',
    'R6' : '6E\n',
    'R7' : '6F\n'
}

def LJMP_addr16_table(address):
    hex_address = hex(address)
    hex_address = hex_address.upper()
    hex_address = hex_address[2:]
    return '02 ' + str(hex_address[:2]) + " " + str(hex_address[2:]) + '\n'

def DJNZ_direct_offset(direct, current_address, function_address):
    
    offset_dec = function_address - current_address - 3
    
    offset = tohex(offset_dec, 8)[2:]
    offset = str(offset).zfill(2)
    offset = offset.upper()

    if direct == 'P0':
        address = 'D5 80'
    elif direct == 'P1':
        address = 'D5 90'
    elif direct == 'P2':
        address = 'D5 A0'
    elif direct == 'P3':
        address = 'D5 B0'
    else:
        address = 'D5 ' + str(direct)

    return address + " " + offset + '\n'

def mov_A_immed(immed):
    return '74 ' + str(immed) + '\n'

def mov_A_direct(direct):
    if direct == 'P0':
        return 'E5 80\n'
    elif direct == 'P1':
        return 'E5 90\n'
    elif direct == 'P2':
        return 'E5 A0\n'
    elif direct == 'P3':
        return 'E5 B0\n'
    else:
        return 'E5 ' + direct + '\n'

def mov_direct_A(direct):
    if direct == 'P0':
        return 'F5 80\n'
    elif direct == 'P1':
        return 'F5 90\n'
    elif direct == 'P2':
        return 'F5 A0\n'
    elif direct == 'P3':
        return 'F5 B0\n'
    else:
        return 'F5 ' + str(direct) + '\n'

def mov_Rn_direct(rn, direct):
    if rn == 'R0':
        return 'A8 ' + str(direct) + '\n'
    elif rn == 'R1':
        return 'A9 ' + str(direct) + '\n'
    elif rn == 'R2':
        return 'AA ' + str(direct) + '\n'
    elif rn =='R3':
        return 'AB ' + str(direct) + '\n'
    elif rn == 'R4':
        return 'AC ' + str(direct) + '\n'
    elif rn == 'R5':
        return 'AD ' + str(direct) + '\n'
    elif rn == 'R6':
        return 'AE ' + str(direct) + '\n'
    elif rn == 'R7':
        return 'AF ' + str(direct) + '\n'

def nop():
    return '00\n' 

def tohex(val, nbits):
  return hex((val + (1 << nbits)) % (1 << nbits))
