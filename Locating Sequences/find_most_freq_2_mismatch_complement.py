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

def rev_compliment(str):
    compl = ""
    for c in str:
        if c == "A":
            compl += "T"
        if c == "T":
            compl += "A"
        if c == "C":
            compl += "G"
        if c == "G":
            compl += "C"
    rev_compl = ""
    for c in compl:
        rev_compl = c + rev_compl
    return rev_compl

def freq_word_mismatch_compliment(text, k, d):
    combos = []
    make_combos("ATGC", "", 4, k, combos)
    # check each kmer with the text and store occurance and pattern in dictionary, look for max
    dict = {}
    for i in combos:
        for j in range(len(text) - k + 1):
            word = text[j:(j+k)]
            if hamming_dist(i, word) <= d:
                if i in dict:
                    dict[i] = dict.get(i) + 1
                else:
                    dict[i] = 1
            comp_combo = rev_compliment(i)
            if hamming_dist(comp_combo, word) <= d:
                if i in dict:
                    dict[i] = dict.get(i) + 1
                else:
                    dict[i] = 1
    #find max and print combinations with max count
    max = 0
    for i in dict:
        if dict[i] > max:
            max = dict[i]
    result = ""
    for i in dict:
        if dict[i] == max:
            result = result + str(i) + " "
    return result

# print(freq_word_mismatch_compliment("", , ))
