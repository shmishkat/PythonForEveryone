#the top most common words

file = input('Enter the file name : ')
fileHandler = open(file)

dic = dict()

for line in fileHandler:
    words = line.split()
    for word in words:
        dic[word] = dic.get(word,0) + 1

lst = list()

for k,v in dic.items():
    newTup = (v,k)
    lst.append(newTup)

lst = sorted(lst, reverse=True)

for v,k in lst[:10]:
    print(k,v)

#list comprehension
c = {'a': 10, 'b'201,'c':20}
print(sorted([v,k for k,v in c.items()]))