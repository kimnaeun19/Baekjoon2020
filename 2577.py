# 2021. 02. 05. 금
# 세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 
# 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.

A = int(input())
B = int(input())
C = int(input())

abc = str(A * B * C)
# str로 바꿔준 이유: for문 이용할 때, 하나씩 뽑아오려고

for i in range(10):
    print(abc.count('{}'.format(i)))    