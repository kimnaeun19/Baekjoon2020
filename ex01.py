'''def solution(s):
   
    if len(s) % 2 == 0:
        return s[(len(s) // 2) - 1 : (len(s) // 2) + 1]
    else:
        return s[len(s)//2]
    
print(solution("abcde"), end = '\n')

def solution_2(n):
    answer = sorted(str(n), reverse = True) # sorted() : 기존에 선언된 리스트 값은 변화시지키지않고 그대로 둔다. 순서대로 정렬한 리스트를 반환. reverse = T : 내림차순
    return int(''.join(answer)) # join : ''안에 있는 기호로 문자열 연결

print(solution_2(118372))   ''' 

# 문자열 다루기 기본 프로그래머스
# 문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요. 
# 예를 들어 s가 a234이면 False를 리턴하고 1234라면 True를 리턴하면 됩니다.

'''def solution(s):
    if len(s) == 4 or len(s) == 6:
        try:
             int(s)
        except ValueError:
            answer = False
        else:
            answer = True         
    else:
        answer = False
    
    return answer

print(solution('a234'))'''

# 제곱근 판별하기 프로그래머스
# 임의의 양의 정수 n에 대해, n이 어떤 양의 정수 x의 제곱인지 아닌지 판단하려 합니다.
# n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, 
# n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.

'''from math import sqrt

def solution(s):
    x = sqrt(s)
    if x % 1 == 0:
        answer = (x + 1) ** 2
    else:
        answer = -1
    
    return answer

print(solution(121))'''

# 두 수 비교하기 백준

a, b = map(int, input().split())
if a > b:
    print('>')
elif a == b:
    print('==')
else:
    print('<')
            