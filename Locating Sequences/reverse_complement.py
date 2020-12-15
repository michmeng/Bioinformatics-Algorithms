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

#print (rev_compliment(""))
