INPUT_FILE_1 = "input1.txt"
INPUT_FILE_2 = "input2.txt"


def main():

    star1 = get_star_1(INPUT_FILE_1)
    print("Star 1 answer : " + str(star1))

    star2 = get_star_2(INPUT_FILE_2)
    print("Star 2 answer : " + str(star2))



def get_star_1(file):
    data = getLineFile(file)
    
    crabs = data[0].split(',')
    crabs = [int(crab) for crab in crabs]
    
    max_pos = max(crabs)
    
    list_fuel = []
    
    for pos in range(max_pos + 1):
        sum_fuel = 0
        
        for crab in crabs:
            sum_fuel += abs(crab - pos)
            
        list_fuel.append(sum_fuel)

    return min(list_fuel)



def get_star_2(file):
    data = getLineFile(file)
    
    crabs = data[0].split(',')
    crabs = [int(crab) for crab in crabs]
    
    max_pos = max(crabs)
    
    list_fuel = []
    
    for pos in range(max_pos + 1):
        sum_fuel = 0
        
        for crab in crabs:
            sum_fuel += get_fuel_position(abs(crab - pos))
            
        list_fuel.append(sum_fuel)

    return min(list_fuel)


def get_fuel_position(move):
    return int((move * move + move) / 2)


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