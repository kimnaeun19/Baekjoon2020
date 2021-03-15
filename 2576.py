# 2021. 03. 15. 월
# 2576번
# 7개의 자연수가 주어질 때, 
# 이들 중 홀수인 자연수들을 모두 골라 그 합을 구하고, 
# 고른 홀수들 중 최솟값을 찾는 프로그램을 작성하시오.

odd_num = [] # 입력받은 홀수를 저장할 리스트 생성

for i in range(7):
    n = int(input())
    if n % 2 == 1: # 입력받은 값 n이 홀수인지 판단
        odd_num.append(n) # n이 홀수 -> 리스트에 넣어주기

if len(odd_num) == 0:
    print(-1)   # 만약 홀수를 하나도 입력 x -> -1 출력
else:
    print(sum(odd_num))     # 홀수들의 합 출력
    print(min(odd_num))     # 홀수들 중 최솟값 출력   