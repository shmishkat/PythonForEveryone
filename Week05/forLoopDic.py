#for loop in dictionaries.

countsofNames = {'sarowar': 1, 'hossain': 2, 'mishkat': 2, 'mishu': 2}

for key in countsofNames:
    print(key,countsofNames[key])

#converting dictionary to list
nameList = list(countsofNames)

print(nameList)
print(countsofNames.keys())
print(countsofNames.values())
print(countsofNames.items())

#Cool thing!!
#Muiltiple iteration variables!!

for key,value in countsofNames.items():
    print(key,value)