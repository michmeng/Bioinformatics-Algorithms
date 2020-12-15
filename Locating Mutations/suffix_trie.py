class SuffixTrieNode():

    def __init__(self, data, count, index, length):
        self.children = {}
        self.data = data
        self.count = count
        self.index = index
        self.terminate = False
        self.length = length
        self.repeat = ""
        self.color = "G"
        self.lss = ""

class SuffixTrie():

    def __init__(self):
        self.root = SuffixTrieNode("*", 0, float("-inf"), 0)
        self.paths = []

    def insert(self, pattern, count, start):
        word = []
        curr = self.root
        check = True
        for each in pattern:
            if each not in curr.children:
                curr.children[each] = SuffixTrieNode(each, count, start, 0)
                count = count + 1
            curr = curr.children[each]
            start = start + 1
        curr.terminate = True
        return count

    def non_branching_paths(self):
        starts = []
        curr = self.root
        for each in curr.children:
            starts.append((curr.children[each], curr))
        paths = []
        while len(starts) > 0:
            path = []
            curr = starts[0][0]
            path.append(starts[0][1])
            path.append(starts[0][0])
            while len(curr.children) == 1:
                path.append(list(curr.children.items())[0][1])
                curr = list(curr.children.items())[0][1]

            if len(curr.children) > 1:
                for each in curr.children:
                    starts.append((curr.children[each], curr))

            paths.append(path)
            starts.pop(0)
        self.paths = paths
        return paths
        print (self.paths)

    def construct_tree(self, text):
        for path in self.paths:
            parent = path[0]
            first = path[1]
            position = first.index
            edge_length = len(path) - 1

            curr_parent = parent
            path.pop(0)
            while len(path) > 0:
                curr = path[0]
                curr_parent.children.pop(list(curr_parent.children)[0])
                curr_parent = curr
                path.pop(0)

            parent.children[position] = curr_parent
            parent.children[position].index = position
            parent.children[position].length = edge_length
            s = parent.children[position].index
            e = s + parent.children[position].length
            word = text[s:e]
            if len(parent.children[position].children) == 0:
                if "#" in word:
                    parent.children[position].color = "B"
                else:
                    parent.children[position].color = "R"
            # print (text[s:e])
            # print ("children: " + str(parent.children[position].color))
        return

    def color_tree(self, node):
        if len(node.children) == 0:
            return

        for each in node.children:
            self.color_tree(node.children[each])

        colors = []
        for each in node.children:
            colors.append(node.children[each].color)

        if "B" in colors and "R" in colors:
            node.color = "P"
        elif "P" in colors:
            node.color = "P"
        elif "R" in colors:
            node.color = "R"
        else:
            node.color = "B"
