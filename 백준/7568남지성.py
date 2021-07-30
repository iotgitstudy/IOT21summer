n = int(input())
box = []
for i in range(n):
    x,y = map(int, input().split())
    box.append([x,y])
answer = []
for _ in range(n):
    j = box.pop(0)
    count = 1
    for i in box:
        if j[0] < i[0] and j[1] < i[1]:
            count += 1
    box.append(j)
    answer.append(count)

for i in answer:
    print(i,end=" ")