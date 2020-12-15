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

def eulerian_cycle(graph):
    #create initial cycle
    cycle = []
    cycle.append(str(graph[0][0]))
    v = graph[0][1][0]
    graph[0][1].pop(0)
    while v != graph[0][0]:
        cycle.append(str(v))
        index = [x[0] for x in graph].index(v)
        v = graph[index][1].pop(0)
    cycle.append(str(graph[0][0]))

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

    result = ""
    for i in range(len(cycle)):
        if i < len(cycle) - 1:
            result = result + str(cycle[i]) + "->"
        else:
            result = result + str(cycle[i])
    return result

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
    print (eulerian_cycle(graph))
