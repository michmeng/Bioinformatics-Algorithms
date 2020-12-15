def string_from_genome_path(patterns):
    result = ""
    result = result + str(patterns[0])
    for i in range(1, len(patterns)):
        result = result + str(patterns[i][-1])
    return result

# if __name__== "__main__":
#     with open("Chapter 3\input.txt") as f:
#         lines = [line.rstrip() for line in f]
#     print (string_from_genome_path(lines))
