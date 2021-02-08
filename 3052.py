# 2021. 02. 08. 월
# 3052번
# 수 10개를 입력 받아 42로 나눈 후 서로 다른 나머지의 갯수

num = []

for i in range(10):
    n = int(input())
    r = n % 42
    num.append(n)

num2 = set(num)
# set 함수 : 중복값을 제외시키는 함수

print(len(num2))    

