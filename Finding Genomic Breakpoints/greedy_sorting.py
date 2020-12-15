def greedy_sorting(permutation):
    changes = ""
    i = 1
    while permutation[-1] != len(permutation):
        if permutation[i-1] != i:
            if permutation[i-1] == (i * -1) + 1:
                permutation[i-1] == i
                add = "("
                for each in permutation:
                    if each > 0:
                        add = add + "+" + str(each) + " "
                    elif each < 0:
                        add = add + str(each) + " "
                add = add[:-1]
                add = add + ")"
                changes = changes + add + "\n"
            elif i in permutation:
                index = permutation.index(i)
                for j in range(i-1,index+1):
                    permutation[j] = permutation[j]*(-1)
                permutation = permutation[:i-1] + permutation[i-1:index+1][::-1] + permutation[index+1:]
                add = "("
                for each in permutation:
                    if each > 0:
                        add = add + "+" + str(each) + " "
                    elif each < 0:
                        add = add + str(each) + " "
                add = add[:-1]
                add = add + ")"
                changes = changes + add + "\n"
            elif (i * -1) in permutation:
                index = permutation.index((i * -1))
                for j in range(i-1,index+1):
                    permutation[j] = permutation[j]*(-1)
                permutation = permutation[:i-1] + permutation[i-1:index+1][::-1] + permutation[index+1:]
                add = "("
                for each in permutation:
                    if each > 0:
                        add = add + "+" + str(each) + " "
                    elif each < 0:
                        add = add + str(each) + " "
                add = add[:-1]
                add = add + ")"
                changes = changes + add + "\n"
        if permutation[i-1] < 0:
            permutation[i-1] = permutation[i-1] *-1
            add = "("
            for each in permutation:
                if each > 0:
                    add = add + "+" + str(each) + " "
                elif each < 0:
                    add = add + str(each) + " "
            add = add[:-1]
            add = add + ")"
            changes = changes + add + "\n"
        i = i + 1
    return changes

if __name__== "__main__":
    with open("Chapter 6\input.txt") as f:
        for line in f:
            line = line.rstrip()
    line = x = list(map(int, line.split()))
    f = open("Chapter 6\output.txt", "w")
    changes = greedy_sorting(line)
    f.write(changes)
    f.close()
