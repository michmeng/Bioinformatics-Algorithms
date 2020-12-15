def most_freq_words(text, k):
    all_pat = {}
    for i in (range(len(text) - k + 1)):
        pattern = text[i:(i+k)]
        if pattern in all_pat:
            all_pat[pattern] = all_pat.get(pattern) + 1
        else:
            all_pat[pattern] = 1
    result = ""
    max = 0
    for i in all_pat:
        if all_pat[i] > max:
            max = all_pat[i]
    for i in all_pat:
        if all_pat[i] == max:
            result = result + i + " "
    return result

#print (most_freq_words( ))
