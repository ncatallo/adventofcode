INPUT_FILE_1 = "input1.txt"
INPUT_FILE_2 = "input2.txt"


char_score_first = {
    ")" : 3,
    "]" : 57,
    "}" : 1197,
    ">" : 25137
}
char_score_seconds = {
    ")" : 1,
    "]" : 2,
    "}" : 3,
    ">" : 4
}


openings = ["(", "[", "{", "<"]
closings = [")", "]", "}", ">"]
chars_assignements_closing = {
    ")" : "(",
    "]" : "[",
    "}" : "{",
    ">" : "<"
}
chars_assignements_opening = {
    "(" : ")",
    "[" : "]",
    "{" : "}",
    "<" : ">"
}

def main():

    star1 = get_star_1(INPUT_FILE_1)
    print("Star 1 answer : " + str(star1))

    star2 = get_star_2(INPUT_FILE_2)
    print("Star 2 answer : " + str(star2))



def get_star_1(file):
    data = getLineFile(file)
    score = 0
    
    for line in data:
        char = find_first_illegal(line)
        
        if char is not None:
            score += char_score_first[char]
        

    return score


def find_first_illegal(chunk):
    openings_memory = []
    
    for index, value in enumerate(list(chunk)):
        if value in openings:
            openings_memory.append(value)
            
        if value in closings:
            if chars_assignements_closing[value] == openings_memory[-1]:
                openings_memory.pop()
            else:
                return value
                
    return None


def get_star_2(file):
    data = getLineFile(file)
    scores = []
    
    incompleted = []
    
    # get only incompleted ones
    for line in data:
        char = find_first_illegal(line)
        if char is None:
            incompleted.append(line)
        
    for line in incompleted:
        missing = find_closing_seq(line)
        
        new_missing = []
        for i in range(len(missing)):
            value = missing.pop()
            value = chars_assignements_opening[value]
            new_missing.append(value)
        
        score = 0
        for m in new_missing:
            print(m + " : " + str(char_score_seconds[m]))
            score = score * 5 + char_score_seconds[m]
            
        scores.append(score)
        
    scores = sorted(scores)

    print(scores)
        
    return scores[int(len(scores) / 2 - 0.5)]


def find_closing_seq(chunk):
    openings_memory = []
    
    for index, value in enumerate(list(chunk)):
        if value in openings:
            openings_memory.append(value)
            
        if value in closings:
            if chars_assignements_closing[value] == openings_memory[-1]:
                openings_memory.pop()
                
    return openings_memory


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