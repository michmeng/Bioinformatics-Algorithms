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

def longest_repeat(text, tree):
    answer = ""
    curr = tree.root
    curr.repeat = ""
    starts = []
    for each in curr.children:
        starts.append((curr.children[each], curr))
    while len(starts) > 0:
        curr = starts[0]
        if len(curr[0].children) == 0:
            curr[0].repeat = curr[1].repeat
            starts.pop(0)
            continue
        else:
            s = curr[0].index
            e = s + curr[0].length
            check = curr[1].repeat + text[s:e]
            curr[0].repeat = check
            if len(check) > len(answer):
                answer = check
            for each in curr[0].children:
                starts.append((curr[0].children[each], curr[0]))
        starts.pop(0)
    print (answer)
    return


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

    longest_repeat(text, t)
