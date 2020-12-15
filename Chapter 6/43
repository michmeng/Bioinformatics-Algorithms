def breakpoints(permutation):
    count = 0
    for i in range(0, len(permutation)-1):
        if permutation[i+1]-permutation[i] != 1:
            count = count + 1
    return count

if __name__== "__main__":
    with open("Chapter 6\input.txt") as f:
        for line in f:
            line = line.rstrip()
    line = x = list(map(int, line.split()))
    line.append(len(line)+1)
    line.insert(0, 0)
    print (breakpoints(line))
