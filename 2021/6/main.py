INPUT_FILE_1 = "input1.txt"
INPUT_FILE_2 = "input2.txt"


def main():

    star1 = get_star_1(INPUT_FILE_1)
    print("Star 1 answer : " + str(star1))

    star2 = get_star_2(INPUT_FILE_2)
    print("Star 2 answer : " + str(star2))



def get_star_1(file):
    data = getLineFile(file)

    fishes = data[0].split(",")
    fishes = [int(x) for x in fishes]

    nb_days = 80

    while nb_days > 0:

        added_list = []

        #print(fishes)

        for index, fish in enumerate(fishes):
            if fish == 0:
                fishes[index] = 6
                added_list.append(8)
            else:
                fishes[index] -= 1

        fishes += added_list

        nb_days -= 1

    return len(fishes)



def get_star_2(file):
    data = getLineFile(file)

    fishes = data[0].split(",")
    fishes = [int(x) for x in fishes]

    fishes_dict = {}
    for fish in fishes:
        fishes_dict[fish] = fishes_dict.get(fish, 0) + 1

    nb_days = 256
    count = 0

    while nb_days > 0:
        copy = {}

        for fish_key in fishes_dict.keys():

            if fish_key > 0:

                copy[fish_key-1] = copy.get(fish_key-1, 0) + fishes_dict.get(fish_key, 0)

            elif fish_key == 0:

                copy[6] = copy.get(6, 0) + fishes_dict.get(fish_key, 0)
                copy[8] = fishes_dict.get(fish_key)


        fishes_dict = copy

        nb_days -= 1


    for key in fishes_dict.keys():
        count += fishes_dict[key]


    return count


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