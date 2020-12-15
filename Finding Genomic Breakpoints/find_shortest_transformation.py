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

def edge_cycles(g):
    graph = g.copy()
    starts = []
    for each in graph:
        starts.append(each[0])

    cycles = []
    while len(graph) > 0:
        add_cycle = []
        initial = graph[0]
        curr = initial
        check = True
        while check == True and len(graph) > 0:
            if curr[1] % 2 == 0:
                element = curr[1] - 1
            else:
                element = curr[1] + 1
            add = [each for each in graph if each[0] == element]
            add_two = [each for each in graph if each[1] == element]
            if len(add) > 0:
                add_cycle.append(add[0][0])
                add_cycle.append(add[0][1])
                graph.remove(add[0])
                curr = add[0]
            if len(add_two) > 0:
                add_cycle.append(add_two[0][1])
                add_cycle.append(add_two[0][0])
                graph.remove(add_two[0])
                curr = [add_two[0][1], add_two[0][0]]


            if curr == initial:
                check = False
        add_cycle.insert(0, initial[0])
        add_cycle.insert(1, initial[1])
        add_cycle = add_cycle[0:len(add_cycle)-2]
        cycles.append(add_cycle)

    updated_cycles = []
    for each in cycles:
        new_each = each
        min_index = each.index(min(each))
        if min_index == len(each)-1:
            new_each = each[min_index:] + each[0:min_index]
        elif min_index == 0:
            min_next_index = each.index(min(each)+1)
            if min_next_index == len(each)-1:
                new_each = each[min_next_index:] + each[0:min_next_index]
        else:
            min_next_index = each.index(min(each)+1)
            if min_next_index == min_index-1:
                new_each = each[min_next_index:] + each[0:min_next_index]
            else:
                new_each = each[min_index:] + each[0:min_index]
        updated_cycles.append(new_each)

    return updated_cycles

def cycle_to_chromosome(cycle):
    chromosome = [0] * (int(len(cycle)/2))
    for i in range(0, int(len(cycle)/2)):
        if cycle[(2*i)] < cycle[2*i + 1]:
            chromosome[i] = int((cycle[2*i] + 1)/2)
        else:
            chromosome[i] = int(cycle[(2*i)]/2) * -1
    return chromosome

def graph_to_genome(cycles):
    graph = []
    for each in cycles:
        chromosome = cycle_to_chromosome(each)
        graph.append(chromosome)
    return graph

def non_trivial_cycles(graph):
    cycles = []
    for each in graph:
        if any(each[0] in sublist for sublist in cycles) == True or any(each[1] in sublist for sublist in cycles) == True:
            count = 0
            index = 0
            for cycle in cycles:
                if count == 0:
                    if each[0] in cycle or each[1] in cycle:
                        if each[0] not in cycle:
                            cycle.append(each[0])
                        if each[1] not in cycle:
                            cycle.append(each[1])
                        index = cycles.index(cycle)
                        count = count + 1
                else:
                    if each[0] in cycle or each[1] in cycle:
                        for c in cycle:
                            if c not in cycles[index]:
                                cycles[index].append(c)
                        cycles.remove(cycle)
        else:
            cycles.append([each[0], each[1]])

    copy_cycle = []
    for each in cycles:
        if len(each) != 2:
            copy_cycle.append(each)

    return copy_cycle

def shortest_transform(genome_one, genome_two):
    steps = []
    steps.append(genome_one)
    red_edges = colored_edges(genome_one)
    blue_edges = colored_edges(genome_two)
    graph = []
    for each in red_edges:
        graph.append(each)
    for each in blue_edges:
        graph.append(each)

    cycles = non_trivial_cycles(graph)

    while len(cycles) > 0:
        path = []
        for each in blue_edges:
            if each[0] in cycles[0] and each[1] in cycles[0]:
                b_edge = each
                break

        b_edge = list(b_edge)

        for each in red_edges:
            if len(path) < 4:
                if each[1] in b_edge or each[0] in b_edge:
                    if each[0] == b_edge[0] or each[1] == b_edge[0]:
                        if each[0] == b_edge[0]:
                            r_edge_one = (each[1], each[0])
                        else:
                            r_edge_one = each
                        original_one = each
                    if each[0] == b_edge[1] or each[1] == b_edge[1]:
                        if each[1] == b_edge[1]:
                            r_edge_two = (each[1], each[0])
                        else:
                            r_edge_two = each
                        original_two = each
                    path.append(each[0])
                    path.append(each[1])

            else:
                break


        red_edges.remove(original_one)
        red_edges.remove(original_two)
        red_edges.append((r_edge_one[0],r_edge_two[1]))
        red_edges.append((r_edge_one[1],r_edge_two[0]))

        graph = []

        for each in red_edges:
            graph.append(each)
        for each in blue_edges:
            graph.append(each)

        red_cycles = edge_cycles(red_edges)
        step = graph_to_genome(red_cycles)
        steps.append(step)

        cycles = non_trivial_cycles(graph)

    return steps

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
    steps = shortest_transform(edit_genome[0], edit_genome[1])

    result = ""
    for step in steps:
        add = ""
        for each in step:
            add = add + "("
            for block in each:
                if block > 0:
                    add = add + "+" + str(block) + " "
                else:
                    add = add + str(block) + " "
            add = add[:-1]
            add = add + ")"
        add = add[:-1]
        add = add + ")"
        result = result + add + "\n"

    print (result)
