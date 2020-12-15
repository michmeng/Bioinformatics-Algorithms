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

def motif_enumeration(Dna, k, d):
    result = []
    c = []
    make_combos("ATGC", "", 4, k, c)
    all_seq = {}
    for each in c:
        for seq in Dna:
            for i in range(len(seq) - k + 1):
                check = seq[i:(i+k)]
                if hamming_dist(check, each) <= d:
                    if each in all_seq:
                        if Dna.index(seq) not in all_seq[each]:
                            all_seq[each].append(Dna.index(seq))
                    else:
                        all_seq[each] = [Dna.index(seq)]
    result = ""
    for each in all_seq:
        if len(all_seq[each]) == len(Dna):
            result = result + each + " "
    return result

def motif_enumeration_two(Dna, k, d):
    patterns = {}



# print (motif_enumeration())
