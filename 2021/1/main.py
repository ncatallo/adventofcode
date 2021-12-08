INPUT_FILE_1 = "input1.txt"
INPUT_FILE_2 = "input2.txt"


def main():

    star1 = get_star_1(INPUT_FILE_1)
    print("Star 1 answer : " + str(star1))

    star2 = get_star_2(INPUT_FILE_2, 3)
    print("Star 2 answer : " + str(star2))



def get_star_2(file, slide = 3):
    data = getLineFile(file)

    previous = None
    larger_to_previous_count = 0

    for index, current_data in enumerate(data):

        if index > len(data) - slide:
            break

        current_sum = 0
        for i in range(index, index + slide):
            current_sum += int(data[i])

        if(previous is not None):
            if current_sum > previous:
                larger_to_previous_count += 1

        previous = current_sum

    return larger_to_previous_count


def get_star_1(file):
    data = getLineFile(file)

    previous = None
    larger_to_previous_count = 0

    for current_data in data:
        current_data = int(current_data)

        if(previous is not None):
            if current_data > previous:
                larger_to_previous_count += 1

        previous = current_data

    return larger_to_previous_count



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