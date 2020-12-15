
def hamming_dist(str1, str2):
    mismatch = 0
    #should prob check if len(str1) == len(str2)
    for i in range(len(str1)):
        c1 = str1[i]
        c2 = str2[i]
        if c1 != c2:
            mismatch += 1
    return mismatch

def make_combos(lst, prefix, l, k, result):
    if k == 0:
        result.append(prefix)
        return []
    for i in range(l):
        prefNew = prefix + lst[i]
        make_combos(lst, prefNew, l, k-1, result)

def neighbors(pattern, d):
    k = len(pattern)
    combos = []
    make_combos("ATGC", "", 4, k, combos)
    c = []
    for i in combos:
        string = ''.join(i)
        c.append(string)
    result = []
    for neighbor in c:
        if hamming_dist(pattern, neighbor) <= d:
            result.append(neighbor)
    # for each in result:
    #     print (each)
    return result

neighbors("TGAGTCCAA",2)
