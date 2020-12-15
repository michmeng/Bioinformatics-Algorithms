def backtracker(str1, str2):
    score = [[0 for i in range(len(str2) + 1)] for j in range(len(str1) + 1)]
    backtrack = [[0 for i in range(len(str2) + 1)] for j in range(len(str1) + 1)]

    for i in range(1, len(str1)+1):
        for j in range(1, len(str2)+1):
            check1 = score[i-1][j]
            check2 = score[i][j-1]
            add = 0
            if str1[i-1] == str2[j-1]:
                add = 1
            check3 = score[i-1][j-1] + add
            score[i][j] = max(check1, check2, check3)
            if score[i][j] == score[i-1][j]:
                backtrack[i][j] = "D"
            elif score[i][j] == score[i][j-1]:
                backtrack[i][j] = "R"
            elif score[i][j] == score[i-1][j-1] + add:
                backtrack[i][j] = "DIAG"
    return backtrack

def longest_common_subseq(str1, str2):
    longest_common = []
    backtrack = backtracker(str1, str2)
    i = len(str1)
    j = len(str2)
    while i > 0 and j > 0:
        if backtrack[i][j] == "DIAG":
            longest_common.append(str1[i-1])
            i = i-1
            j = j-1
        elif backtrack[i][j] == "D":
            i = i-1
        else:
            j = j-1
    result = ""
    for each in longest_common[::-1]:
        result = result + each
    return result

if __name__== "__main__":
    # with open("Chapter 5\input.txt") as f:
    #     lines = [line.rstrip() for line in f]
    # str1 = lines[0]
    # str2 = lines[1]
    # print (longest_common_subseq(str1,str2))
    print (longest_common_subseq("BCADB", "BDCBA"))
