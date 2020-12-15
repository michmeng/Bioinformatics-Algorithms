def backtracker(str1,str2):
    backtrack = [[0 for i in range(len(str2) + 1)] for j in range(len(str1) + 1)]
    #initialize matrix and 0 row and column
    score = [[0 for i in range(len(str2) + 1)] for j in range(len(str1) + 1)]
    max_score = 0
    max_location = []

    for j in range (1, len(str2)+1):
        score[0][j] = score[0][j-1]-2

    for i in range(1, len(str1)+1):
        for j in range(1, len(str2)+1):
            check1 = score[i-1][j] - 2
            check2 = score[i][j-1] - 2
            if str1[i-1] == str2[j-1]:
                add = 1
            else:
                add = -2
            check3 = score[i-1][j-1] + add
            score[i][j] = max(check1, check2, check3)
            if score[i][j] == score[i-1][j] - 2:
                backtrack[i][j] = "D"
            elif score[i][j] == score[i][j-1] - 2:
                backtrack[i][j] = "R"
            elif score[i][j] == score[i-1][j-1] + add:
                backtrack[i][j] = "DIAG"

    max_position = []
    for each in score[-1]:
        if each >= max_score:
            max_score = each
            max_position = []
            max_position.append(len(score)-1)
            max_position.append(score[-1].index(max_score))

    return backtrack, max_score, max_position

def overlap_allignment(str1,str2):
    o_allign = []
    o_allign_two = []

    # backtrack, max_score, max_location = backtracker(l_string,s_string)
    backtrack, max_score, max_location = backtracker(str1,str2)
    i = max_location[0]
    j = max_location[1]
    allignment = ""

    check = False
    while i > 0 and j > 0:
        if backtrack[i][j] == "DIAG":
            o_allign.append(str1[i-1])
            o_allign_two.append(str2[j-1])
            i = i-1
            j = j-1
        elif backtrack[i][j] == "D":
            o_allign.append(str1[i-1])
            o_allign_two.append("-")
            i = i-1
        elif backtrack[i][j] == "R" :
            o_allign.append("-")
            o_allign_two.append(str2[j-1])
            j = j-1
        elif backtrack[i][j] == 0:
            break


    o_allign = o_allign[::-1]
    o_allign_two = o_allign_two[::-1]


    allign_one = "".join(o_allign)
    allign_two = "".join(o_allign_two)

    return max_score, allign_one, allign_two

if __name__== "__main__":
    # with open("Chapter 5\input.txt") as f:
    #     patterns = [line.strip() for line in f]
    patterns = ["BRISTOL", "BURPS"]
    score, str1, allignment =  overlap_allignment(patterns[0], patterns[1])
    print (score)
    print (str1)
    print (allignment)
