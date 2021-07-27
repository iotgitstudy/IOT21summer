from dataclasses import dataclass

@dataclass(order=True)
class point():
    x: int
    y: int


    

n = int(input())
box = []
for i in range(n):
    k, v = map(int, input().split())
    box.append(point(k,v))

box.sort()
for i in box:
    print(i.x, i.y)