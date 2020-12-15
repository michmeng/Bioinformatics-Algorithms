def cycle_to_chromosome(cycle):
    chromosome = [0] * (int(len(cycle)/2))
    for i in range(0, int(len(cycle)/2)):
        if cycle[(2*i)] < cycle[2*i + 1]:
            chromosome[i] = int((cycle[2*i] + 1)/2)
        else:
            chromosome[i] = int(cycle[(2*i)]/2) * -1
    return chromosome

if __name__== "__main__":
    with open("Chapter 6\input.txt") as f:
        for line in f:
            line = line.rstrip()
    line = x = list(map(int, line.split()))
    line = line[-1:] + line[:-1]
    result = cycle_to_chromosome(line)
    chromosome = "("
    for each in result:
        if each > 0:
            chromosome = chromosome + "+" + str(each) + " "
        else:
            chromosome = chromosome + str(each) + " "
    chromosome = chromosome[:-1]
    chromosome = chromosome + ")"
    print (chromosome)
