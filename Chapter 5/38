def middle_edge(str1,str2,scoring_matrix,letters,penalty):
    mid = len(str2)//2
    score = [[0 for i in range(len(str2) + 1)] for j in range(len(str1) + 1)]
    score_reverse = [[0 for i in range(len(str2) + 1)] for j in range(len(str1) + 1)]
    sum = [[0 for i in range(len(str2) + 1)] for j in range(len(str1) + 1)]

    for i in range (1, len(str1)+1):
        score[i][0] = score[i-1][0]-5
        score_reverse[i][0] = score[i-1][0]-5
        sum[i][0] = score[i][0] + score_reverse[i][0]
    for j in range (1, len(str2)+1):
        score[0][j] = score[0][j-1]-5
        score_reverse[0][j] = score[0][j-1]-5
        sum[0][j] = score[0][j] + score_reverse[0][j]

    for i in range(1, len(str1)+1):
        for j in range(1, len(str2)+1):
            check1 = score[i-1][j] - 5
            check2 = score[i][j-1] - 5
            index_one = letters.index(str1[i-1])
            index_two = letters.index(str2[j-1])
            check3 = score[i-1][j-1] + scoring_matrix[index_two][index_one]
            score[i][j] = max(check1, check2, check3)

    str1_reverse = str1[::-1]
    str2_reverse = str2[::-1]

    for i in range(1, len(str1_reverse)+1):
        for j in range(1, len(str2_reverse)+1):
            check1 = score_reverse[i-1][j] - 5
            check2 = score_reverse[i][j-1] - 5
            index_one = letters.index(str1_reverse[i-1])
            index_two = letters.index(str2_reverse[j-1])
            check3 = score_reverse[i-1][j-1] + scoring_matrix[index_two][index_one]
            score_reverse[i][j] = max(check1, check2, check3)

    fix_reverse = []
    for each in score_reverse:
        new_each = each[::-1]
        fix_reverse.append(new_each)
    fix_reverse = fix_reverse[::-1]

    for i in range(0, len(str1_reverse)+1):
        for j in range(0, len(str2_reverse)+1):
            sum[i][j] = int(score[i][j]) + int(fix_reverse[i][j])

    # for each in sum:
    #     print (each)

    maxim = float("-inf")
    max_position = []
    max_position.append(mid)
    max_position.append(None)
    for each in sum:
        if each[mid] > maxim:
            maxim = each[mid]
            max_position.pop(1)
            max_position.append(sum.index(each))

    max_position = max_position[::-1]

    edge_to = []
    if sum[max_position[0]+1][max_position[1]] == maxim:
        edge_to.append(max_position[0]+1)
        edge_to.append(max_position[1])
    elif sum[max_position[0]][max_position[1]+1] ==  maxim:
        edge_to.append(max_position[0])
        edge_to.append(max_position[1]+1)
    elif sum[max_position[0]+1][max_position[1]+1] ==  maxim:
        edge_to.append(max_position[0]+1)
        edge_to.append(max_position[1]+1)

    return tuple(max_position), tuple(edge_to)


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
    penalty = 5
    for l in new_lines:
        scoring_matrix.append( [ int (x) for x in l.split(',') ] )
    # with open("Chapter 5\input.txt") as f:
    #     patterns = [line.strip() for line in f]
    # max_position, edge_to = middle_edge(patterns[0], patterns[1], scoring_matrix, letters, penalty)
    max_position, edge_to = middle_edge("GAGA" , "GAT", scoring_matrix, letters, penalty)
    print (max_position)
    print (edge_to)
