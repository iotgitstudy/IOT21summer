n = input()
x = 'A'
count = 0
for i in n:
    y = i
    z = 26 - abs(ord(x) - ord(y))
    if z > 13:
        z = 26 - z
    count += z
    x = y
print(count)