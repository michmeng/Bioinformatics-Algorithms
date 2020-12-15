def bwt(text):
    rotations = []
    suff = ""
    while len(text) > 0:
        add = text + suff
        rotations.append(add)
        suff = suff + text[0]
        text = text[1:]
    rotations.sort()
    transformation = ""
    for each in rotations:
        transformation = transformation + each[-1]
    del rotations
    del suff
    return transformation

def first_and_last_column(transform):
    last_column = []
    a_count = 1
    t_count = 1
    c_count = 1
    g_count = 1
    for each in transform:
        if each == "A":
            last_column.append((each,a_count))
            a_count = a_count + 1
        elif each == "T":
            last_column.append((each,t_count))
            t_count = t_count + 1
        elif each == "C":
            last_column.append((each,c_count))
            c_count = c_count + 1
        elif each == "G":
            last_column.append((each,g_count))
            g_count = g_count + 1
        else:
            last_column.append((each, 1))
    first_column = last_column.copy()
    first_column.sort(key=lambda x: x[0])
    return first_column, last_column

def check_occurance(start, end, symbol, last_column):
    for i in range(int(start), int(end)+1):
        if last_column[i][0] == symbol:
            return True
    return False

def find_count(last_column, C):
    counts = []
    counts.append([0, 0, 0, 0, 0])
    a_count = 0
    c_count = 0
    g_count = 0
    t_count = 0
    d_count = 0
    for i in range(0, len(last_column)):
        if last_column[i][0] == "A":
            a_count = a_count + 1
        elif last_column[i][0] == "C":
            c_count = c_count + 1
        elif last_column[i][0] == "G":
            g_count = g_count + 1
        elif last_column[i][0] == "T":
            t_count = t_count + 1
        else:
            d_count = d_count + 1
        counts.append([d_count, a_count, c_count, g_count, t_count])

    result_counts = []
    for i in range(0, len(counts)):
        if i % C == 0:
            result_counts.append(counts[i])
    del counts
    return result_counts

def partial_suffix_array(text, K):
    suffixes = []
    count = 0
    while len(text) > 0:
        suffixes.append((text, count))
        text = text[1:]
        count = count + 1
    suffixes.sort()
    positions = [(suffixes.index(i), i[1]) for i in suffixes if i[1]%K == 0]
    del suffixes
    return positions

def first_occurance(first_column):
    result = []
    result.append(0)
    result.append(first_column.index(("A", 1)))
    result.append(first_column.index(("C", 1)))
    result.append(first_column.index(("G", 1)))
    result.append(first_column.index(("T", 1)))
    return result

def BWT_matching(text, transform, patterns, C, K):
    results = []
    first_column, last_column = first_and_last_column(transform)
    f_occ = first_occurance(first_column)
    counts = find_count(last_column, C)
    partial_suff_arr = partial_suffix_array(text, 1)
    for each in patterns:
        positions = BWT_matching_helper(first_column, last_column, each, transform, f_occ, counts, partial_suff_arr, C, K)
        if positions == 0:
            continue
        if len(positions) == 0:
            continue
        else:
            for each in positions:
                results.append(each)
    return results

def BWT_matching_helper(first_column, last_column, pattern, transform, f_occ, counts, partial_suff_arr, C, K):
    top = 0
    bottom = len(last_column) - 1
    while top <= bottom:
        if len(pattern) > 0:
            symbol = pattern[-1]
            pattern = pattern[:-1]
            if check_occurance(top, bottom, symbol, last_column) == True:
                if top % C != 0:
                    off = top % C
                    index = top - off
                    check_count = counts[int(index/C)]
                else:
                    check_count = counts[int(top/C)]
                    index = top
                if (bottom+1) % C != 0:
                    off_b = (bottom+1) % C
                    index_b = (bottom+1) - off_b
                    check_count_b = counts[int(index_b/C)]
                else:
                    check_count_b = counts[int((bottom+1)/C)]
                    index_b = bottom + 1
                if symbol == "$":
                    first = f_occ[0]
                    c_1 = check_count[0] + check_occurance(index, top-1, "$", last_column)
                    c_2 = check_count_b[0] + check_occurance(index_b, (bottom), "$", last_column)
                elif symbol == "A":
                    first = f_occ[1]
                    c_1 = check_count[1] + check_occurance(index, top-1, "A", last_column)
                    c_2 = check_count_b[1] + check_occurance(index_b, (bottom), "A", last_column)
                elif symbol == "C":
                    first = f_occ[2]
                    c_1 = check_count[2] + check_occurance(index, top-1, "C", last_column)
                    c_2 = check_count_b[2] + check_occurance(index_b, (bottom), "C", last_column)
                elif symbol == "G":
                    first = f_occ[3]
                    c_1 = check_count[3] + check_occurance(index, top-1, "G", last_column)
                    c_2 = check_count_b[3] + check_occurance(index_b, (bottom), "G", last_column)
                elif symbol == "T":
                    first = f_occ[4]
                    c_1 = check_count[4] + check_occurance(index, top-1, "T", last_column)
                    c_2 = check_count_b[4] + check_occurance(index_b, (bottom), "T", last_column)
                top = first + c_1
                bottom = first + c_2 - 1
            else:
                return 0
        else:
            add = []
            for i in range(top, bottom + 1):
                add.append(partial_suff_arr[i][1])
            return add
    return

if __name__ == "__main__":
    with open("Chapter 9\input.txt") as f:
        patterns = [line.rstrip() for line in f]

    text = patterns[0]
    text = text + "$"
    patterns = patterns[1:]
    transform = bwt(text)
    first_column, last_column = first_and_last_column(transform)
    f_occ = first_occurance(first_column)
    counts = find_count(last_column, 2)
    partial_suff_arr = partial_suffix_array(text, 1)
    # print (BWT_matching_helper(first_column, last_column, patterns[0], transform, f_occ, counts, partial_suff_arr, 2, 2))
    positions = BWT_matching(text, transform, patterns, 2, 2)
    result = ""
    for each in positions:
        result = result + str(each) + " "
    del positions
    print (result)
