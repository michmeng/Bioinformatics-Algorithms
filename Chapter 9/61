def first_and_last_column(transform):
    last_column = []
    a_count = 1
    t_count = 1
    c_count = 1
    g_count = 1
    for each in transform:
        if each == "A":
            last_column.append((each,a_count))
            a_count = a_count + 1
        elif each == "T":
            last_column.append((each,t_count))
            t_count = t_count + 1
        elif each == "C":
            last_column.append((each,c_count))
            c_count = c_count + 1
        elif each == "G":
            last_column.append((each,g_count))
            g_count = g_count + 1
        else:
            last_column.append((each, 1))
    first_column = last_column.copy()
    first_column.sort(key=lambda x: x[0])
    return first_column, last_column

def last_to_first_mapping(transform, i):
    first_column, last_column = first_and_last_column(transform)
    symbol = last_column[int(i)]
    return first_column.index(symbol)



if __name__ == "__main__":
    with open("Chapter 9\input.txt") as f:
        strings = [line.rstrip() for line in f]

    transform = strings[0]
    i = strings[1]
    print (last_to_first_mapping(transform, i))
