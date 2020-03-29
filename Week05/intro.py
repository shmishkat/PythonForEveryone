#dictionaries
wallet = dict()
wallet['money'] = 500
wallet['candy'] = 5

print(wallet)

wallet['candy'] = wallet['candy']-2
print(wallet)


#many counter with a dictionary
ccc = dict()

counts = dict()
names = ['sarowar','hossain','mishkat','hossain','mishu','mishkat','mishu']

for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1

print(counts)

#get method
x = counts.get('mishkat',0)
print(x)
