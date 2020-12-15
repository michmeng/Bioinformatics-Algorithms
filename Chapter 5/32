def backtracker(str1,str2,penalty,scoring_matrix,letters):
    backtrack = [[0 for i in range(len(str2) + 1)] for j in range(len(str1) + 1)]
    #initialize matrix and 0 row and column

    for i in range (1, len(str1)+1):
        for j in range (1, len(str2)+1):
                backtrack[i][0] = "R"
                backtrack[0][j] = "D"

    score = [[0 for i in range(len(str2) + 1)] for j in range(len(str1) + 1)]
    for i in range (1, len(str1)+1):
        score[i][0] = score[i-1][0]-5
    for j in range (1, len(str2)+1):
        score[0][j] = score[0][j-1]-5

    for i in range(1, len(str1)+1):
        for j in range(1, len(str2)+1):
            check1 = score[i-1][j] - 5
            check2 = score[i][j-1] - 5
            index_one = letters.index(str1[i-1])
            index_two = letters.index(str2[j-1])
            check3 = score[i-1][j-1] + scoring_matrix[index_two][index_one]
            score[i][j] = max(check1, check2, check3)
            #fix backtrack
            if score[i][j] == score[i-1][j] - 5:
                backtrack[i][j] = "D"
            elif score[i][j] == score[i][j-1] - 5:
                backtrack[i][j] = "R"
            elif score[i][j] == score[i-1][j-1] + scoring_matrix[index_two][index_one]:
                backtrack[i][j] = "DIAG"

    return backtrack, score[len(str1)][len(str2)]

def global_allignment(str1,str2,penalty,scoring_matrix,letters):
    g_allign = []
    g_allign_two = []
    if len(str1) > len(str2):
        l_string = str1
        s_string = str2
    else:
        l_string = str2
        s_string = str1

    # l_string = str1
    # s_string = str2

    backtrack, score = backtracker(l_string,s_string,penalty,scoring_matrix, letters)
    i = len(l_string)
    j = len(s_string)
    allignment = ""

    while i > 0 and j > 0:
        if backtrack[i][j] == "DIAG":
            g_allign.append(l_string[i-1])
            g_allign_two.append(s_string[j-1])
            i = i-1
            j = j-1
        elif backtrack[i][j] == "D":
            g_allign.append(l_string[i-1])
            g_allign_two.append("-")
            i = i-1
        elif backtrack[i][j] == "R" :
            g_allign.append("-")
            g_allign_two.append(s_string[j-1])
            j = j-1

    g_allign = g_allign[::-1]
    g_allign_two = g_allign_two[::-1]

    if g_allign[0] != l_string[0] or g_allign_two[0] != s_string[0]:
        if g_allign[0] != l_string[0]:
            g_allign.insert(0, l_string[0])
            g_allign_two.insert(0, "-")
        elif g_allign_two[0] != s_string[0]:
            print ("hello")
            g_allign_two.insert(0, s_string[0])
            g_allign.insert(0, "-")

    allign_one = "".join(g_allign)
    allign_two = "".join(g_allign_two)

    if len(str1) > len(str2):
        str1 = allign_one
        str2 = allign_two
    else:
        str2 = allign_one
        str1 = allign_two

    return score, str1, str2

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
    for l in new_lines:
        scoring_matrix.append( [ int (x) for x in l.split(',') ] )
    # with open("Chapter 5\input.txt") as f:
    #     patterns = [line.strip() for line in f]
    # score, str1, allignment =  global_allignment(patterns[0], patterns[1], 5, scoring_matrix, letters)
    score, str1, allignment =  global_allignment("RISTOL", "RISTLES", 5, scoring_matrix, letters)
    print (score)
    print (str1)
    print (allignment)
