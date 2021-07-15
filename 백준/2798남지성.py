# 블랙잭

# 카지노에서 제일 인기 있는 게임 블랙잭의 규칙은 상당히 쉽다. 카드의 합이 21을 넘지 않는 한도 내에서, 카드의 합을 최대한 크게 만드는 게임이다. 블랙잭은 카지노마다 다양한 규정이 있다.

# 한국 최고의 블랙잭 고수 김정인은 새로운 블랙잭 규칙을 만들어 상근, 창영이와 게임하려고 한다.

# 김정인 버전의 블랙잭에서 각 카드에는 양의 정수가 쓰여 있다. 그 다음, 딜러는 N장의 카드를 모두 숫자가 보이도록 바닥에 놓는다. 그런 후에 딜러는 숫자 M을 크게 외친다.

# 이제 플레이어는 제한된 시간 안에 N장의 카드 중에서 3장의 카드를 골라야 한다. 블랙잭 변형 게임이기 때문에, 플레이어가 고른 카드의 합은 M을 넘지 않으면서 M과 최대한 가깝게 만들어야 한다.

# N장의 카드에 써져 있는 숫자가 주어졌을 때, M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력하시오.

# 입력
# 첫째 줄에 카드의 개수 N(3 ≤ N ≤ 100)과 M(10 ≤ M ≤ 300,000)이 주어진다. 둘째 줄에는 카드에 쓰여 있는 수가 주어지며, 이 값은 100,000을 넘지 않는 양의 정수이다.

# 합이 M을 넘지 않는 카드 3장을 찾을 수 있는 경우만 입력으로 주어진다.

# 출력
# 첫째 줄에 M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 출력한다.

#list 합 구하는 함수
def list_sum(box):
    count = 0
    for i in box:
        count += i
    return count
#list 원소 3개인지 확인하는 함수
def not3(box):
    if len(box) != 3:
        return True
    else:
        return False


n, m = map(int, input().split())
box = list(map(int, input().split()))
#오름차순
box.sort(reverse=True)
#얕은 복사
box1 = box[:]
#합 구하는 빈 통
sum = []

#정답 list
answer = []


#반복문 시작
while True:

    #box1에서 원소를 제거하며 합 탐색
    for i in box1:
        
        #3보다 적은 수 일때 원소 투입
        if not3(sum):
            sum.append(i)

            #3이 아닐시 계산 X 그냥 넘어감
            if not3(sum):
                continue
        
        #조건에 부합할때 출력
        if list_sum(sum) <= m:
            answer.append(list_sum(sum))
            
        #초과시 마지막 제일 작은 원소 제거
        else:
            sum.pop()
    
    #box1탐색 중 원소의 개수가 2보다 클 경우만 
    if len(box1) >= 2:
        #2번째로 큰 값 제거 후 탐색
        del box1[1]
        sum = []
    #box1 탐색중 원소가 모자라는 경우 - 탐색이 끝난 것이니 제일 큰 원소 삭제 후 재 탐색
    else:
        if len(box) <= 2:
            break
        del box[0]
        box1 = box[:]
        sum=[]

#정답 list에서 근접 값 출력
answer.sort(reverse=True)
for i in answer:
    if i <= m:
        print(i)
        break
