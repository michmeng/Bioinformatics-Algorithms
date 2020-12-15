def chromosome_to_cycle(chromosome):
    nodes = [0] * (2 * len(chromosome))

    for i in range(0, len(chromosome)):
        curr = chromosome[i]
        if curr > 0:
            nodes[(2*i)] = (2*curr)-1
            nodes[2*i+1] = 2*curr
        else:
            nodes[(2*i)] = (-2)*curr
            nodes[2*i+1] = (-2*curr) - 1
    return nodes

if __name__== "__main__":
    with open("Chapter 6\input.txt") as f:
        for line in f:
            line = line.rstrip()
    line = x = list(map(int, line.split()))
    result = chromosome_to_cycle(line)
    cycle = "("
    for each in result:
        cycle = cycle + str(each) + " "
    cycle = cycle[:-1]
    cycle = cycle + ")"
    print(cycle)
