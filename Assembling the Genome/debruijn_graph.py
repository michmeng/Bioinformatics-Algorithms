def debruijn(text, k):
    patterns = []
    for i in range(0,len(text)-k+2):
        add = text[i:i+k-1]
        patterns.append(add)
    result = []
    pre = []
    suff = []
    pre_check = []
    for each in patterns:
        pre.append(each[0:len(each)-1])
        suff.append(each[1:len(each)+1])
    for i in range(0,len(suff)):
        if suff[i] in pre:
            if patterns[i] in pre_check:
                result[pre_check.index(patterns[i])] = result[pre_check.index(patterns[i])] + "," + str(patterns[pre.index(suff[i])])
                pre[pre.index(suff[i])] = "N"
            else:
                pre_check.append(patterns[i])
                result.append(str(patterns[i] + " -> " + str(patterns[pre.index(suff[i])])))
                pre[pre.index(suff[i])] = "N"
    result.sort()
    for each in result:
        print (each)

if __name__== "__main__":
    # with open("Chapter 3\input.txt") as f:
    #     lines = line.rstrip() for line in f]
    # with open('Chapter 3\input.txt', 'r') as file:
    #     data = file.read().replace('\n', '')

    print (debruijn("AAGATTCTCTAC", 4))
