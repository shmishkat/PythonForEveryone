# Use words.txt as the file name

fname = input("Enter file name: ")
try:
    fh = open(fname)

    for line in fh:
        line = line.rstrip()
        print(line.upper())

except:
    print("File not found")
