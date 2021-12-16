INPUT_FILE_1 = "input1.txt"
INPUT_FILE_2 = "input2.txt"


equ_bin_hex = {
    '0' : '0000',
    '1' : '0001',
    '2' : '0010',
    '3' : '0011',
    '4' : '0100',
    '5' : '0101',
    '6' : '0110',
    '7' : '0111',
    '8' : '1000',
    '9' : '1001',
    'A' : '1010',
    'B' : '1011',
    'C' : '1100',
    'D' : '1101',
    'E' : '1110',
    'F' : '1111'
}

def main():

    star1 = get_star_1(INPUT_FILE_1)
    print("Star 1 answer : " + str(star1))

    star2 = get_star_2(INPUT_FILE_2)
    print("Star 2 answer : " + str(star2))



def get_star_1(file):
    data = getLineFile(file)[0]
    bin_data = "".join([equ_bin_hex[c] for c in data])

    packet = parse_bin_data(bin_data)

    value = add_versions_packet(packet)

    return value


def get_star_2(file):
    data = getLineFile(file)[0]


    bin_data = "".join([equ_bin_hex[c] for c in data])

    packet = parse_bin_data(bin_data)
    value = apply_operator_packet(packet)

    return value


def apply_operator_packet(packet):
    value = 0
    id = packet["type_id"]

    if id == 0:
        for submodule in packet["submodules"]:
            value += apply_operator_packet(submodule)

    elif id == 1:
        value = 1
        for submodule in packet["submodules"]:
            value *= apply_operator_packet(submodule)

    elif id == 2:
        min = float('inf')
        for submodule in packet["submodules"]:
            value_sub = apply_operator_packet(submodule)
            if value_sub < min:
                min = value_sub
        value = min

    elif id == 3:
        max = 0
        for submodule in packet["submodules"]:
            value_sub = apply_operator_packet(submodule)
            if value_sub > max:
                max = value_sub
        value = max
    
    elif id == 5:
        sub_1 = apply_operator_packet(packet["submodules"][0])
        sub_2 = apply_operator_packet(packet["submodules"][1])
        if sub_1 > sub_2:
            value = 1
        else:
            value = 0

    elif id == 6:
        sub_1 = apply_operator_packet(packet["submodules"][0])
        sub_2 = apply_operator_packet(packet["submodules"][1])
        if sub_1 < sub_2:
            value = 1
        else:
            value = 0

    elif id == 7:
        sub_1 = apply_operator_packet(packet["submodules"][0])
        sub_2 = apply_operator_packet(packet["submodules"][1])
        if sub_1 == sub_2:
            value = 1
        else:
            value = 0

    elif id == 4:
        value = packet["value"]

    return value


def add_versions_packet(packet):
    sum = int(packet["version"])

    for submodule in packet.get("submodules", []):
        sum += add_versions_packet(submodule)

    return sum



def parse_bin_data(bin_data):

    packet = {
        "bit_length" : 0,
        "version" : int(bin_data[0:3], 2),
        "type_id" : int(bin_data[3:6], 2)
    }

    if packet["type_id"] == 4:
        start_index = 6
        end_of_value = False
        current_value = ""

        while end_of_value == False:
            if bin_data[start_index] == "0":
                end_of_value = True
    
            current_value += bin_data[start_index+1:start_index+5]
            start_index += 5

        packet["bit_length"] = start_index
        packet["value"] = int(current_value, 2)

    else:
        packet["submodules"] = []
        length_type_id = bin_data[6]

        if length_type_id == "0":
            total_length = 7+15
            length_bits = int(bin_data[7:7+15], 2)
            packet_start = 7+15

            while True:
                packet_recursive = parse_bin_data(bin_data[packet_start:packet_start+length_bits])

                packet["submodules"].append(
                    packet_recursive
                )

                total_length += packet_recursive["bit_length"]
                packet_start += packet_recursive["bit_length"]
                length_bits -= packet_recursive["bit_length"]

                if length_bits <= 0:
                    break

            packet["bit_length"] = total_length
        else:
            total_length = 7+11
            num_subpacket = int(bin_data[7:7+11], 2)
            packet_start = 7+11

            while num_subpacket > 0:
                packet_recursive = parse_bin_data(bin_data[packet_start:])

                packet["submodules"].append(
                    packet_recursive
                )

                total_length += packet_recursive["bit_length"]
                packet_start += packet_recursive["bit_length"]
                num_subpacket -= 1

            packet["bit_length"] = total_length


    return packet



def getLineFile(file):
    lines = []

    with open(file, 'r') as f:
        lines = f.read().split('\n')

    for index, line in enumerate(lines):
        if line == "" or line == "\n" or line is None or line == "\r\n":
            lines.pop(index)

    return lines

if __name__ == "__main__":
    main()