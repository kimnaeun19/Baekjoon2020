# 2021. 03. 09. 화
# 1934번
# 두 자연수 A와 B가 주어졌을 때, A와 B의 최소공배수를 구하는 프로그램을 작성하시오.

num = int(input())

# gcd(최대공약수) 구하는 함수 구현
def gcd(n, m):
    if m == 0:
        return n        # n이 0이면 최대공약수 m
    else:
        return gcd(m, n % m)    

for i in range(num):
    a, b = map(int, input().split( ))   
    k = gcd(a, b)
    print(int(k * (a/k)*(b/k)))     