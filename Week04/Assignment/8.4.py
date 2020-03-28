fname = input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
    listInLine = line.split()

    for i in listInLine:
        if i in lst:
            continue
        else:
            lst.append(i)

lst.sort()
print(lst)

