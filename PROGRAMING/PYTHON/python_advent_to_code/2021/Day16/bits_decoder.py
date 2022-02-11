## 1) the first three bits encode the packet [version]
## 2) the next three bits encode the packet [type ID]
## 3) These groups of five bits
##  These two values are numbers
## ~ Packets with type ID 4 represent a literal value
## [Broken into groups of four bits. Each group is prefixed by a 1 bit except
## the last group, which is prefixed by a 0 bit]

hex_dict = {'0': '0000', '1':'0001','2':'0010', '3':'0011', '4':'0100',
            '5':'0101', '6':'0110', '7':'0111', '8':'1000', '9':'1001',
            'A':'1010', 'B':'1011', 'C':'1100', 'D':'1101', 'E':'1110',
            'F':'1111'}

def load_file(fname):
    with open(fname) as f:
        return f.readline().rstrip()

def hex_to_binary(hex_number):
    return ''.join([hex_dict[ch] for ch in hex_number])

"""
ID 4: Paskutine forma ir nuskaiciuoja kas 5 bitus ir ksaito tik 4 paskutinius
galiojancius, visi like 0 gale nusiminusuoja
ID != 4: Ziuri pagal sekancia reiskme: Jei 0 tada nuskaiciuoji 15 bitu (paverti
i dec), kurie parodo visu kiek bitu uzima visi subsetai [nuskaiciuojam toki kieki bitu]
Jei 1 tada nuskaiciuojam 11 bitu(paverciam i dec), kurie pardodo kiek subestu
bus po 11 bitu nuskaiciuot.
"""
# def literal_value(binary_number):
#     version =
#     pass

def get_version_sum(binary_number, versions):
    version = binary_number[:3]
    type_id = binary_number[3:6]
    binary_number = binary_number[6:]


    if len(binary_number) == binary_number.count('0'): return versions

    versions += int(version, 2)

    if int(type_id, 2) != 4:
        length_type_id = binary_number[:1]
        binary_number = binary_number[1:]
        # print(f'Version: {int(version, 2)}')
        # print(f'Type ID: {int(type_id, 2)}')
        # print(f'Length Type ID: {int(length_type_id, 2)}')
        if length_type_id == '1':
            number_sub_packets = binary_number[:11]
            binary_number = binary_number[11:]
            # print(f'Number of packets: {int(number_sub_packets, 2)}')
            # print(f'Left binary number: {binary_number}')
            for _ in range(int(number_sub_packets, 2)):
                versions += get_version_sum(binary_number, versions)
        else:
            total_length_in_bits = binary_number[:15]
            binary_number = binary_number[15:]
            versions += get_version_sum(binary_number[:int(total_length_in_bits,2)],versions)

    else:
        while len(binary_number) != binary_number.count('0'):
            packet = binary_number[:5]
            binary_number = binary_number[5:]
            if packet[0] == '0':
                return versions
    #     print(f'Version: {int(version, 2)}')
    #     print(f'Type ID: {int(type_id, 2)}')


def get_factorial(number):
    if number == 1: return 1
    return number * get_factorial(number - 1)

def main():
    file = 'example_data'
    # hex_number = load_file(file)
    hex_number = '620080001611562C8802118E34'
    print(f'Hex number: {hex_number}')
    print(f'Binary hex number: {hex_to_binary(hex_number)}')

    # print(f'Factorial: {get_factorial(10)}')
    get_version_sum(hex_to_binary(hex_number), 0)

if __name__ == '__main__':
    main()
