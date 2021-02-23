# 2021. 02. 23. 화
# 2675번
# 문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오.

n = int(input())

for i in range(n): # n개의 문자열을 입력하기 위한 for문
    num, s = input().split() # num번씩 s문자열의 각 문자를 반복
    
    for j in s: # s문자열의 각각의 문자를 반복하기 위한 fon문
        print(j * int(num), end ="")
        
    print()