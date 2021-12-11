INPUT_FILE_1 = "input1.txt"
INPUT_FILE_2 = "input2.txt"


def main():

    star1 = get_star_1(INPUT_FILE_1)
    print("Star 1 answer : " + str(star1))

    star2 = get_star_2(INPUT_FILE_2)
    print("Star 2 answer : " + str(star2))



def get_star_1(file):
    data = getLineFile(file)
    matrix = getDataMatrix(data)
    score = 0

    steps = 100

    for i in range(steps):
        matrix, count = makeOneStep(matrix)
        score += count

    printMatrix(matrix, len(matrix), len(matrix[0]))

    return score


def makeOneStep(matrix):

    matrix = makeFirstStep(matrix)
    matrix, flashed = makeSecondStep(matrix)
    matrix = makeLastStep(matrix)

    return matrix, len(flashed)


def makeFirstStep(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] += 1

    return matrix


def makeSecondStep(matrix):

    flashed = []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            
            if matrix[i][j] > 9 and [i, j] not in flashed:
                flashed.append([i, j])
                matrix, flashed = makeFlash(matrix, i, j, flashed)

    return matrix, flashed


def makeFlash(matrix, i, j, flashed):

    points = [
        (-1, -1),
        (-1, 0),
        (-1, +1),
        (0, -1),
        (0, +1),
        (+1, -1),
        (+1, 0),
        (+1, +1)
    ]

    for p in points:
        dx = i + p[0]
        dy = j + p[1]

        if dx >= 0 and (dx < len(matrix)):
            if dy >= 0 and (dy < len(matrix[0])): 
                matrix[dx][dy] += 1

    for p in points:
        dx = i + p[0]
        dy = j + p[1]

        if dx >= 0 and (dx < len(matrix)):
            if dy >= 0 and (dy < len(matrix[0])): 

                if matrix[dx][dy] > 9 and [dx, dy] not in flashed:
                    flashed.append([dx, dy])
                    matrix, flashed = makeFlash(matrix, dx, dy, flashed)

    return matrix, flashed



def makeLastStep(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            
            if matrix[i][j] > 9:
                matrix[i][j] = 0

    return matrix



def printFlashed(flashed, sizeX, sizeY):

    print("")
    for i in range(sizeX):
        for j in range(sizeY):
            if [i, j] in flashed:
                print("x", end='')
            else:
                print("-", end = "")

        print("")



def printMatrix(matrix, sizeX, sizeY, charSize = 1):

    print("")
    for i in range(sizeX):
        for j in range(sizeY):
            if charSize == 1:
                print(matrix[i][j], end = "")
            else:
                need = charSize - len(str(matrix[i][j]))
                string = " " * need + str(matrix[i][j])
                print(string, end = "")

        print("")

    print("")



def get_star_2(file):
    data = getLineFile(file)
    matrix = getDataMatrix(data)
    step = 1

    while True:
        matrix, count = makeOneStep(matrix)

        if(checkAllFlash(matrix)):
            return step

        step += 1

    return None

def checkAllFlash(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 0:
                return False

    return True


def getDataMatrix(lines):
    matrix = []

    for l in lines:
        values = [int(val) for val in list(l)]
        matrix.append(values)

    return matrix


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