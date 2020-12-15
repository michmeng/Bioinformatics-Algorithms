def rev_compliment(str):
    compl = ""
    for c in str:
        if c == "A":
            compl += "T"
        if c == "T":
            compl += "A"
        if c == "C":
            compl += "G"
        if c == "G":
            compl += "C"
    rev_compl = ""
    for c in compl:
        rev_compl = c + rev_compl
    return rev_compl

def shared_kmers(k, str1, str2):
    str1_dict = {}
    str2_dict = {}
    str2_revcomp_dict = {}
    for i in range(len(str1)-k+1):
        k_mer = str1[i:i+k]
        if k_mer in str1_dict.keys():
            str1_dict[k_mer].append(i)
        else:
            str1_dict.update({k_mer: [i]})
    for i in range(len(str2)-k+1):
        k_mer = str2[i:i+k]
        k_mer_revcomp = rev_compliment(k_mer) + "*"
        k_mer = k_mer + "*"
        if k_mer in str2_dict.keys():
            str2_dict[k_mer].append(i)
        else:
            str2_dict.update({k_mer: [i]})
        if k_mer_revcomp in str2_revcomp_dict.keys():
            str2_revcomp_dict[k_mer_revcomp].append(i)
        else:
            str2_revcomp_dict.update({k_mer_revcomp: [i]})

    all_kmers = []
    for key,v in str1_dict.items():
        all_kmers.append((key,v))
    for key,v in str2_dict.items():
        all_kmers.append((key,v))
    for key,v in str2_revcomp_dict.items():
        all_kmers.append((key,v))

    all_kmers.sort(key=lambda x: x[0])

    results = []


    while len(all_kmers) > 0:
        add = 0
        initial = all_kmers[0]
        initial_kmer = all_kmers[0][0]
        add = add + 1
        if len(initial_kmer) != k + 1:
            for i in range(1, len(all_kmers)):
                if  all_kmers[i][0] == initial_kmer + "*":
                    results.append((initial[1], all_kmers[i][1]))
                    add = add + 1
                else:
                    break

        for i in range(add):
            all_kmers.pop(0)

    s_kmers = []
    for each in results:
        for i in range(len(each[0])):
            for j in range(len(each[1])):
                s_kmers.append((each[0][i], each[1][j]))

    return s_kmers

if __name__== "__main__":
    with open("Chapter 6\input.txt") as f:
        lines = [line.strip() for line in f]
    k = int(lines[0])
    str1 = lines[1]
    str2 = lines[2]
    results = shared_kmers(k, str1, str2)
    for each in results:
        print (each)
