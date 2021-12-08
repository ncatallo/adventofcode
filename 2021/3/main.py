INPUT_FILE_1 = "input1.txt"
INPUT_FILE_2 = "input2.txt"


def main():

    star1 = get_star_1(INPUT_FILE_1)
    print("Star 1 answer : " + str(star1))

    star2 = get_star_2(INPUT_FILE_2)
    print("Star 2 answer : " + str(star2))



def get_star_1(file):
    data = getLineFile(file)
    total_input = len(data)
    sums = []
    values_gamma = []
    values_epsilon = []
    bin_value_gamma = ""
    bin_value_epsilon = ""

    length_line = len(list(data[0]))
    for i in range(length_line):
        sums.append(0)

    for d in data:
        for index, val in enumerate(list(d)):
            if val == "1":
                sums[index] += 1

    for s in sums:
        if s > total_input/2:
            values_gamma.append("1")
            values_epsilon.append("0")
        else:
            values_gamma.append("0")
            values_epsilon.append("1")

    bin_value_gamma = "".join(values_gamma)
    bin_value_epsilon = "".join(values_epsilon)


    return int(bin_value_gamma, 2) * int(bin_value_epsilon, 2)



def get_star_2(file):
    data = getLineFile(file)

    oxygen_list = data
    co2_list = data

    oxygen_number = 0
    co2_number = 0

    oxygen_number = returnNumList(data, True)
    co2_number = returnNumList(data, False)

    return co2_number * oxygen_number


def returnNumList(data, most):

    data_list = data.copy()

    data_pattern = ""
    index_data = 0
    while len(data_list) > 1:

        total_input = len(data_list)

        sum_data = 0
        for d in data_list:
            values = list(d)

            if values[index_data] == "1":
                sum_data += 1

        if sum_data >= total_input/2:
            if most:
                data_pattern += "1"
            else:
                data_pattern += "0"
        else:
            if most:
                data_pattern += "0"
            else:
                data_pattern += "1"

        index_to_pop = []
        for index, d in enumerate(data_list):
            if d.startswith(data_pattern) == False:
                index_to_pop.append(index)

        shift = 0
        for i in index_to_pop:
            data_list.pop(i - shift)
            shift += 1

        index_data += 1

    return int(data_list[0], 2)


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