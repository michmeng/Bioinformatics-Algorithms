def occurance_pattern(pattern, genome):
    result = ""
    for i in range(len(genome)-len(pattern) + 1):
        if genome[i:(i+len(pattern))] == pattern:
            result = result + str(i) + " "
    return result

#print (occurance_pattern("",""))
