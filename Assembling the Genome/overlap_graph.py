def overlap_graph(patterns):
    result = []
    pre = []
    suff = []
    for each in patterns:
        pre.append(each[0:len(each)-1])
        suff.append(each[1:len(each)+1])
    for i in range(0,len(suff)):
        if suff[i] in pre:
            result.append(str(patterns[i] + " -> " + str(patterns[pre.index(suff[i])])))
            pre[pre.index(suff[i])] = "N"
    for each in result:
        print (each)


# if __name__== "__main__":
#     with open("Chapter 3\input.txt") as f:
#         lines = [line.rstrip() for line in f]
#     print (overlap_graph(lines))
