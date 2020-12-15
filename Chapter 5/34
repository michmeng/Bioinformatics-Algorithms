def edit_distance(str1, str2):
    d = [[i for i in range(len(str2) + 1)] for j in range(len(str1) + 1)]
    for i in range(len(str1) + 1):
        d[i][0] = i

    for j in range(1, len(str2)+1):
        for i in range(1, len(str1)+1):
            insertion = d[i][j-1] + 1
            deletion = d[i-1][j] + 1
            mismatch = d[i-1][j-1] + 1
            match = d[i-1][j-1]

            if str1[i-1] == str2[j-1]:
                d[i][j] = min(insertion,deletion,match)
            else:
                d[i][j] = min(insertion, deletion,mismatch)

    return (int(d[len(str1)][len(str2)]))

if __name__== "__main__":
    with open("Chapter 5\input.txt") as f:
        patterns = [line.strip() for line in f]
    print( edit_distance(patterns[0], patterns[1]))
