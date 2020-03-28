fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    line.rstrip()
    if line.startswith("From "):
        newLineList = line.split()
        print(newLineList[1])
        count = count + 1

print("There were", count, "lines in the file with From as the first word")
