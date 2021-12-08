INPUT_FILE_1 = "input1.txt"
INPUT_FILE_2 = "input2.txt"


segment_equ = {}

ZERO = "abcefg"
ONE = "cf"
TWO = "acdeg"
THREE = "acdfg"
FOUR = "bcdf"
FIVE = "abdfg"
SIX = "abdefg"
SEVEN = "acf"
EIGHT = "abcdefg"
NINE = "abcdfg"

def main():

    star1 = get_star_1(INPUT_FILE_1)
    print("Star 1 answer : " + str(star1))

    star2 = get_star_2(INPUT_FILE_2)
    print("Star 2 answer : " + str(star2))



def get_star_1(file):
    data = getLineFile(file)
    
    digits_found = 0
    
    for d in data:
        patterns, digits = get_line_data(d)
        
        for digit in digits:
            if len(digit) == 2 or len(digit) == 3 or len(digit) == 4 or len(digit) == 7:
                digits_found += 1

    return digits_found





def get_star_2(file):
    data = getLineFile(file)
    
    sum_data = 0
    
    for d in data:
        patterns, digits = get_line_data(d)

        sum_data += decode_patterns(patterns, digits)

        
    return sum_data


def decode_patterns(patterns, digits):
    decoded_value = 0
    seg_equ = {}

    seg_equ['a'] = get_a_equivalent(patterns)
    seg_equ['g'] = get_g_equivalent(patterns, seg_equ['a'])
    seg_equ['e'] = get_e_equivalent(patterns, seg_equ['a'])
    seg_equ['d'] = get_d_equivalent(patterns, seg_equ['a'], seg_equ['g'])
    seg_equ['c'] = get_c_equivalent(patterns, seg_equ['a'], seg_equ['g'], seg_equ['d'], seg_equ['e'])
    seg_equ['f'] = get_f_equivalent(patterns, seg_equ['c'])
    seg_equ['b'] = get_b_equivalent(seg_equ)

    for digit in digits:
        decoded_digit = decode_digit(digit, seg_equ)
        decoded_value = decoded_value * 10 + decoded_digit

    return decoded_value


def decode_digit(digit, seg_equ):

    converted = ""

    for d in list(digit):
        for key in seg_equ.keys():
            if seg_equ[key] == d:
                converted += key

    if same_number(converted, ZERO):
        return 0

    if same_number(converted, ONE):
        return 1

    if same_number(converted, TWO):
        return 2

    if same_number(converted, THREE):
        return 3

    if same_number(converted, FOUR):
        return 4

    if same_number(converted, FIVE):
        return 5

    if same_number(converted, SIX):
        return 6

    if same_number(converted, SEVEN):
        return 7

    if same_number(converted, EIGHT):
        return 8

    if same_number(converted, NINE):
        return 9




def get_a_equivalent(patterns):
    seven = find_digit_pattern(patterns, 7)
    one = find_digit_pattern(patterns, 1)

    return find_differences(seven, one)[0]


def get_g_equivalent(patterns, a_equ):
    four = find_digit_pattern(patterns, 4)
    nine = find_digit_pattern(patterns, 9, a_equ)
    
    diffs = find_differences(four + a_equ, nine)

    return diffs[0]


def get_e_equivalent(patterns, a_equ):
    nine = find_digit_pattern(patterns, 9, a_equ)
    eight = find_digit_pattern(patterns, 8)
    
    diffs = find_differences(nine, eight)

    return diffs[0]


def get_d_equivalent(patterns, a_equ, g_equ):
    one = find_digit_pattern(patterns, 1)
    three = ""

    for pattern in patterns:
        if len(pattern) == 5:
            if len(find_differences(one + a_equ + g_equ, pattern)) == 1:
                three = pattern
                break

    diffs = find_differences(three, one + a_equ + g_equ)
    return diffs[0]


def get_c_equivalent(patterns, a_equ, g_equ, d_equ, e_equ):
    two = ""
    patt = a_equ + g_equ + d_equ + e_equ

    for pattern in patterns:
        if len(pattern) == 5:
            if len(find_differences(pattern, patt)) == 1:
                two = pattern

    return find_differences(patt, two)[0]


def get_f_equivalent(patterns, c_equ):
    one = find_digit_pattern(patterns, 1)

    for char in list(one):
        if char != c_equ:
            return char


def get_b_equivalent(seg_equ):
    chars = "abcdefg"

    for c in list(chars):
        if c not in seg_equ.values():
            return c



def find_differences(pattern1, pattern2):

    pattern1 = list(pattern1)
    pattern2 = list(pattern2)

    diffs = []

    if len(pattern1) < len(pattern2):
        pattern1, pattern2 = pattern2, pattern1

    for p1 in pattern1:
        found = False
        for p2 in pattern2:
            if p2 == p1:
                found = True
                break

        if found == False:
            diffs.append(p1)

    return diffs


# only for getting 1, 4, 7, 8
def find_digit_pattern(patterns, digit, a_equ = ""):

    for pattern in patterns:
        if(digit == 7) and len(pattern) == 3:
            return pattern

        elif digit == 1 and len(pattern) == 2:
            return pattern

        elif digit == 4 and len(pattern) == 4:
            return pattern

        elif digit == 8 and len(pattern) == 7:
            return pattern

        elif digit == 9 and len(pattern) == 6:
            four = find_digit_pattern(patterns, 4)

            for patter in patterns:
                if len(patter) == 6:
                    if len(find_differences(four + a_equ, patter)) == 1:
                        return patter

        elif digit == 0 and len(pattern) == 6:
            eight = find_digit_pattern(pattern, 8)

            if len(find_differences(eight, pattern)) == 1:
                return pattern



def same_number(pattern1, pattern2):
    if len(pattern1) != len(pattern2):
        return False
        
    if ''.join(sorted(pattern1)) == ''.join(sorted(pattern2)):
        return True

    return False



def get_line_data(data):
    first, second = data.split(" | ")
    
    return first.split(" "), second.split(" ")


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