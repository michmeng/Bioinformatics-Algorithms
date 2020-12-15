from trie import TrieNode
from trie import Trie

if __name__ == "__main__":
    with open("Chapter 9\input.txt") as f:
        strings = [line.rstrip() for line in f]

    t = Trie()
    count = 1
    for word in strings:
        count = t.insert(word, count)
