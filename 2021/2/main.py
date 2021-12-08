INPUT_FILE_1 = "input1.txt"
INPUT_FILE_2 = "input2.txt"


def main():

    star1 = get_star_1(INPUT_FILE_1)
    print("Star 1 answer : " + str(star1))

    star2 = get_star_2(INPUT_FILE_2)
    print("Star 2 answer : " + str(star2))



def get_star_1(file):
    data = getLineFile(file)

    horizontal_position = 0
    depth_position = 0

    for d in data:
        action, value = d.split(" ")

        if action == "forward":
            horizontal_position += int(value)
        elif action == "up":
            depth_position -= int(value)
        elif action == "down":
            depth_position += int(value)

    multiply_position = horizontal_position * depth_position

    print("Horizontal : " + str(horizontal_position))
    print("Depth : " + str(depth_position))

    return multiply_position



def get_star_2(file):
    data = getLineFile(file)

    horizontal_position = 0
    depth_position = 0
    aim = 0

    for d in data:
        action, value = d.split(" ")

        if action == "forward":
            horizontal_position += int(value)
            depth_position += aim * int(value)
        elif action == "up":
            aim -= int(value)
        elif action == "down":
            aim += int(value)

    multiply_position = horizontal_position * depth_position

    print("Horizontal : " + str(horizontal_position))
    print("Depth : " + str(depth_position))

    return multiply_position




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