# 백준 10951번
#  정수 a, b를 입력받아서 a+b를 출력하는 프로그램 만들기

while True:
    try:
        a, b = map(int, input().split( ))
        print(a+b)
    except:
        break    