INPUT_FILE_1 = "input1.txt"
INPUT_FILE_2 = "input2.txt"


def main():

    star1 = get_star_1(INPUT_FILE_1)
    print("Star 1 answer : " + str(star1))

    star2 = get_star_2(INPUT_FILE_2)
    print("Star 2 answer : " + str(star2))



def get_star_1(file):
    data = getLineFile(file)
    
    edges = getCorrectData(data)

    return dfs(edges, "start", [])


def dfs(edges, current, visited, twice = True):
    num = 0

    # loop throught all destinations
    for dst in edges[current]:
        if dst == "end":
            num += 1
        # checking multiple passing in cave
        elif not dst.islower():
            num += dfs(edges, dst, visited, twice)

        elif dst != "start":
            if dst not in visited:
                num += dfs(edges, dst, visited + [dst], twice)
            elif not twice:
                num += dfs(edges, dst, visited + [dst], True)

    return num





def get_star_2(file):
    data = getLineFile(file)
    
    edges = getCorrectData(data)

    return dfs(edges, "start", [], False)


def getCorrectData(lines):

    edges = {}

    for line in lines:
        src, dst = line.split("-")

        if src not in edges.keys():
            edges[src] = []

        if dst not in edges.keys():
            edges[dst] = []

        edges[src].append(dst)
        edges[dst].append(src)

    return edges



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