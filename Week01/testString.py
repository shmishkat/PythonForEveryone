camera = "photograph"

print(camera[1])

x = len(camera)
print(x)

index = 0
while index < len(camera):
    x = camera[index]
    print(index,x)
    index = index + 1
print(" ")

index = 0
count = 0
for letter in camera:
    print(index, letter)
    if letter == "h":
        count = count + 1
    index = index + 1
print(" ")
print(count)

print(camera[0:5])
print(camera[5:])
print(camera[:])