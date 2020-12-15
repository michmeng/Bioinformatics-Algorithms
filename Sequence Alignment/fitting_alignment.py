def backtracker(str1,str2):
    backtrack = [[0 for i in range(len(str2) + 1)] for j in range(len(str1) + 1)]
    #initialize matrix and 0 row and column
    score = [[0 for i in range(len(str2) + 1)] for j in range(len(str1) + 1)]
    max_score = 0
    max_location = []

    for j in range (1, len(str2)+1):
        score[0][j] = score[0][j-1]-1

    for i in range(1, len(str1)+1):
        for j in range(1, len(str2)+1):
            check1 = score[i-1][j] - 1
            check2 = score[i][j-1] - 1
            if str1[i-1] == str2[j-1]:
                add = 1
            else:
                add = -1
            check3 = score[i-1][j-1] + add
            score[i][j] = max(check1, check2, check3)
            if score[i][j] == score[i-1][j] - 1:
                backtrack[i][j] = "D"
            elif score[i][j] == score[i][j-1] - 1:
                backtrack[i][j] = "R"
            elif score[i][j] == score[i-1][j-1] + add:
                backtrack[i][j] = "DIAG"
    max_position = []
    for each in score:
        if each[-1] >= max_score:
            max_score = each[-1]
            max_position = []
            max_position.append(score.index(each))
            max_position.append(len(str2))
    return backtrack, max_score, max_position

def fitting_allignment(str1,str2):
    f_allign = []
    f_allign_two = []
    if len(str1) > len(str2):
        l_string = str1
        s_string = str2
    else:
        l_string = str2
        s_string = str1

    backtrack, max_score, max_location = backtracker(l_string,s_string)
    i = max_location[0]
    j = max_location[1]
    allignment = ""

    check = False
    while i > 0 and j > 0:
        if backtrack[i][j] == "DIAG":
            f_allign.append(l_string[i-1])
            f_allign_two.append(s_string[j-1])
            i = i-1
            j = j-1
        elif backtrack[i][j] == "D":
            f_allign.append(l_string[i-1])
            f_allign_two.append("-")
            i = i-1
        elif backtrack[i][j] == "R" :
            f_allign.append("-")
            f_allign_two.append(s_string[j-1])
            j = j-1
        elif backtrack[i][j] == 0:
            break


    f_allign = f_allign[::-1]
    f_allign_two = f_allign_two[::-1]


    allign_one = "".join(f_allign)
    allign_two = "".join(f_allign_two)

    if len(str1) > len(str2):
        str1 = allign_one
        str2 = allign_two
    else:
        str2 = allign_one
        str1 = allign_two

    return max_score, str1, str2


if __name__== "__main__":
    # with open("Chapter 5\input.txt") as f:
    #     patterns = [line.strip() for line in f]
    patterns = ["BRISTOL", "MYERS"]
    score, str1, allignment =  fitting_allignment(patterns[0], patterns[1])
    print (score)
    print (str1)
    print (allignment)
