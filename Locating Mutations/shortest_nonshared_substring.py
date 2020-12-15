from trie import TrieNode
from trie import Trie

def suffix(text):
    suffixes = []
    count = 0
    while len(text) > 0:
        suffixes.append((text, count))
        text = text[1:]
        count = count + 1
    return suffixes

def string_composition(text, k):
    k_mers = []
    for i in range(0,len(text)-k+1):
        add = text[i:i+k]
        k_mers.append(add)
    # k_mers.sort()
    return k_mers

def all_kmers(text):
    l = len(text)
    k_mers = []
    for i in range(2, l+1):
        add = string_composition(text, i)
        for each in add:
            k_mers.append(each)
    return k_mers

if __name__ == "__main__":
    with open("Chapter 9\input.txt") as f:
        strings = [line.rstrip() for line in f]

    suffixes = suffix(strings[1])

    t = Trie()
    count = 1
    for word in suffixes:
        count = t.insert(word[0], count)


    check = all_kmers(strings[0])
    while len(check) > 0:
        curr = check[0]
        if t.search(curr) == False:
            print (curr)
            break
        check.pop(0)
