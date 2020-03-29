#simplified counting using the get method.

dic = dict()
names = ['sarowar','hossain','mishkat','hossain','mishu','mishkat','mishu']

for name in names:
    dic[name] = dic.get(name,0) + 1
print(dic)