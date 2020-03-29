name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

dic = dict()
for line in handle:
    if line.startswith("From "):
        words = line.split()

        time = words[5]
        hourSplit = time.split(":")
        hour = hourSplit[0]
        dic[hour] = dic.get(hour,0) + 1


lst = dic.items()
sortedlst = sorted(lst)

for v,k in sortedlst:
    print(v,k)
