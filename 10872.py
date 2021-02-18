# 2021. 02. 18. 목
# 10872번
# 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

n = int(input())

# 재귀함수이용

def fac(num):
    if num < 1:
        return 1

    return num * fac(num-1)

print(fac(n))        
