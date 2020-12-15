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

# print (distance_between_pattern_and_strings())
