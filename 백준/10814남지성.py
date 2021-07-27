from dataclasses import dataclass

@dataclass(order=True)
class box():
    age:int
    name : str

L = []
lock = True
n = int(input())

for i in range(n):
    a, name = map(str, input().split())
    age = int(a)
    for _ in L:
        if _.age == age:
            _.name = _.name+" "+name
            lock = False
            break
        lock = True
    if lock:
        L.append(box(age, name))
        lock = True
L.sort()

for i in L:
    name_box = i.name.split()
    for j in name_box:
        print(i.age, j)