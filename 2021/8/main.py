INPUT_FILE_1 = "input1.txt"
INPUT_FILE_2 = "input2.txt"


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

    return None


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