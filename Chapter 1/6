def minimize_skew(genome):
    g = 0
    c = 0
    skew = []
    #skew is always 0 to begin with
    skew.append(0)
    for i in genome:
        if i ==  "C":
            c += 1
        if i == "G":
            g += 1
        skew.append(g-c)
    positions = ""
    min = float('inf')
    for j in range(len(skew)):
        if skew[j] < min:
            min = skew[j]
    for k in range(len(skew)):
        if skew[k] == min:
            positions = positions + str(k) + " "
    return positions

#print (minimize_skew(""))
