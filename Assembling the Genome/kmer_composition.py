def string_composition(text, k):
    k_mers = []
    for i in range(0,len(text)-k+1):
        add = text[i:i+k]
        k_mers.append(add)
    k_mers.sort()
    return k_mers

# print (string_composition())
