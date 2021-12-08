INPUT_FILE_1 = "input1.txt"
INPUT_FILE_2 = "input2.txt"


def main():

    star1 = get_star_1(INPUT_FILE_1)
    print("Star 1 answer : " + str(star1))

    star2 = get_star_2(INPUT_FILE_2)
    print("Star 2 answer : " + str(star2))



def get_star_1(file):
    data = getLineFile(file)

    board_size = 5

    play = data[0].split(",")
    nb_boards = int((len(data) - 1) / board_size)
    boards_data = []
    board_found = [False] * (board_size * board_size)
    boards_found = []

    data_shift = 1
    for i in range(nb_boards):
        boards_found.append(board_found.copy())
        boards_data.append(get_board_formatted(data[1 + i * board_size:1 + i * board_size + board_size]))

    for p in play:
        p = int(p)

        for index, board in enumerate(boards_data):
            if p in board:
                found = board.index(p)
                boards_found[index][found] = True

            if check_board_finished(boards_found[index], board_size):

                return get_sum_element(board, boards_found[index], False) * p


    return None



def get_star_2(file):
    data = getLineFile(file)

    board_size = 5

    play = data[0].split(",")
    nb_boards = int((len(data) - 1) / board_size)
    boards_data = []
    board_found = [False] * (board_size * board_size)
    boards_found = []

    finished_boards = []

    data_shift = 1
    for i in range(nb_boards):
        boards_found.append(board_found.copy())
        boards_data.append(get_board_formatted(data[1 + i * board_size:1 + i * board_size + board_size]))

    for p in play:
        p = int(p)

        for index, board in enumerate(boards_data):

            if index not in finished_boards:
                if p in board:
                    found = board.index(p)
                    boards_found[index][found] = True

                if check_board_finished(boards_found[index], board_size):

                    finished_boards.append(index)

                    if len(finished_boards) == len(boards_data):
                        return get_sum_element(board, boards_found[index], False) * p


    return None



def get_sum_element(matrix_data, board_found, founded):

    total = 0
    for index, value in enumerate(board_found):

        if value == founded:
            total += matrix_data[index]

    return total 



def get_board_formatted(data):

    string = " ".join(data)
    listed = string.split(" ")
    listed = [x for x in listed if x] # rmeove empty char
    listed = [int(x) for x in listed if x] # convert to int

    return listed



def check_board_finished(board_found, board_size):

    row_done = check_row_done(board_found, board_size)
    col_done = check_col_done(board_found, board_size)

    if (row_done != -1) or (col_done != -1):
        return True

    return False


def check_row_done(board_found, board_size):
    
    for i in range(board_size):
        done = True
        for j in range(board_size):
            if board_found[i*board_size + j] == False:
                done = False
                break

        if done == True:
            return i

    return -1


def check_col_done(board_found, board_size):
    
    for i in range(board_size):
        done = True
        for j in range(board_size):
            if board_found[j*board_size + i] == False:
                done = False
                break

        if done == True:
            return i

    return -1



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