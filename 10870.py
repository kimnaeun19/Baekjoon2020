# 2021. 02. 22. 월
# 10870번
# 피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 
# 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.
# n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.

n = int(input())

# 재귀함수 이용
def fibo(num):
    if num <= 1:
        return num
    return fibo(num-2) + fibo(num-1)  

print(fibo(n))