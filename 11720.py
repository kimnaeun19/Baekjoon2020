# 2021. 02. 11. 목
# 11720번
# N개의 숫자가 공백없이, 각 숫자를 더해서 합을 출력하는 프로그램

len = int(input())
n = list(input())

sum = 0

for i in n:
    sum += int(i)

print(sum)    