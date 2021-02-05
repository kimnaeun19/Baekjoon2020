# 2021. 02. 05. 금
# 최대, 최소 출력
# n개의 정수가 주어졌을 때, max, min 출력

n = int(input())
num = list(map(int, input().split(" ")))

num_max = -1000000
num_min = 1000000

for i in range(n):
    if num[i] > num_max:
        num_max = num[i]
for j in range(n):
    if num[j] < num_min:
        num_min = num[j]

print(num_min, num_max)              