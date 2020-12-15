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
                prob = float(prob * profile[0][index])
            if c == "C":
                prob = float(prob * profile[1][index])
            if c == "G":
                prob =  float(prob * profile[2][index])
            if c == "T":
                prob = float(prob * profile[3][index])
            index += 1
        probs[each] = float(prob)
    max = 0
    for each in probs:
        if probs[each] > max:
            max = probs[each]
    for each in probs:
        if probs[each] == max:
            print (each)

# profile_most_prob()
