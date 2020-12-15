def suffix_array(text):
    suffixes = []
    count = 0
    while len(text) > 0:
        suffixes.append((text, count))
        text = text[1:]
        count = count + 1
    suffixes.sort()
    results = ""
    for each in suffixes:
        results = results + str(each[1]) + ", "
    results = results[:-2]
    return results

if __name__ == "__main__":
    with open("Chapter 9\input.txt") as f:
        line = f.readline().rstrip()

    print (suffix_array(line))
