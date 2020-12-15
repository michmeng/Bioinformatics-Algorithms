def clump_pattern(genome, k, L, t):
    result = []
    for i in range(len(genome) - L + 1):
        patterns = {}
        for j in range(i, (i+L-1)):
            pattern = genome[j:(j+k)]
            if pattern in patterns:
                patterns[pattern] = patterns.get(pattern) + 1
            else:
                patterns[pattern] = 1
        for each in patterns:
            if patterns[each] >= t:
                if each not in result:
                    result.append(each)
        p = ""
        for pattern in result:
            p = p + pattern + " "
    return p

#print (clump_pattern())
