def find_degrees(graph):
    n = []
    for each in graph:
        n.append(each[0])
    indegree = [0] * len(n)
    outdegree = [0] * len(n)
    for each in graph:
        index = [x[0] for x in graph].index(each[0])
        outdegree[index] = (len(each[1]))
        for vertex in each[1]:
            if vertex in n:
                index = n.index(vertex)
                indegree[index] += 1
            else:
                n.append(vertex)
                indegree.append(1)
                outdegree.append(0)
    return n, indegree, outdegree


def max_nonbranching_paths(graph):
    n, indegree, outdegree = find_degrees(graph)
    one_to_one = []
    for i in range(0,len(n)):
        if indegree[i] == outdegree[i]:
            one_to_one.append(n[i])
        if outdegree[i] == 0:
            temp = list(graph)
            temp.append(tuple((n[i], [])))
            graph = tuple(temp)

    #make sure start and end are one to one

    used_nodes = []
    path = []
    for node in graph:
        if node[0] not in one_to_one:
            index = n.index(node[0])
            if outdegree[index] > 0:
                for each in node[1]:
                    non_branch_path = []
                    non_branch_path.append(node[0])
                    non_branch_path.append(each)
                    if node[0] not in used_nodes:
                        used_nodes.append(node[0])
                    if each not in used_nodes:
                        used_nodes.append(each)
                    graph[index][1][graph[index][1].index(each)] = "N"
                    while each in one_to_one:
                        i = n.index(each)
                        each = graph[i][1][0]
                        non_branch_path.append(each)
                        if each not in used_nodes:
                            used_nodes.append(each)
                    path.append(non_branch_path)

    for each in one_to_one:
        if each in used_nodes:
            one_to_one[:] = (value for value in one_to_one if value != each)

    repeats = []

    isolated_cycles = []
    for vertice in one_to_one:
        if vertice not in repeats:
            index = n.index(vertice)
            node = graph[index]
            for each in node[1]:
                if each in one_to_one:
                    cycle = []
                    cycle.append(node[0])
                    cycle.append(each)
                    while each in one_to_one and each != cycle[0]:
                        i = n.index(each)
                        each = graph[i][1][0]
                        cycle.append(each)
                    if cycle[0] == cycle[-1]:
                        for each in cycle:
                            repeats.append(each)
                        isolated_cycles.append(cycle)



    for each in isolated_cycles:
        path.append(each)

    return path

if __name__== "__main__":
    with open("Chapter 3\input.txt") as f:
        lines = [line.rstrip() for line in f]
    vertices = []
    edges_to  = []
    for each in lines:
        vertices.append(each.split(' -> ')[0])
        edges = each.split(' -> ')[1]
        add = edges.split(',')
        edges_to.append(add)
    graph = tuple(zip(vertices, edges_to))
    results = max_nonbranching_paths(graph)

    output = open("Chapter 3\output",'w')
    for each in results:
        result = ""
        for i in range(0, len(each)):
            if i < len(each) - 1:
                result = result + str(each[i]) + " -> "
            else:
                result = result + str(each[i])
        output.write(result +  " \n")
