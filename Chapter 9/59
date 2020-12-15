def bwt(text):
    rotations = []
    suff = ""
    while len(text) > 0:
        add = text + suff
        rotations.append(add)
        suff = suff + text[0]
        text = text[1:]
    rotations.sort()
    transformation = ""
    for each in rotations:
        transformation = transformation + each[-1]
    return transformation

if __name__ == "__main__":
    with open("Chapter 9\input.txt") as f:
        line = f.readline().rstrip()

    print (bwt(line))
