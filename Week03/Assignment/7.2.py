# Use the file name mbox-short.txt as the file name

fname = input("Enter file name: ")
fh = open(fname)

count = 0
add = 0
avg = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    line = line.rstrip()
    
    val = float(line[19:26])
    add = add + val
    
    #print(val)
    #print(line)

avg = add / count
print("Average spam confidence:",avg)