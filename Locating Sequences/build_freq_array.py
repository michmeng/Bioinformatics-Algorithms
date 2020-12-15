def make_combos(lst, prefix, l, k, result):
    if k == 0:
        result.append(prefix)
        return []
    for i in range(l):
        prefNew = prefix + lst[i]
        make_combos(lst, prefNew, l, k-1, result)

def freq_array(text, k):
    # get all kmers
    combos = []
    make_combos("ACGT", "", 4, k, combos)
    c = []
    for i in combos:
        string = ''.join(i)
        c.append(string)
    freq = ""
    #for each kmer of text, count how many and put in array
    for i in c:
        count = 0
        for j in range(len(text) - k + 1):
            check = text[j:(j+k)]
            if i == check:
                count +=  1
        freq = freq + str(count) + " "

    return freq

# print (freq_array("", ))
