from suffix_trie import SuffixTrieNode
from suffix_trie import SuffixTrie

def suffix(text):
    suffixes = []
    count = 0
    while len(text) > 0:
        suffixes.append((text, count))
        text = text[1:]
        count = count + 1
    return suffixes

if __name__ == "__main__":
    with open("Chapter 9\input.txt") as f:
        for text in f:
            text = text.rstrip()

    suffixes = suffix(text)
    t = SuffixTrie()
    count = 1
    for word in suffixes:
        count = t.insert(word[0], count, word[1])

    paths = t.paths

    initial_paths = t.non_branching_paths()

    t.construct_tree(text)

    after_paths = t.non_branching_paths()
