def hamming_dist(str1, str2):
    mismatch = 0
    #should prob check if len(str1) == len(str2)
    for i in range(len(str1)):
        c1 = str1[i]
        c2 = str2[i]
        if c1 != c2:
            mismatch += 1
    return mismatch

def approx_matching(pattern, text, d):
    result = ""
    for i in range(len(text) - len(pattern) + 1):
        check = text[i:(i+len(text))]
        if hamming_dist(pattern, check) <= d:
            result = result + str(i) + " "
    return result

#print (approx_matching("","", ))
