def hamming_dist(str1, str2):
    mismatch = 0
    #should prob check if len(str1) == len(str2)
    for i in range(len(str1)):
        c1 = str1[i]
        c2 = str2[i]
        if c1 != c2:
            mismatch += 1
    return mismatch

def distance_between_pattern_and_strings(pattern, dna):
    k = len(pattern)
    distance = 0
    for each in dna:
        hamming_distance = float('inf')
        for i in range(len(each) - k + 1):
            check = each[i:(i+k)]
            if hamming_distance > hamming_dist(pattern, check):
                hamming_distance = hamming_dist(pattern, check)
        distance = distance + hamming_distance
    return distance

def make_combos(lst, prefix, l, k, result):
    if k == 0:
        result.append(prefix)
        return []
    for i in range(l):
        prefNew = prefix + lst[i]
        make_combos(lst, prefNew, l, k-1, result)

def median_string(dna, k):
    distance = float('inf')
    c = []
    make_combos("ATGC", "", 4, k, c)
    for each in c:
        if distance > distance_between_pattern_and_strings(each, dna):
            distance = distance_between_pattern_and_strings(each, dna)
            median = each
    return median

# print (median_string( ))
