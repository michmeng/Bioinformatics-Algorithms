def manhattan_tourist(n,m,down,right):
    score = [ [ 0 for i in range(m+1) ] for j in range(n+1) ]
    for i in range(1, n+1):
        score[i][0] = int(score[i-1][0]) + int(down[i-1][0])
    for j in range(1, m+1):
        score[0][j] = int(score[0][j-1]) + int(right[0][j-1])
    for i in range(1, n+1):
        for j in range(1, m+1):
            check_one = int(score[i-1][j]) + int(down[i-1][j])
            check_two = int(score[i][j-1]) + int(right[i][j-1])
            score[i][j] = max(check_one, check_two)
    return score[n][m]

if __name__== "__main__":
    down = []
    right = []
    with open("Chapter 5\input.txt") as f:
        lines = [line.rstrip() for line in f]
    divide = lines.index("-")
    for i in range(0, divide):
        add = []
        new = "".join(lines[i].split())
        for each in new:
            add.append(each)
        down.append(add)
    for i in range(divide+1, len(lines)):
        add = []
        new = "".join(lines[i].split())
        for each in new:
            add.append(each)
        right.append(add)
    # print (manhattan_tourist())
