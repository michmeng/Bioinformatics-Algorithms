import sys
sys.setrecursionlimit(15000)

def calculate_score(str1, str2, top, bottom, left, right, scoring_matrix, letters, penalty):
    mid = ((left + right)//2)
    score = [[0 for i in range((right-left)+1)] for j in range((bottom-top)+1)]
    score_reverse = [[0 for i in range((right-left)+1)] for j in range((bottom-top)+1)]
    sum = [[0 for i in range((right-left)+1)] for j in range((bottom-top)+1)]

    for i in range (1, ((bottom-top)+1)):
        score[i][0] = score[i-1][0]-penalty
        score_reverse[i][0] = score[i-1][0]-penalty
        sum[i][0] = score[i][0] + score_reverse[i][0]
    for j in range (1, (right-left)+1):
        score[0][j] = score[0][j-1]-penalty
        score_reverse[0][j] = score[0][j-1]-penalty
        sum[0][j]= score[0][j] + score_reverse[0][j]

    str1_reverse = str1[::-1]
    str2_reverse = str2[::-1]

    for i in range(1, (bottom-top)+1):
        for j in range(1, (right-left)+1):
            check1 = score[i-1][j] - penalty
            check2 = score[i][j-1] - penalty
            index_one = letters.index(str1[i-1])
            index_two = letters.index(str2[j-1])
            check3 = score[i-1][j-1] + scoring_matrix[index_two][index_one]
            score[i][j] = max(check1, check2, check3)
            check1 = score_reverse[i-1][j] - penalty
            check2 = score_reverse[i][j-1] - penalty
            index_one = letters.index(str1_reverse[i-1])
            index_two = letters.index(str2_reverse[j-1])
            check3 = score_reverse[i-1][j-1] + scoring_matrix[index_two][index_one]
            score_reverse[i][j] = max(check1, check2, check3)

    fix_reverse = []
    for each in score_reverse:
        new_each = each[::-1]
        fix_reverse.append(new_each)
    fix_reverse = fix_reverse[::-1]

    for i in range(0, (bottom-top)+1):
        for j in range(0, (right-left)+1):
            sum[i][j] = int(score[i][j]) + int(fix_reverse[i][j])

    return sum[bottom][right], sum


def middle_edge(str1, str2, top, bottom, left, right, scoring_matrix, letters, penalty, sum):
    mid = ((left + right)//2)
    maxim = float("-inf")
    max_x = None
    for each in sum:
        if each[mid] >= maxim:
            maxim = each[mid]
            max_x = sum.index(each)
    max_position = [max_x, mid]

    if max_position[0] == bottom :
        if sum[max_position[0]][max_position[1]+1] ==  maxim:
            return list(max_position), [max_position[0],max_position[1]+1]
        elif sum[max_position[0]+1][max_position[1]+1] ==  maxim:
            return list(max_position), [max_position[0]+1,max_position[1]+1]
    elif max_position[1] == right:
        if sum[max_position[0]+1][max_position[1]] == maxim:
            return list(max_position),[max_position[0]+1,max_position[1]]
    else:
        if sum[max_position[0]][max_position[1]+1] ==  maxim:
            return list(max_position), [max_position[0],max_position[1]+1]
        elif sum[max_position[0]+1][max_position[1]+1] ==  maxim:
            return list(max_position), [max_position[0]+1,max_position[1]+1]
        elif sum[max_position[0]+1][max_position[1]] == maxim:
            return list(max_position), [max_position[0]+1,max_position[1]]

    return list(max_position), list(edge_to)

def mid_edge_symbol(start, end):
    if start[0] == end[0] - 1 and start[1] == end[1]:
        return "right"
    elif start[0] == end[0] and start[1] == end[1] - 1:
        return "down"
    elif start[0] == end[0] - 1 and start[1] == end[1] - 1:
        return "diag"

def mid_edge_change(start, end):
    if start[0] == end[0] - 1 and start[1] == end[1]:
        return "H"
    elif start[0] == end[0] and start[1] == end[1] - 1:
        return "V"
    elif start[0] == end[0] - 1 and start[1] == end[1] - 1:
        return "D"

def linear_alignment(str1, str2, top, bottom, left, right, scoring_matrix, letters, penalty, sum):
    if left == right:
        file1.write("V"*(bottom-top))
        return
    if top == bottom:
        file1.write("H"*(right-left))
        return
    middle = (left + right)//2
    mid_node, mid_edge = middle_edge(str1[top:bottom], str2[left:right], 0, len(str1[top:bottom]), 0, len(str2[left:right]), scoring_matrix, letters, penalty, sum)
    # mid_node, mid_edge = middle_edge(str1, str2, top, bottom, left, right, scoring_matrix, letters, penalty, sum)
    mid_node[0] = mid_node[0] + top
    mid_node[1] = mid_node[1] + left
    mid_edge[0] = mid_edge[0] + top
    mid_edge[1] = mid_edge[1] + left
    linear_alignment(str1, str2, top, mid_node[0], left, middle, scoring_matrix, letters, penalty, sum)
    file1.write(mid_edge_change(mid_node,mid_edge))
    if mid_edge_symbol(mid_node, mid_edge)  == "right" or  mid_edge_symbol(mid_node, mid_edge)  == "diag":
        middle = middle + 1
    if mid_edge_symbol(mid_node, mid_edge)  == "down" or  mid_edge_symbol(mid_node, mid_edge)  == "diag":
        mid_node[0] = mid_node[0] + 1
    linear_alignment(str1, str2, mid_node[0], bottom, middle, right, scoring_matrix, letters, penalty, sum)

def align(directions, str1, str2):
    allign_one = ""
    allign_two = ""

    for each in directions:
        if each == "H":
            allign_two =  allign_two + str2[0]
            allign_one =  allign_one + "-"
            str2 = str2[1:]
        elif each == "V":
            allign_two = allign_two + "-"
            allign_one = allign_one + str1[0]
            str1 = str1[1:]
        elif each == "D":
            allign_two = allign_two + str2[0]
            allign_one = allign_one + str1[0]
            str2 = str2[1:]
            str1 = str1[1:]
    # print (allign_one)
    # print (allign_two)
    return allign_one, allign_two

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

    with open("Chapter 5\input.txt") as f:
        lines = [line.strip() for line in f]

    file1 = open("Chapter 5\output.txt", 'w')
    file_out = open("Chapter 5\hello.txt", 'w')

    # score, mid_node, mid_edge = middle_edge("PLEASANTLY","MEANLY", 0, len("PLEASANTLY"), 0, len("MEANLY"), scoring_matrix, letters, penalty)
    print ("one")
    score, sum = calculate_score(lines[0], lines[1], 0, len(lines[0]), 0, len(lines[1]), scoring_matrix, letters, penalty)
    print ("two")
    file_out.write(str(score) + "\n")
    # linear_alignment( "PLEASANTLY","MEANLY", 0, len("PLEASANTLY"), 0, len("MEANLY"), scoring_matrix, letters, penalty
    linear_alignment(lines[0], lines[1], 0, len(lines[0]), 0, len(lines[1]), scoring_matrix, letters, penalty, sum)
    print ("three")
    file1.close()

    directions = [ch for ch in open('Chapter 5\output.txt').read() if ch != '\n' if ch != ' ']
    # print (directions)

    allign_one, allign_two = align(directions, lines[0], lines[1])
    file_out.write(allign_one + "\n")
    file_out.write(allign_two)
