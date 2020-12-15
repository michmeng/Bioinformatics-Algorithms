from trie import TrieNode
from trie import Trie

def prefix_trie_matching(text, trie, start):
    index = 0
    symbol = text[index]
    init_symbol = symbol
    v = trie.root
    word = ""
    while True:
        if v.terminate:
            return start
        elif symbol in v.children:
            index = index + 1
            word = word + symbol
            v = v.children[symbol]
            symbol = text[index]
        else:
            return "none found"
    return

def trie_matching(text, trie, smallest):
    positions = ""
    start = 0
    while len(text) >= len(smallest):
        result = prefix_trie_matching(text, trie, start)
        if result != "none found":
            positions = positions + str(result) + " "
        text = text[1:]
        start = start + 1
    return positions

if __name__ == "__main__":
    with open("Chapter 9\input.txt") as f:
        strings = [line.rstrip() for line in f]

    text = strings[0]
    text = text + "*"
    strings.pop(0)
    t = Trie()
    count = 1
    for word in strings:
        count = t.insert(word, count)

    smallest = min(strings, key=len)
    print (trie_matching(text, t, smallest))
