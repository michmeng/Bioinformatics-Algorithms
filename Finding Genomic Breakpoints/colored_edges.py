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

def colored_edges(genome):
    edges = []
    for each in genome:
        nodes = chromosome_to_cycle(each)
        for i in range(1, len(each)):
            edge = (nodes[(2*i - 1)], nodes[(2*i)])
            edges.append(edge)
        edges.append((nodes[-1],nodes[0]))
    return edges

if __name__== "__main__":
    with open("Chapter 6\input.txt") as f:
        for line in f:
            line = line.rstrip("")
    line = line[1:-2]
    g = line.split(")(")
    genome = []
    for each in g:
        add = each.split(" ")
        genome.append(add)
    edit_genome = []
    for g in genome:
        add = []
        for each in g:
            if "+" in each:
                add.append(int(each[1:]))
            if "-" in each:
                add.append(int(each[1:]) * -1)
        edit_genome.append(add)
    result = colored_edges(edit_genome)
    edges = ""
    for each in result:
        edges = edges + str(each) + ", "
    edges = edges[:-2]
    print (edges)
