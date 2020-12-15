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

def blocks(genome_one, genome_two):
    blocks = []
    for each in genome_one:
        for node in each:
            if node not in blocks:
                blocks.append(node)
    return len(blocks)

def cycles(graph):
    cycles = []
    for each in graph:
        if any(each[0] in sublist for sublist in cycles) == True or any(each[1] in sublist for sublist in cycles) == True:
            count = 0
            index = 0
            for cycle in cycles:
                if count == 0:
                    if each[0] in cycle or each[1] in cycle:
                        cycle.append(each[0])
                        cycle.append(each[1])
                        index = cycles.index(cycle)
                        count = count + 1
                else:
                    if each[0] in cycle or each[1] in cycle:
                        for c in cycle:
                            cycles[index].append(c)
                        cycles.remove(cycle)
        else:
            cycles.append([each[0], each[1]])
    return len(cycles)

def two_break_distance(genome_one, genome_two):
    num_blocks = blocks(genome_one,genome_two)
    genome_one_colored_edges = colored_edges(genome_one)
    genome_two_colored_edges = colored_edges(genome_two)
    new_graph = []
    for each in genome_one_colored_edges:
        new_graph.append(each)
    for each in genome_two_colored_edges:
        new_graph.append(each)
    print (new_graph)
    num_cycles = cycles(new_graph)
    return num_blocks-num_cycles

if __name__== "__main__":
    with open("Chapter 6\input.txt") as f:
        lines = [line.strip() for line in f]
    genomes = []
    for genome in lines:
        curr_genome = []
        genome = genome[1:-1]
        g = genome.split(")(")
        for each in g:
            add = each.split(" ")
            curr_genome.append(add)
        genomes.append(curr_genome)
    edit_genome = []
    for each in genomes:
        new = []
        for e in each:
            new_add = []
            for node in e:
                if "+" in node:
                    new_add.append(int(node[1:]))
                if "-" in node:
                    new_add.append(int(node[1:])*-1)
            new.append(new_add)
        edit_genome.append(new)
    print (two_break_distance(edit_genome[0], edit_genome[1]))
