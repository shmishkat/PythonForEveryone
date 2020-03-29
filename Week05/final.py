name = input('Enter file name: ')
handle = open(name)

counts = dict()

for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1


bigword = None
bigcount = None

for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword,bigcount)

# stuff = dict()
# print(stuff['candy'])