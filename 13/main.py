INPUT_FILE_1 = "input1.txt"
INPUT_FILE_2 = "input2.txt"


def main():

    star1 = get_star_1(INPUT_FILE_1)
    print("Star 1 answer : " + str(star1))

    star2 = get_star_2(INPUT_FILE_2)
    print("Star 2 answer : " + str(star2))



def get_star_1(file):
    data, foldings = getLineFile(file)
    matrix = convert_data_to_matrix(data)

    for folding in foldings:
        matrix = fold_matrix(matrix, folding)
        break
    
    count = 0
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if matrix[y][x] == "#":
                count += 1

    return count



def get_star_2(file):
    data, foldings = getLineFile(file)
    matrix = convert_data_to_matrix(data)

    for folding in foldings:
        matrix = fold_matrix(matrix, folding)
    
    count = 0
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if matrix[y][x] == "#":
                count += 1

    return count


def fold_matrix(matrix, folding):

    if folding.get("x", None) is not None:
        fold_index = folding.get("x", None)

        copy = [row[fold_index + 1:] for row in matrix]
        copy = reverse_matrix(copy, False)

        for y in range(len(copy)):
            for x in range(len(copy[0])):
                
                if copy[y][x] == "#":
                    matrix[y][x] = "#"

        matrix = [row[:fold_index] for row in matrix]
        

    elif folding.get("y", None) is not None:
        fold_index = folding.get("y", None)

        copy = matrix[fold_index + 1:][:]
        copy = reverse_matrix(copy, True)

        for y in range(len(copy)):
            for x in range(len(copy[0])):
                
                if copy[y][x] == "#":
                    matrix[y][x] = "#"

        matrix = matrix[:fold_index][:]
    

    return matrix


def reverse_matrix(matrix, lines = True):

    if lines:
        # Easy with lines because in arrray
        matrix.reverse() 
        return matrix
    else:
        new_matrix = []

        # on columns need to do it manually
        for i in range(len(matrix)):
            new_matrix.append(matrix[i][::-1])

        return new_matrix



def convert_data_to_matrix(data):
    matrix = []

    xMax, yMax = 0, 0
    for line in data:
        x, y = line.split(",")
        x = int(x)
        y = int(y)
        if x > xMax:
            xMax = x
        if y > yMax:
            yMax = y

    for j in range(yMax+1):
        matrix.append([])

        for i in range(xMax+1):
            matrix[j].append(".")

    for line in data:
        x, y = line.split(",")
        x = int(x)
        y = int(y)

        matrix[y][x] = "#"

    return matrix




def printMatrix(matrix, charSize = 1):

    print("")
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if charSize == 1:
                print(matrix[i][j], end = "")
            else:
                need = charSize - len(str(matrix[i][j]))
                string = " " * need + str(matrix[i][j])
                print(string, end = "")

        print("")

    print("")


def getLineFile(file):
    lines = []

    with open(file, 'r') as f:
        lines = f.read().split('\n')

    data = []
    foldings = []
    endData = False
    for index, line in enumerate(lines):

        if endData:
            el = line.split(" ")[2]
            key, value = el.split("=")

            foldings.append({
                key: int(value)
            })
        elif line == "" or line == "\n" or line is None or line == "\r\n":
            endData = True
        else:
            data.append(line)

    return data, foldings

if __name__ == "__main__":
    main()