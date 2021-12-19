INPUT_FILE_1 = "input1.txt"
INPUT_FILE_2 = "input2.txt"


class Node:

    def __init__(self, val = None):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        if isinstance(self.val, int):
            return str(self.val)
        
        return f"[{str(self.left)},{str(self.right)}]"


def parse(fishnum):
    root = Node()

    if isinstance(fishnum, int):
        root.val = fishnum
        return root

    root.left = parse(fishnum[0])
    root.right = parse(fishnum[1])
    root.left.parent = root
    root.right.parent = root

    reduce(root)
    return root


def add(node1, node2):
    root = Node()

    root.left = node1
    root.right = node2
    root.left.parent = root
    root.right.parent = root

    reduce(root)
    return root


def magnitude(root):
    if isinstance(root.val, int):
        return root.val

    return 3 * magnitude(root.left) + 2 * magnitude(root.right)


def reduce(root):
    
    # find explofing pairs
    # if not split numbers
    # if nothing then done
    # else reduce again

    done = True

    stack = [(root, 0)]

    while len(stack) > 0:
        node, depth = stack.pop()

        if node == None:
            continue


        # we will explode the pair 
        if depth >= 4 and node.val == None and ((node.left == None and node.right == None) or (node.left.val != None and node.right.val != None)):

            prev_node = node.left
            curr_node = node

            # here to find the left node to add the value
            while curr_node != None and (curr_node.left == prev_node or curr_node.left == None):
                prev_node = curr_node
                curr_node = curr_node.parent

            if curr_node != None:

                #go to left node the nalways right until value
                curr_node = curr_node.left
                while curr_node.val == None:
                    if curr_node.right != None:
                        curr_node = curr_node.right
                    else:
                        curr_node = curr_node.left

                # adding to that node 
                curr_node.val += node.left.val

            # Same thing but for the right node
            prev_node = node.right
            curr_node = node

            # here to find the left node to add the value
            while curr_node != None and (curr_node.right == prev_node or curr_node.right == None):
                prev_node = curr_node
                curr_node = curr_node.parent

            if curr_node != None:

                #go to left node the nalways right until value
                curr_node = curr_node.right
                while curr_node.val == None:
                    if curr_node.left != None:
                        curr_node = curr_node.left
                    else:
                        curr_node = curr_node.right

                # adding to that node 
                curr_node.val += node.right.val

            
            # finally after explosion
            node.val = 0
            node.left = None
            node.right = None

            done = False
            break

        stack.append((node.right, depth + 1))
        stack.append((node.left, depth + 1))


    # now checking for split values
    if done == False:
        reduce(root)
        return

    # going here only if not epxlosion
    stack = [root]
    while len(stack) > 0:
        node = stack.pop()
        if node == None:
            continue

        if node.val != None:
            if node.val >= 10:
                node.left = Node(node.val // 2)
                node.right = Node(node.val - (node.val // 2))

                node.left.parent = node
                node.right.parent = node
                node.val = None

                done = False
                break

        stack.append(node.right)
        stack.append(node.left)

    if done == False:
        reduce(root)


def main():

    star1 = get_star_1(INPUT_FILE_1)
    print("Star 1 answer : " + str(star1))

    star2 = get_star_2(INPUT_FILE_2)
    print("Star 2 answer : " + str(star2))



def get_star_1(file):
    data = getLineFile(file)
    data = [eval(line) for line in data]

    root = parse(data[0])

    for i in range(1, len(data)):
        root = add(root, parse(data[i]))

    mag = magnitude(root)

    return mag



def get_star_2(file):
    data = getLineFile(file)
    data = [eval(line) for line in data]

    max_mag = 0

    for x in data:
        for y in data:
            tree = add(parse(x), parse(y))
            mag = magnitude(tree)

            if mag > max_mag:
                max_mag = mag

            tree = add(parse(y), parse(x))
            mag = magnitude(tree)

            if mag > max_mag:
                max_mag = mag
            
    return max_mag






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