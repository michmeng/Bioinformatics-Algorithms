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

def first_occurance(first_column):
    result = []
    result.append(0)
    result.append(first_column.index(("A", 1)))
    result.append(first_column.index(("C", 1)))
    result.append(first_column.index(("G", 1)))
    result.append(first_column.index(("T", 1)))
    return result

def find_count(last_column):
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
    return counts

def check_occurance(start, end, symbol, last_column):
    for i in range(int(start), int(end)+1):
        if last_column[i][0] == symbol:
            return True
    return False

def BWT_matching(transform, patterns):
    results = []
    first_column, last_column = first_and_last_column(transform)
    f_occ = first_occurance(first_column)
    print (f_occ)
    counts = find_count(last_column)
    for each in patterns:
        count = BWT_matching_helper(first_column, last_column, each, transform, f_occ, counts)
        results.append(count)
    return results

def BWT_matching_helper(first_column, last_column, pattern, transform, f_occ, counts):
    top = 0
    bottom = len(last_column) - 1
    while top <= bottom:
        if len(pattern) > 0:
            symbol = pattern[-1]
            pattern = pattern[:-1]
            if check_occurance(top, bottom, symbol, last_column) == True:
                if symbol == "$":
                    first = f_occ[0]
                    c_1 = counts[top][0]
                    c_2 = counts[bottom+1][0]
                elif symbol == "A":
                    first = f_occ[1]
                    c_1 = counts[top][1]
                    c_2 = counts[bottom+1][1]
                elif symbol == "C":
                    first = f_occ[2]
                    c_1 = counts[top][2]
                    c_2 = counts[bottom+1][2]
                elif symbol == "G":
                    first = f_occ[3]
                    c_1 = counts[top][3]
                    c_2 = counts[bottom+1][3]
                elif symbol == "T":
                    first = f_occ[4]
                    c_1 = counts[top][4]
                    c_2 = counts[bottom+1][4]
                top = first + c_1
                bottom = first + c_2 - 1
                print ("first occ: " + str(first))
                print ("count top: " + str(c_1))
                print ("top: " + str(top) + " bottom: " + str(bottom))
            else:
                return 0
        else:
            return bottom - top + 1
    return

if __name__ == "__main__":
    with open("Chapter 9\input.txt") as f:
        strings = [line.rstrip() for line in f]

    transform = strings[0]
    patterns = strings[1].split(" ")
    results = BWT_matching(transform, patterns)
    positions = ""
    for each in results:
        positions = positions + str(each) + " "
    print (positions)
