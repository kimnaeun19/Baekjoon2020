# 2021. 03. 11
# 2501번
# 두 개의 자연수 N과 K가 주어졌을 때, N의 약수들 중 K번째로 작은 수를 출력하는 프로그램을 작성하시오.

n, k =map(int, input().split())

num = [] # 약수를 저장할 리스트

for i in range(1, n+1):
    if n % i == 0:
        num.append(i)   # n이 i로 나눠지면 num 리스트에 i를 추가

if len(num) >= k:
    print(num[k-1])     # 파이썬에서는 인덱스가 0 ~ n-1까지 이므로 k번째 약수를 출력하려면 k-1
else:
    print(0)            