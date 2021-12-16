from queue import PriorityQueue

INPUT_FILE_1 = "input1.txt"
INPUT_FILE_2 = "input2.txt"


def main():

    star1 = get_star_1(INPUT_FILE_1)
    print("Star 1 answer : " + str(star1))

    star2 = get_star_2(INPUT_FILE_2)
    print("Star 2 answer : " + str(star2))



def get_star_1(file):
    data = getLineFile(file)
    matrix = getMatrixData(data)

    start = getKeyFromPoint([0,0])
    goal = getKeyFromPoint([len(matrix)-1,len(matrix[0])-1])

    graph = matrixToGraph(matrix)

    parent, cost = dijkstra(graph, start, goal)
    totalCost = cost[goal]
    path = reverse_path(parent, goal)

    print(path)

    return totalCost



def get_star_2(file):

    data = getLineFile(file)
    matrix = getMatrixData(data)
    matrix = shiftMatrix(matrix)

    start = getKeyFromPoint([0,0])
    goal = getKeyFromPoint([len(matrix)-1,len(matrix[0])-1])

    graph = matrixToGraph(matrix)

    parent, cost = dijkstra(graph, start, goal)
    totalCost = cost[goal]
    path = reverse_path(parent, goal)

    print(path)

    return totalCost


def dijkstra(G, start, goal):
    visited = set()
    cost = {start : 0}
    parent = {start : None}
    priority_queue = PriorityQueue()

    priority_queue.put((0, start))
    while priority_queue:
        while not priority_queue.empty():
            _, prio = priority_queue.get()

            if prio not in visited: 
                break

        else:
            break

        visited.add(prio)

        if prio == goal:
            break

        for neightboor, distance in G[prio]:
            if neightboor in visited: 
                continue

            old_cost = cost.get(neightboor, float('inf'))
            new_cost = cost[prio] + distance

            if new_cost < old_cost:
                priority_queue.put((new_cost, neightboor))
                cost[neightboor] = new_cost
                parent[neightboor] = prio

    return parent, cost


def reverse_path(parent, goal):
    goal = getKeyFromPoint(goal)

    if goal not in parent:
        return None

    value = goal
    path = []
    while value is not None:
        path.append(value)
        value = parent[value]

    return path[::-1]

def shiftMatrix(matrix):
    new_matrix = []

    for i in range(len(matrix)):
        length = len(matrix[0])
        new_line = matrix[i].copy()
        for k in range(1, 5):
            new_line += [x+1 if (x+1) <= 9 else 1 for x in new_line[(k-1)*length:(k-1)*length+length]]

        new_matrix.append(new_line)

    mat_ref = new_matrix.copy()
    for k in range(1, 5):
        new_mat = []

        for i in range(len(mat_ref)):
            new_mat.append([])
            new_mat[i] = [x+1 if (x+1) <= 9 else 1 for x in mat_ref[i]]

        for line in new_mat:
            new_matrix.append(line)

        mat_ref = new_mat.copy()

    return new_matrix


def getKeyFromPoint(start):
    return str(start[0]) + "_" + str(start[1]) 



def getNeighboors(matrix, point):
    neighboors = []

    for dx, dy in ((-1, 0), (0, -1), (1, 0), (0, 1)):

        px = point[0]+dx
        py = point[1]+dy

        if px >= 0 and px < len(matrix):
            if py >= 0 and py < len(matrix[0]):
                neighboors.append([px, py])


    return neighboors



def getMatrixData(lines):

    matrix = []

    for l in lines:
        matrix.append(
            [int(x) for x in list(l)]
        )

    return matrix


def matrixToGraph(matrix):
    graph = {}
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            neighboors = getNeighboors(matrix, [i, j])
            current_key = getKeyFromPoint([i, j])
            graph[current_key] = set()

            for n in neighboors:
                graph[current_key].add((
                    getKeyFromPoint(n),
                    matrix[n[0]][n[1]]
                ))

    return graph
            


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

    for index, line in enumerate(lines):
        if line == "" or line == "\n" or line is None or line == "\r\n":
            lines.pop(index)

    return lines

if __name__ == "__main__":
    main()