def suffix_array(text):
    suffixes = []
    count = 0
    while len(text) > 0:
        suffixes.append((text, count))
        text = text[1:]
        count = count + 1
    suffixes.sort()
    suff = []
    suff_indices = []
    for each in suffixes:
        suff.append(each[0])
        suff_indices.append(each[1])
    return suff, suff_indices

def pattern_matching_w_suffix_array(text, pattern, suff, suff_indices):
    min_index = 0
    max_index = len(text) - 1
    while min_index <= max_index:
        mid_index = (min_index + max_index) // 2
        if pattern > suff[mid_index]:
            min_index = mid_index + 1
        else:
            max_index = mid_index - 1
    if pattern == suff[min_index][0:len(pattern)]:
        first = min_index
    else:
        return "not found"
    min_index = first
    max_index = len(text) - 1
    while min_index <= max_index:
        mid_index = (min_index + max_index) // 2
        if pattern == suff[mid_index][0:len(pattern)]:
            min_index = mid_index + 1
        else:
            max_index = mid_index - 1
    last = max_index
    return (first, last)

if __name__ == "__main__":
    with open("Chapter 9\input.txt") as f:
        strings = [line.rstrip() for line in f]

    text = strings[0]
    strings.pop(0)

    suff, suff_indices = suffix_array(text)

    positions = []
    for each in strings:
        pos = pattern_matching_w_suffix_array(text, each, suff, suff_indices)
        for i in range(pos[0], pos[1]+1):
            positions.append(suff_indices[i])
    positions.sort()
    result = ""
    for each in positions:
        result = result + str(each) + " "
    print (result)
