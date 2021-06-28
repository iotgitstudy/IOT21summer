#거스름 돈

##조건: 
#500, 100, 50, 10, 5, 1 무한
# 언제나 거스름 돈 개수가 가장 적게 반환
#제출 금액은 언제나 1000엔 지폐

#input : 지불할 금액

#output : 거스름 돈 개수

x = int(input())
x = 1000 - x
box = []

while x >= 500:
    x -= 500
    box.append(500)
while x >= 100:
    x -=100
    box.append(100)
while x >= 50:
    x -=50
    box.append(50)
while x >= 10:
    x -=10
    box.append(10)
while x >= 5:
    x -=5
    box.append(5)
while x >= 1:
    x -=1
    box.append(1)
print(len(box))