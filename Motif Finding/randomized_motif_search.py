import random

def profile_most_prob(text, k, profile):
    all_kmer = []
    for i in range(len(text) - k + 1):
        check = text[i:(i+k)]
        all_kmer.append(check)
    probs = {}
    for each in all_kmer:
        prob = 1.0
        index = 0
        for c in each:
            if c == "A":
                prob = float(prob * profile[index][0])
            if c == "C":
                prob = float(prob * profile[index][1])
            if c == "G":
                prob =  float(prob * profile[index][2])
            if c == "T":
                prob = float(prob * profile[index][3])
            index += 1
        probs[each] = float(prob)
    result = []
    max = 0
    for each in probs:
        if probs[each] > max:
            max = probs[each]
    for each in probs:
        if probs[each] == max:
            result.append(each)
    # if more than one result, choose the first one to appear
    min = len(probs) - 1
    if len(result) == 1:
        r = result[0]
    if len(result) > 1:
        for each in result:
            index = all_kmer.index(each)
            if index < min:
                min = index
        r = all_kmer[min]
    return r

def make_profile(motifs):
    columns = [''.join(seq) for seq in zip(*motifs)]
    return [[float(col.count(nuc) + 1) / float(len(col)) for nuc in 'ACGT'] for col in columns]

def hamming_dist(str1, str2):
    mismatch = 0
    #should prob check if len(str1) == len(str2)
    for i in range(len(str1)):
        c1 = str1[i]
        c2 = str2[i]
        if c1 != c2:
            mismatch += 1
    return mismatch

def most_freq_words(text, k):
    all_pat = {}
    for i in (range(len(text) - k + 1)):
        pattern = text[i:(i+k)]
        if pattern in all_pat:
            all_pat[pattern] = all_pat.get(pattern) + 1
        else:
            all_pat[pattern] = 1
    result = []
    max = 0
    for i in all_pat:
        if all_pat[i] > max:
            max = all_pat[i]
    for i in all_pat:
        if all_pat[i] == max:
            return i

def score(motifs):
    #find consensus string
    con = ""
    for i in range(len(motifs[0])):
        l = []
        for each in motifs:
            l.append(each[i])
        line = ""
        for each in l:
            line = line + each
        res = most_freq_words(line, 1)
        con = con + res
    #sum hamming dist between consensus string and each of motif
    sum = 0
    for each in motifs:
        diff = hamming_dist(each, con)
        sum += diff
    return sum

def mot(profile, Dna, k):
    motifs = []
    for i in range(len(Dna)):
        motif = profile_most_prob(Dna[i], k, profile)
        motifs.append(motif)
    return motifs

def randomized_motif_search(Dna, k, t):
    # randomly select kmers to make motif, one from each string in DNA
    motifs = []
    for each in Dna:
        patterns = []
        for i in range(len(each) - k + 1):
            patterns.append(each[i:(i+k)])
        index = random.randrange(0, len(patterns), 1)
        motifs.append(patterns[index])
    best_motif = motifs[:]

    while True:
        profile = make_profile(motifs)
        motifs = mot(profile, Dna, k)
        if score(motifs) < score(best_motif):
            best_motif = motifs
        else:
            return best_motif


def solver(Dna, k, t):
    i = 0

    last_motif = randomized_motif_search(Dna, k, t)

    while(i<1000):
        best_motif = randomized_motif_search(Dna, k, t)
        if score(best_motif) < score(last_motif):
            last_motif = best_motif
        i+=1

    result = ""
    for each in last_motif:
        result = result + "\n" + each
    return result

    return last_motif


# print (solver())
