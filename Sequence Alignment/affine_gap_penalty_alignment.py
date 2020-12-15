def backtracker(str1,str2,open_penalty, extension_penalty, scoring_matrix, letters):
    backtrack = [[0 for i in range(len(str2) + 1)] for j in range(len(str1) + 1)]

    # initialize M
    M = [[0 for i in range(len(str2) + 1)] for j in range(len(str1) + 1)]
    M[0][1] = -(open_penalty)
    M[1][0] = -(open_penalty)
    for i in range (2, len(str1)+1):
        M[i][0] = M[i-1][0]-extension_penalty
    for j in range (2, len(str2)+1):
        M[0][j] = M[0][j-1]-extension_penalty

    # initialize L
    L = [[0 for i in range(len(str2) + 1)] for j in range(len(str1) + 1)]
    L[1][0] = -(open_penalty)
    for i in range (2, len(str1)+1):
        L[i][0] = L[i-1][0]-extension_penalty
    for j in range (1, len(str2)+1):
        L[0][j] = float("-inf")

    T = [[0 for i in range(len(str2) + 1)] for j in range(len(str1) + 1)]
    T[0][1] = -(open_penalty)
    for i in range (1, len(str1)+1):
        T[i][0] = float("-inf")
    for j in range (2, len(str2)+1):
        T[0][j] = T[0][j-1]-extension_penalty

    for i in range(1, len(str1)+1):
        for j in range(1, len(str2)+1):
            T[i][j] = max((T[i][j-1]-extension_penalty),(M[i][j-1]-open_penalty))
            L[i][j] = max((L[i-1][j]-extension_penalty),(M[i-1][j]-open_penalty))
            index_one = letters.index(str1[i-1])
            index_two = letters.index(str2[j-1])
            M[i][j] = max((L[i][j]),(M[i-1][j-1]+scoring_matrix[index_one][index_two]),T[i][j])

            #fix backtrack
            check = max(L[i][j],T[i][j],M[i-1][j-1]+scoring_matrix[index_one][index_two])
            if check == L[i][j]:
                backtrack[i][j] = "D"
            elif check == T[i][j]:
                backtrack[i][j] = "R"
            elif check == M[i-1][j-1]+scoring_matrix[index_one][index_two]:
                backtrack[i][j] = "DIAG"
    return backtrack, M[len(str1)][len(str2)]

def allign_with_affine_gap(str1, str2, scoring_matrix, letters, open_penalty, extension_penalty):
    allign = []
    allign_two = []
    backtrack, score = backtracker(str1, str2, open_penalty, extension_penalty, scoring_matrix, letters)
    i = len(str1)
    j = len(str2)

    while i > 0 and j > 0:
        if backtrack[i][j] == "DIAG":
            allign.append(str1[i-1])
            allign_two.append(str2[j-1])
            i = i-1
            j = j-1
        elif backtrack[i][j] == "D":
            allign.append(str1[i-1])
            allign_two.append("-")
            i = i-1
        elif backtrack[i][j] == "R" :
            allign.append("-")
            allign_two.append(str2[j-1])
            j = j-1

    allign = allign[::-1]
    allign_two = allign_two[::-1]

    allign_one = "".join(allign)
    allign_two = "".join(allign_two)

    return score, allign_one, allign_two

if __name__== "__main__":
    with open("Chapter 5\BLOSUM62") as f:
        lines = [line.strip() for line in f]
    new_lines = []
    for each in lines:
        new = each.replace("  ", " ")
        new = new.replace(" ", ",")
        new_lines.append(new)

    letters = ['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y']
    scoring_matrix = []
    open_penalty = 11
    extension_penalty = 1
    for l in new_lines:
        scoring_matrix.append( [ int (x) for x in l.split(',') ] )
    # with open("Chapter 5\input.txt") as f:
    #     patterns = [line.strip() for line in f]
    # score, str1, str2 = allign_with_affine_gap(patterns[0], patterns[1], scoring_matrix, letters, open_penalty, extension_penalty)
    # print (score)
    # print (str1)
    # print (str2)

    print (allign_with_affine_gap("PRTEINS", "PRTWPSEIN", scoring_matrix, letters, open_penalty, extension_penalty,))
