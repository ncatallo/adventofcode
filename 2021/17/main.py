import re
from pprint import pprint

INPUT_FILE_1 = "input1.txt"
INPUT_FILE_2 = "input2.txt"


def main():

    star1 = get_star_1(INPUT_FILE_1)
    print("Star 1 answer : " + str(star1))

    star2 = get_star_2(INPUT_FILE_2)
    print("Star 2 answer : " + str(star2))
    



def get_star_1(file):
    data = getLineFile(file)[0]
    
    x_values_re = r"x=(\d+|-\d+)+..(\d+|-\d+)"
    y_values_re = r"y=(\d+|-\d+)+..(\d+|-\d+)"
    
    x_values = re.search(x_values_re, data).groups()
    y_values = re.search(y_values_re, data).groups()
    
    x_values = [int(x) for x in x_values]
    y_values = [int(y) for y in y_values]
    
    max_y_final = 0
    
    for x_velo in range(1, abs(x_values[1])+1):
        for y_velo in range(-abs(x_values[1]+1), abs(x_values[1])+1): # make sure to test a lot of y
            found, max_y = processLoop(x_values, y_values, x_velo, y_velo)
            if found:
                if max_y > max_y_final:
                    max_y_final = max_y
        
    return max_y_final


def get_star_2(file):
    data = getLineFile(file)[0]
    
    x_values_re = r"x=(\d+|-\d+)+..(\d+|-\d+)"
    y_values_re = r"y=(\d+|-\d+)+..(\d+|-\d+)"
    
    x_values = re.search(x_values_re, data).groups()
    y_values = re.search(y_values_re, data).groups()
    
    x_values = [int(x) for x in x_values]
    y_values = [int(y) for y in y_values]
    
    list_found = []
        
    for x_velo in range(1, abs(x_values[1])+1):
        for y_velo in range(-abs(x_values[1])+1, abs(x_values[1])+1): # make sure to test a lot of y
            found, max_y = processLoop(x_values, y_values, x_velo, y_velo)
            if found == True:
                list_found.append([x_velo, y_velo])
                
    return len(list_found)
    

def processLoop(x_values, y_values, x_velo, y_velo, start_x = 0, start_y = 0):
    
    start_x_velo = x_velo
    start_y_velo = y_velo
    found = False
    max_y = 0
    
    while True:    
        if isInsideTarget(start_x, start_y, x_values[0], x_values[1], y_values[0], y_values[1]):
            found = True
            break
    
        if toFarFromTarget(start_y, y_values[0]):
            break
            
        start_x, start_y, start_x_velo, start_y_velo = makeOneStep(start_x, start_y, start_x_velo, start_y_velo)
        
        if start_y > max_y:
            max_y = start_y
    
    return found, max_y





def makeOneStep(x, y, x_velo, y_velo):

    new_x = x + x_velo
    new_y = y + y_velo
    new_x_velo = x_velo
    
    if x_velo > 0:
        new_x_velo = x_velo - 1
    elif x < 0:
        x_velo + 1
        
    new_y_velo = y_velo - 1

    return new_x, new_y, new_x_velo, new_y_velo


def isInsideTarget(current_x, current_y, x_min, x_max, y_min, y_max):
    if current_x >= x_min and current_x <= x_max:
        if current_y >= y_min and current_y <= y_max:
            return True    
            
    return False
    
    
def toFarFromTarget(current_y, y_min):
    if current_y < y_min:
        return True
        
    return False



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