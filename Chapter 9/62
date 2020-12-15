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

def last_to_first_mapping(transform, i):
    first_column, last_column = first_and_last_column(transform)
    symbol = last_column[int(i)]
    return first_column.index(symbol)

def BWT_matching(transform, patterns):
    results = []
    first_column, last_column = first_and_last_column(transform)
    for each in patterns:
        count = BWT_matching_helper(first_column, last_column, each, transform)
        results.append(count)
    return results

def BWT_matching_helper(first_column, last_column, pattern, transform):
    top = 0
    bottom = len(last_column) - 1
    while top <= bottom:
        if len(pattern) > 0:
            symbol = pattern[-1]
            pattern = pattern[:-1]
            sub_last_column = last_column[top:bottom+1]
            contain_pattern = [tup for tup in sub_last_column if tup[0] == symbol]
            if len(contain_pattern)  > 0:
                top_index = last_column.index(contain_pattern[0])
                bottom_index = last_column.index(contain_pattern[-1])
                top = last_to_first_mapping(transform, top_index)
                bottom = last_to_first_mapping(transform, bottom_index)
                print ("top: " + str(top) + " bottom: " + str(bottom))
            else:
                return 0
        else: return bottom - top + 1
    return

if __name__ == "__main__":
    with open("Chapter 9\input.txt") as f:
        strings = [line.rstrip() for line in f]

    transform = strings[0]
    patterns = strings[1].split(" ")
    # results = BWT_matching(transform, patterns)
    print (BWT_matching('AATCGGGTTCAATCGGGGT$', ["ATCG"]))
    # positions = ""
    # for each in results:
    #     positions = positions + str(each) + " "
    # print (positions)
