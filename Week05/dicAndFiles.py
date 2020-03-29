#dictionaries and files.

text = input('Enter your text:' )

words = text.split()
dic = dict()
for word in words:
    dic[word] = dic.get(word,0) + 1

print(dic)