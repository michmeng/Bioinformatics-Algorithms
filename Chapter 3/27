def find_start_and_end(graph):
    #find vertex with one more outdegree than indegree
    #each time encounter num while going through others lists increment
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

    start = ""
    end = ""
    for i in range(0,len(n)):
        if outdegree[i] == indegree[i] + 1:
            start = n[i]
        if outdegree[i] == indegree[i] - 1:
            end = n[i]
    return start, end

def unexplored(graph, cycle):
    for each in graph:
        if len(each[1]) != 0:
            if each[0] in cycle:
                return each
    return False

def new_cycle_shift(cycle, new_start):
    cycle.pop(-1)
    index = cycle.index(str(new_start))
    for i in range(0,index):
        cycle.append(cycle.pop(0))
    cycle.append(new_start)
    return cycle

def eulerian_cycle(graph, start):
    #create initial cycle
    cycle = []
    i = [x[0] for x in graph].index(start)
    cycle.append(str(graph[i][0]))
    v = graph[i][1][0]
    graph[i][1].pop(0)
    while v != graph[i][0]:
        cycle.append(str(v))
        index = [x[0] for x in graph].index(v)
        v = graph[index][1].pop(0)
    cycle.append(str(graph[i][0]))

    #while there are unexplored edges in graph
    while unexplored(graph,cycle) != False:
        newStart = unexplored(graph,cycle)[0]
        new_cycle = new_cycle_shift(cycle, newStart)
        index = [x[0] for x in graph].index(newStart)
        v = graph[index][1][0]
        graph[index][1].pop(0)
        while int(v) != int(newStart):
            new_cycle.append(str(v))
            index = [x[0] for x in graph].index(v)
            v = graph[index][1].pop(0)
        new_cycle.append(str(newStart))
        cycle = new_cycle

    return cycle

def eulerian_path(graph):
    start, end = find_start_and_end(graph)
    if end not in [x[0] for x in graph]:
        graph.append((end,[start]))
    else:
        index = [x[0] for x in graph].index(end)
        graph[index][1].append(start)

    output = eulerian_cycle(graph, start)
    index = output.index(end)
    output[:-1]

    ending = output[0:index+1]
    beginning = output[index+1:len(output)-1]

    ans = beginning + ending

    result = ""
    for i in range(len(ans)):
        if i < len(ans) - 1:
            result = result + str(ans[i]) + "->"
        else:
            result = result + str(ans[i])
    return result



if __name__== "__main__":
    with open("Chapter 3\input") as f:
        lines = [line.rstrip() for line in f]
    vertices = []
    edges_to  = []
    for each in lines:
        vertices.append(each.split(' -> ')[0])
        edges = each.split(' -> ')[1]
        add = edges.split(',')
        edges_to.append(add)
    graph_init = tuple(zip(vertices, edges_to))
    graph = list(graph_init)
    print(eulerian_path(graph))
