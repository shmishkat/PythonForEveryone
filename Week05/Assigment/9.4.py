

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

dic = dict()
for line in handle:
    if line.startswith("From "):
        line = line.split()
        line = line [1]
        dic[line] = dic.get(line, 0) + 1

bigword = None
bigcount = None

for word, count in dic.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)


        #dic[newLineList[1]] = 1

# print(dic)



