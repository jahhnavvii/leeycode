target = int(input("enter the value: "))
l = [3, 2, 4]
x = []

for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if l[i] + l[j] == target:
            x.append((i, j))

print(x)

