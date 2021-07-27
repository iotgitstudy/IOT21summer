n = int(input())

i = 665
count = 0


def real(x):
    #연속 6 체크하는 변수 count
    count = 0
    #인자로 들어온 수 첫 자리부터 탐색
    while x != 0:
        #6이면 +
        if x % 10 == 6:
            count +=1
        #아니면 초기화
        else:
            count = 0
        #3연속일때 중지
        if count >= 3:
            return True
        x = x // 10
    
    return False

#i 증가 연산 루프문
while n != count:
    i += 1
    # 종말의 숫자인지 확인하는 부분
    if real(i):
        count += 1
    
print(i)

