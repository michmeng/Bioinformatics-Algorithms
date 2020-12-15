def backtracker(first_sequence, second_sequence, third_sequence):
    score = [[[0 for k in range(len(third_sequence)+1)] for j in range(len(second_sequence)+1)] for i in range(len(first_sequence)+1)]
    backtrack = [[[0 for k in range(len(third_sequence)+1)] for j in range(len(second_sequence)+1)] for i in range(len(first_sequence)+1)]

    for i in range (1, len(first_sequence)+1):
        score[i][0][0] = score[i-1][0][0]-1
    for j in range (1, len(second_sequence)+1):
        score[0][j][0] = score[0][j-1][0]-1
    for k in range (1, len(third_sequence)+1):
        score[0][0][k] = score[0][0][k-1]-1

    for i in range (1, len(first_sequence)+1):
        for j in range (1, len(second_sequence)+1):
            for k in range (1, len(third_sequence)+1):
                backtrack[i][0][0] = "D"
                backtrack[0][j][0] = "R"
                backtrack[0][0][k] = "F"
                backtrack[i][j][0] = "DD"
                backtrack[0][j][k] = "DF"
                backtrack[i][0][k] = "DFD"

    for i in range(1, len(first_sequence)+1):
        for j in range(1, len(second_sequence)+1):
            for k in range(1, len(third_sequence)+1):
                if first_sequence[i-1] == second_sequence[j-1] and second_sequence[j-1] == third_sequence[k-1]:
                    score[i][j][k] = score[i-1][j-1][k-1] + 1
                    backtrack[i][j][k] = "DIAG"
                else:
                    score[i][j][k] = max(score[i-1][j][k], score[i][j-1][k], score[i][j][k-1],score[i-1][j-1][k], score[i-1][j][k-1],score[i][j-1][k-1])
                    if score[i][j][k] == score[i-1][j][k]:
                        backtrack[i][j][k] = "D"
                    elif score[i][j][k] == score[i][j][k-1]:
                        backtrack[i][j][k] = "F"
                    elif score[i][j][k] == score[i][j-1][k]:
                        backtrack[i][j][k] = "R"
                    elif score[i][j][k] == score[i-1][j-1][k]:
                        backtrack[i][j][k] = "DD"
                    elif score[i][j][k] == score[i][j-1][k-1]:
                        backtrack[i][j][k] = "DF"
                    elif score[i][j][k] == score[i-1][j][k-1]:
                        backtrack[i][j][k] = "DFD"

    return backtrack, score[len(first_sequence)][len(second_sequence)][len(third_sequence)]

def multiple_allignment(first_sequence, second_sequence, third_sequence):
    allign = []
    allign_two = []
    allign_three = []
    backtrack, score = backtracker(first_sequence, second_sequence, third_sequence)
    i = len(first_sequence)
    j = len(second_sequence)
    k = len(third_sequence)

    while i > 0 or j > 0 or k > 0:
        if backtrack[i][j][k] == "DIAG":
            allign.append(first_sequence[i-1])
            allign_two.append(second_sequence[j-1])
            allign_three.append(third_sequence[k-1])
            i = i-1
            j = j-1
            k = k-1
        elif backtrack[i][j][k] == "D":
            allign.append(first_sequence[i-1])
            allign_two.append("-")
            allign_three.append("-")
            i = i-1
        elif backtrack[i][j][k] == "R":
            allign.append("-")
            allign_two.append(second_sequence[j-1])
            allign_three.append("-")
            j = j-1
        elif backtrack[i][j][k] == "F":
            allign.append("-")
            allign_two.append("-")
            allign_three.append(third_sequence[k-1])
            k = k-1
        elif backtrack[i][j][k] == "DD":
            allign.append(first_sequence[i-1])
            allign_two.append(second_sequence[j-1])
            allign_three.append("-")
            i = i-1
            j = j-1
        elif backtrack[i][j][k] == "DFD":
            allign.append(first_sequence[i-1])
            allign_two.append("-")
            allign_three.append(third_sequence[k-1])
            i = i-1
            k = k-1
        elif backtrack[i][j][k] == "DF":
            allign.append("-")
            allign_two.append(second_sequence[j-1])
            allign_three.append(third_sequence[k-1])
            j = j-1
            k = k-1

    allign = allign[::-1]
    allign_two = allign_two[::-1]
    allign_three = allign_three[::-1]

    allign = "".join(allign)
    allign_two = "".join(allign_two)
    allign_three = "".join(allign_three)


    return score, allign,allign_two,allign_three

if __name__ == '__main__':
    with open("Chapter 5\input.txt") as f:
        patterns = [line.strip() for line in f]
    score, allign, allign_two, allign_three =  multiple_allignment(patterns[0], patterns[1], patterns[2])
    print (score)
    print (allign)
    print (allign_two)
    print (allign_three)
