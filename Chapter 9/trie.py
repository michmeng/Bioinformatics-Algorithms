class TrieNode():

    def __init__(self, data, count):
        self.children = {}
        self.data = data
        self.count = count
        self.terminate = False

class Trie():

    def __init__(self):
        self.root = TrieNode("*", 0)

    def insert(self, pattern, count):
        # count = 1
        curr = self.root
        for each in pattern:
            if each not in curr.children:
                curr.children[each] = TrieNode(each, count)
                count = count + 1
                # print (str(curr.count) + '->' + str(curr.children[each].count) + ":" + str(curr.children[each].data))
            curr = curr.children[each]
        curr.terminate = True
        return count

    def search(self, pattern):
        curr = self.root
        while len(pattern) > 0:
            each = pattern[0]
            if each not in curr.children:
                return False
            curr = curr.children[each]
            pattern = pattern[1:]
        return True
