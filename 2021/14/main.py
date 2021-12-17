INPUT_FILE_1 = "input1.txt"
INPUT_FILE_2 = "input2.txt"


def main():

    star1 = get_star_1(INPUT_FILE_1)
    print("Star 1 answer : " + str(star1))

    star2 = get_star_2(INPUT_FILE_2)
    print("Star 2 answer : " + str(star2))



def get_star_1(file):
    data = getLineFile(file)
    
    template, pair_list = getCleanData(data)
    
    steps = 10
    
    while steps > 0:
        template = applyOneStep(template, pair_list)
        steps -= 1
    
    return getAnswerStar1(template)


def getAnswerStar1(template):

    dict_count = {}

    for char in list(template):
        if dict_count.get(char, None) is None:
            dict_count[char] = 1
        else:
            dict_count[char] += 1
            
    max_value = dict_count[max(dict_count, key=dict_count.get)]
    min_value = dict_count[min(dict_count, key=dict_count.get)]
        
    return max_value - min_value
        

def applyOneStep(template, pairs):
    template = list(template)
    
    new_array = []
    
    for index, char in enumerate(template):
        if index+1 < len(template):
            key = char + template[index+1]
            new_char = pairs[key]
            new_pair = new_char + template[index+1]
            if index == 0:
                new_pair = char + new_char + template[index+1]
            new_array.append(new_pair)

    return "".join(new_array)


def get_star_2(file):
    data = getLineFile(file)
    
    template, pair_list = getCleanData(data)
    
    steps = 40
    pair_counts = {}
    
    template = list(template)
    for index, char in enumerate(template):
        if index+1 < len(template):
            key = char + template[index+1]
            pair_counts[key] = pair_counts.get(key, 0) + 1
    
    while steps > 0:
        new_pair_counts = {}
        for key in pair_counts.keys():
            
            pair_count = pair_counts[key]
            to_insert = pair_list[key]
            new_pair_1 = list(key)[0] + to_insert
            new_pair_2 = to_insert + list(key)[1]
            
            new_pair_counts[new_pair_1] = new_pair_counts.get(new_pair_1, 0) + pair_count
            new_pair_counts[new_pair_2] = new_pair_counts.get(new_pair_2, 0) + pair_count
            
        pair_counts = new_pair_counts
            
        steps -= 1
    
    return count_letters(pair_counts, template)


def count_letters(pair_counts, template):
    dict_letters = {}
    
    for pair in pair_counts.keys():
        dict_letters[pair[0]] = dict_letters.get(pair[0], 0) + pair_counts[pair]
        dict_letters[pair[1]] = dict_letters.get(pair[1], 0) + pair_counts[pair]

    dict_letters[template[0]] += 1
    dict_letters[template[-1]] += 1

    count_values = [c[1] // 2 for c in dict_letters.items()]
    
    return max(count_values) - min(count_values)


def getCleanData(lines):
    dict = {}
    
    for index, line in enumerate(lines):
        if index > 0:
            key, val = line.split(" -> ")
            dict[key] = val
            
    return lines[0], dict


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