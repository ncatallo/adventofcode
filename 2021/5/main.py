INPUT_FILE_1 = "input1.txt"
INPUT_FILE_2 = "input2.txt"


def main():

    star1 = get_star_1(INPUT_FILE_1)
    print("Star 1 answer : " + str(star1))

    star2 = get_star_2(INPUT_FILE_2)
    print("Star 2 answer : " + str(star2))



def get_star_1(file):
    data = getLineFile(file)

    data_lines = {}

    for d in data:
        x1, y1, x2, y2 = get_values_line(d)

        # only lines
        if x1 == x2 or y1 == y2:
            points = get_points_from_values(x1, y1, x2, y2)

            for point in points:
                key = str(point[0]) + "_" + str(point[1])
                dict_value = data_lines.get(key, None)

                if dict_value is None:
                    data_lines[key] = 1
                else:
                    data_lines[key] += 1

    count = 0
    for k in data_lines.keys():
        if data_lines[k] >= 2:
            count += 1

    return count



def get_star_2(file):
    data = getLineFile(file)

    data_lines = {}

    for d in data:
        x1, y1, x2, y2 = get_values_line(d)

        points = get_points_from_values(x1, y1, x2, y2)

        for point in points:
            key = str(point[0]) + "_" + str(point[1])
            dict_value = data_lines.get(key, None)

            if dict_value is None:
                data_lines[key] = 1
            else:
                data_lines[key] += 1

    count = 0
    for k in data_lines.keys():
        if data_lines[k] >= 2:
            count += 1

    return count


def get_points_from_values(x1, y1, x2, y2):

    points = []

    if x1 == x2 or y1 == y2:
        for x in range(min(x1, x2), max(x2, x1) + 1):
            for y in range(min(y1, y2), max(y2, y1) + 1):
                points.append([
                    x, y
                ])
    else:

        if x1 > x2:
            x1, y1, x2, y2 = x2, y2, x1, y1

        slope = 0
        if y2 < y1:
            slope = -1
        else:
            slope = 1

        for i in range(x2 - x1 + 1):
            points.append([
                x1 + i,
                y1 + i*slope
            ])

    return points




def get_values_line(line):
    point1, point2 = line.split("->")
    point1 = point1.strip()
    point2 = point2.strip()
    
    x1, y1 = point1.split(",")
    x2, y2 = point2.split(",")

    return [int(x1), int(y1), int(x2), int(y2)]


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