import sys

INPUT_FILE_1 = "input1.txt"
INPUT_FILE_2 = "input2.txt"


def main():

    sys.setrecursionlimit(5000)

    star1 = get_star_1(INPUT_FILE_1)
    print("Star 1 answer : " + str(star1))

    star2 = get_star_2(INPUT_FILE_2)
    print("Star 2 answer : " + str(star2))



def get_star_1(file):
    data = getLineFile(file)
    
    matrix = []
    sum_risk = 0
    
    for d in data:
        matrix.append([int(x) for x in list(d)])

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            is_lowest = lowest(matrix, i, j)
            
            if is_lowest:
                sum_risk += 1 + matrix[i][j]
    return sum_risk


def lowest(matrix, i, j):
    
    current = matrix[i][j]
    list_adjs = []
    
    # TOP
    if i > 0:
        list_adjs.append(matrix[i-1][j])
    
    # BOTTOM
    if i < (len(matrix) - 1):
        list_adjs.append(matrix[i+1][j])
       
    # LEFT
    if j > 0:
        list_adjs.append(matrix[i][j-1])
    
    # RIGHT
    if j < (len(matrix[0]) - 1):
        list_adjs.append(matrix[i][j+1])
        
    if min(list_adjs) > current:
        return True
    
    return False


def get_star_2(file):
    data = getLineFile(file)
    
    matrix = []
    basin_data = []
    
    for d in data:
        matrix.append([int(x) for x in list(d)])
        
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            is_lowest = lowest(matrix, i, j)   
            
            if is_lowest:
                print("Min at : " + str(i) + "," + str(j))
                basin_prev = basin(matrix, i, j)
                basin_after = remove_duplicates(basin_prev)
                
                basin_data.append(basin_after)
                
    sizes = [len(x) for x in basin_data]
    sizes = sorted(sizes, reverse=True)
    
    print(sizes)
    
    biggest = sizes[:3]
   
    return multiplyList(biggest)


def basin(matrix, i, j):

    current = matrix[i][j]
    
    if current == 9:
        return []
    
    list_basin = [[i, j]]
    
    # TOP
    if i > 0:
        if matrix[i-1][j] >  current:
            list_basin += basin(matrix, i-1, j)
    
    # BOTTOM
    if i < (len(matrix) - 1):
        if matrix[i+1][j] > current :
            list_basin += basin(matrix, i+1, j)
        
    # LEFT
    if j > 0:
        if matrix[i][j-1] > current:
            list_basin += basin(matrix, i, j-1)
    
    # RIGHT
    if j < (len(matrix[i]) - 1):
        if matrix[i][j+1] > current:
            list_basin += basin(matrix, i, j+1)
        
    return list_basin


def remove_duplicates(array):
    new_array = []
    
    for a in array:
        found = False
        for an in new_array:
            if a[0] == an[0] and a[1] == an[1]:
                found = True
                break
            
        if found == False:
            new_array.append(a)
            
    return new_array

def multiplyList(myList) :
    result = 1
    for x in myList:
         result = result * x
    return result

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