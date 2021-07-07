# 제로

# 조건: k개의 수를 차례로 받는 중 0이 등장하면 최근 수 1개를 지운다.
# 최종 합을 출력한다. 0이 등장할 때 삭제할 수가 무조건 있다고 가정한다.

#input : k, k개의 수

#output : 남아있는 숫자 합

k = int(input())
box = []
for i in range(k):
    x = int(input())
    if x:
        box.append(x)
    else:
        box.pop()
answer = 0
for i in box:
    answer +=i
print(answer)