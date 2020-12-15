def make_graph(graph):
    n = []
    for each in graph:
        n.append(each[0])
    indegree = [0] * len(n)
    for each in graph:
        index = [x[0] for x in graph].index(each[0])
        for v in each[1]:
            if v in n:
                index = n.index(v)
                indegree[index] += 1
            else:
                n.append(v)
                indegree.append(1)
                if v not in [i[0] for i in graph]:
                    graph.append(tuple((v, [])))
    return graph

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

def topological_ordering(graph):
    topo_order = []
    source = find_source(graph)
    topo_order.append(int(source))
    rem_index = [x[0] for x in graph].index(source)
    graph.pop(rem_index)
    source = find_source(graph)
    while source != -1 and len(graph) > 0:
        topo_order.append(int(source))
        rem_index = [x[0] for x in graph].index(source)
        graph.pop(rem_index)
        source = find_source(graph)

    result = ", ".join([str(x) for x in topo_order])

    return result

if __name__== "__main__":
    with open("Chapter 5\input.txt") as f:
        lines = [line.rstrip() for line in f]
    vertices = []
    edges = []
    for each in lines:
        v = each.split(' -> ')[0]
        if v not in vertices:
            vertices.append(v)
            e = []
            e = each.split(' -> ')[1].split(",")
            edges.append(e)
        else:
            index = vertices.index(v)
            edges[index].append(each.split(' -> ')[1])
    graph_init = tuple(zip(vertices, edges))
    graph = list(graph_init)
    graph = make_graph(graph)
    print (topological_ordering(graph))
