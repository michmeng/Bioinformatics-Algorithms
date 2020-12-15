from bwt_search import *

def get_subpatterns(text, patterns, d):
    all_results = []
    for pattern in patterns:
        length = len(pattern)
        l = len(pattern)//(int(d)+1)
        pat = pattern
        if len(pattern) == 3:
            results = [(pattern[:1], 0, pat), (pattern[1:], 1, pat)]
        else:
            results = []
            count = 0
            while len(pattern) > 0:
                if len(pattern) < l * 2:
                    results.append((pattern, count, pat))
                    count = count + l
                    break
                else:
                    results.append((pattern[:l], count, pat))
                    count = count + l
                    pattern = pattern[l:]
        all_results.append(results)
    return all_results

def hamming_dist(str1, str2):
    mismatch = 0
    #should prob check if len(str1) == len(str2)
    for i in range(len(str1)):
        c1 = str1[i]
        c2 = str2[i]
        if c1 != c2:
            mismatch += 1
    return mismatch

def approx_pattern_match(text, positions, d):
    fin_positions = []
    for position in positions:
        add_positions = []
        for each in position:
            curr = each[1]
            for index in each[0]:
                curr_substring = text[index-curr[1]:index-curr[1]+len(curr[2])]
                if hamming_dist(each[1][2], curr_substring) <= int(d):
                    if (index-curr[1]) not in add_positions:
                        fin_positions.append(index-curr[1])
                    add_positions.append((index-curr[1]))
    return fin_positions

if __name__ == "__main__":
    with open("Chapter 9\input.txt") as f:
        strings = [line.rstrip() for line in f]

    text = strings[0]
    text = text + "$"
    patterns = strings[1].split(" ")
    d = strings[2]

    transform = bwt(text)
    sub_patterns = get_subpatterns(text, patterns, d)
    positions = BWT_matching(text, transform, sub_patterns, 1, 1)
    approx_match = (approx_pattern_match(text, positions, d))
    approx_match = [str(x) for x in approx_match]
    approx_match.sort()
    answer = ""
    for each in approx_match:
        answer = answer + str(each) + " "
    print (answer)
