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

def longest_shared_substring(text, trie):
    #find longest purple path
    purple_paths = []
    for each in trie.root.children:
        if trie.root.children[each].color == "P":
            purple_paths.append((trie.root.children[each], trie.root))

    lss = ""
    curr = purple_paths[0]
    purple_paths.pop(0)


    while curr[0].color == "P":
        curr[0].lss = curr[1].lss + text[curr[0].index: curr[0].index + curr[0].length]
        for each in curr[0].children:
            if curr[0].children[each].color == "P":
                purple_paths.append((curr[0].children[each], curr[0]))
        curr_lss = curr[0].lss
        if len(curr_lss) > len(lss):
            lss = curr_lss

        if len(purple_paths) > 0:
            curr = purple_paths.pop(0)
        else:
            break


    print ("LSS:  " + str(lss))
    return

if __name__ == "__main__":
    with open("Chapter 9\input.txt") as f:
        strings = [line.rstrip() for line in f]

    strings[0] = strings[0] + "#"
    strings[1] = strings[1] + "$"
    text = strings[0] + strings[1]

    suffixes = suffix(text)
    t = SuffixTrie()
    count = 1
    for word in suffixes:
        count = t.insert(word[0], count, word[1])

    paths = t.paths
    initial_paths = t.non_branching_paths()
    t.construct_tree(text)

    t.color_tree(t.root)

    longest_shared_substring(text, t)
