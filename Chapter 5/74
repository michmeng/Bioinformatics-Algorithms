def make_graph(graph):
    n = []
    for each in graph:
        n.append(each[0])
    indegree = [0] * len(n)
    for each in graph:
        index = [x[0] for x in graph].index(each[0])
        for vertex in each[1]:
            v = vertex.split(':')[0]
            if v in n:
                index = n.index(v)
                indegree[index] += 1
            else:
                n.append(v)
                indegree.append(1)
                if v not in [i[0] for i in graph]:
                    graph.append(tuple((v, [])))
    return graph

def find_indegrees(graph):
    n = []
    for each in graph:
        n.append(tuple((each[0], [])))
    indegree = [0] * len(n)
    for each in graph:
        index = [x[0] for x in graph].index(each[0])
        for vertex in each[1]:
            v = vertex.split(':')[0]
            if v in [i[0] for i in n]:
                index = [x[0] for x in n].index(v)
                indegree[index] += 1
                add = graph[[x[0] for x in graph].index(each[0])]
                for edge in each[1]:
                    if edge.split(':')[0] == v:
                        n[index][1].append(tuple((each[0],edge.split(":")[1])))
    return n

def find_source(graph):
    if len(graph) == 0:
        return -1
    n = []
    for each in graph:
        n.append(each[0])
    indegree = [0] * len(n)
    for each in graph:
        index = [x[0] for x in graph].index(each[0])
        for vertex in each[1]:
            v = vertex.split(':')[0]
            if v in n:
                index = n.index(v)
                indegree[index] += 1
            else:
                n.append(v)
                indegree.append(1)
    for i in range(0,len(n)):
        if indegree[i] == 0:
            return n[i]
    return -1

def topological_ordering(source, end, graph):
    topo_order = []
    topo_order.append(source)
    rem_index = vertices.index(str(source))
    graph.pop(rem_index)
    vertices.pop(rem_index)
    source = find_source(graph)
    while source != -1 and len(vertices) > 0:
        topo_order.append(int(source))
        rem_index = vertices.index(str(source))
        graph.pop(rem_index)
        vertices.pop(rem_index)
        source = find_source(graph)
        if source == end:
            source = -1
    topo_order.append(end)
    return topo_order

def longest_path_in_DAG(source, end, graph):
    predecessors = []
    predecessors.append("N")
    s_index = [x[0] for x in graph]
    s = [float('-inf')]*len(graph)
    vertices = [i[0] for i in graph]
    index = vertices.index(str(source))
    s[index] = 0

    #find topological order in graph
    copy_graph = graph.copy()
    topo_order = topological_ordering(source, end, copy_graph)

    indegrees = find_indegrees(graph)

    topo_copy = topo_order.copy()
    # for each node, find maximum path from its predecessors to it plus the edge weight
    for each in topo_order:
        if each != source:
            index = [x[0] for x in indegrees].index(str(each))
            check = []
            check_nodes = []
            if len(indegrees[index][1]) > 0:
                for edges in indegrees[index][1]:
                    i = s_index.index(edges[0])
                    check.append(float(s[i]) + float(edges[1]))
                    check_nodes.append(float(s_index[i]))
                maximum = max(check)
                max_index = check.index(maximum)
                predecessors.append(int(check_nodes[max_index]))
                here = s_index.index(str(each))
                s[here] = maximum
            else:
                topo_copy.remove(each)
    result_index = s_index.index(str(end))
    return int(s[result_index]), predecessors, topo_copy

def dags_backtracker(source, end, graph):
    l, predecessors, topo_order = longest_path_in_DAG(source, end, graph)
    path = []
    path.append(str(topo_order[-1]))
    node = predecessors[-1]
    path.append(str(node))
    while node != source:
        index = topo_order.index((node))
        path.append(str(predecessors[index]))
        index_two = topo_order.index((predecessors[index]))
        node = topo_order[index_two]
    path.reverse()
    path = "->".join(path)
    return l, path


if __name__== "__main__":
    with open("Chapter 5\input.txt") as f:
        lines = [line.rstrip() for line in f]
    vertices = []
    edges = []
    for each in lines:
        v = each.split('->')[0]
        if v not in vertices:
            vertices.append(v)
            e = []
            e.append(each.split('->')[1])
            edges.append(e)
        else:
            index = vertices.index(v)
            edges[index].append(each.split('->')[1])
    graph_init = tuple(zip(vertices, edges))
    graph = list(graph_init)
    graph = make_graph(graph)
    output = dags_backtracker(0,25,graph)
    print (output[0])
    print (output[1])
