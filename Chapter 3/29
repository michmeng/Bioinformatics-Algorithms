def make_combos(lst, prefix, l, k, result):
    if k == 0:
        result.append(prefix)
        return []
    for i in range(l):
        prefNew = prefix + lst[i]
        make_combos(lst, prefNew, l, k-1, result)

def debruijn_collection(lst):
    pre = []
    suff = []
    for each in lst:
        a = each[0:len(each)-1]
        b = each[1:len(each)]
        pre.append(a)
        suff.append(b)
    result = []
    pre_check = []
    for i in range(0,len(suff)):
        if pre[i] in pre_check:
            result[pre_check.index(pre[i])] = result[pre_check.index(pre[i])] + "," + str(pre[pre.index(suff[i])])
            suff[i] = "N"
        else:
            pre_check.append(pre[i])
            result.append(str(pre[i] + " -> " + str(suff[i])))
            suff[i]= "N"
    result.sort()
    return result

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

    # result = ""
    # for i in range(len(cycle)):
    #     if i < len(cycle) - 1:
    #         result = result + str(cycle[i]) + "->"
    #     else:
    #         result = result + str(cycle[i])
    return cycle

def string_from_genome_path(patterns):
    result = ""
    result = result + str(patterns[0])
    for i in range(1, len(patterns)):
        result = result + str(patterns[i][-1])
    return result

def circular_string(k):
    combos = []
    make_combos("01", "", 2, k, combos)
    graph = debruijn_collection(combos)
    vertices = []
    edges_to  = []
    for each in graph:
        vertices.append(each.split(' -> ')[0])
        edges = each.split(' -> ')[1]
        add = edges.split(',')
        edges_to.append(add)
    graph_init = tuple(zip(vertices, edges_to))

    debruijn_graph = list(graph_init)
    print (debruijn_graph)

    path = eulerian_cycle(debruijn_graph)
    print (path)
    n = k - 1
    res = path[: len(path) - n]

    result = string_from_genome_path(res)

    print (len(result))

    return result

print (circular_string(4))
