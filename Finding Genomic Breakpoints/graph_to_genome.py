def cycle_to_chromosome(cycle):
    chromosome = [0] * (int(len(cycle)/2))
    for i in range(0, int(len(cycle)/2)):
        if cycle[(2*i)] < cycle[2*i + 1]:
            chromosome[i] = int((cycle[2*i] + 1)/2)
        else:
            chromosome[i] = int(cycle[(2*i)]/2) * -1
    return chromosome

def graph_to_genome(colored_edges):
    cycles = []
    i = 0
    while i < len(colored_edges)-1:
        add = []
        initial = colored_edges[i][0]
        add.append(colored_edges[i][0])
        add.append(colored_edges[i][1])
        for j in range(i, len(colored_edges)-1):
            if abs(colored_edges[j][1] - colored_edges[j+1][0]) == 1 :
                add.append(colored_edges[j+1][0])
                add.append(colored_edges[j+1][1])
            else:
                break
        cycles.append(add)
        i = j + 1
    print (cycles)
    # cycles = [[5, 7, 6, 1], [2, 3], [4, 8]]
    graph = []
    for each in cycles:
        each = each[-1:] + each[:-1]
        chromosome = cycle_to_chromosome(each)
        graph.append(chromosome)

    return graph

if __name__== "__main__":
    # with open("Chapter 6\input.txt") as f:
    #     for line in f:
    #         line = line.rstrip("")
    line = "(2, 4), (3, 6), (5, 1), (7, 9), (10, 12), (11, 8) "
    line = line[1:-2]
    e = line.split("), (")
    edges = []
    for each in e:
        add = each.split(", ")
        edges.append(add)
    edit_edges = []
    for e in edges:
        add = []
        for each in e:
            add.append(int(each))
        edit_edges.append(add)
    result = graph_to_genome(edit_edges)
    graph = ""
    for each in result:
        add = "("
        for node in each:
            if node > 0:
                add = add + "+" + str(node) + " "
            else:
                add = add + str(node) + " "
        add = add[:-1]
        add = add + ")"
        graph = graph + add
    print (graph)
