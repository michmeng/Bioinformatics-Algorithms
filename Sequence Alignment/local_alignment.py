def backtracker(str1,str2,penalty,scoring_matrix,letters):
    backtrack = [[0 for i in range(len(str2) + 1)] for j in range(len(str1) + 1)]
    #initialize matrix and 0 row and column
    score = [[0 for i in range(len(str2) + 1)] for j in range(len(str1) + 1)]
    max_score = 0
    max_location = []

    for i in range(1, len(str1)+1):
        for j in range(1, len(str2)+1):
            check1 = score[i-1][j] - 5
            check2 = score[i][j-1] - 5
            index_one = letters.index(str1[i-1])
            index_two = letters.index(str2[j-1])
            check3 = score[i-1][j-1] + scoring_matrix[index_two][index_one]
            score[i][j] = max(0, check1, check2, check3)
            #fix backtrack
            if score[i][j] >= max_score:
                max_score = score[i][j]
                max_location = []
                max_location.append(i)
                max_location.append(j)
            if score[i][j] == score[i-1][j] - 5:
                backtrack[i][j] = "D"
            elif score[i][j] == score[i][j-1] - 5:
                backtrack[i][j] = "R"
            elif score[i][j] == score[i-1][j-1] + scoring_matrix[index_two][index_one]:
                backtrack[i][j] = "DIAG"

    return backtrack, max_score, max_location

def local_allignment(str1,str2,penalty,scoring_matrix,letters):
    l_allign = []
    l_allign_two = []
    if len(str1) > len(str2):
        l_string = str1
        s_string = str2
    else:
        l_string = str2
        s_string = str1

    backtrack, max_score, max_location = backtracker(l_string,s_string,penalty,scoring_matrix, letters)
    i = max_location[0]
    j = max_location[1]
    allignment = ""

    check = False
    while i > 0 and j > 0:
        if backtrack[i][j] == "DIAG":
            l_allign.append(l_string[i-1])
            l_allign_two.append(s_string[j-1])
            i = i-1
            j = j-1
        elif backtrack[i][j] == "D":
            l_allign.append(l_string[i-1])
            l_allign_two.append("-")
            i = i-1
        elif backtrack[i][j] == "R" :
            l_allign.append("-")
            l_allign_two.append(s_string[j-1])
            j = j-1
        elif backtrack[i][j] == 0:
            break


    l_allign = l_allign[::-1]
    l_allign_two = l_allign_two[::-1]


    allign_one = "".join(l_allign)
    allign_two = "".join(l_allign_two)

    if len(str1) > len(str2):
        str1 = allign_one
        str2 = allign_two
    else:
        str2 = allign_one
        str1 = allign_two

    return max_score, str1, str2

if __name__== "__main__":
    with open("Chapter 5\PAM250") as f:
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
    with open("Chapter 5\input.txt") as f:
        patterns = [line.strip() for line in f]
    score, str1, allignment =  local_allignment(patterns[0], patterns[1], 5, scoring_matrix, letters)
    print (score)
    print (str1)
    print (allignment)
