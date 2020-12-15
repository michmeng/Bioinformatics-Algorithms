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
    for each in result:
        print (each)


if __name__== "__main__":
    with open("Chapter 3\input") as f:
        lines = [line.rstrip() for line in f]
    print (debruijn_collection(lines))
