# 2021. 03. 05. 금
# 4153번
# 과거 이집트인들은 각 변들의 길이가 3, 4, 5인 삼각형이 직각 삼각형인것을 알아냈다. 
# 주어진 세변의 길이로 삼각형이 직각인지 아닌지 구분하시오.

while 1:
    num = list(map(int, input().split( ))) # 리스트에 입력받은 변들의 길이를 저장
    num_max = max(num) # max변수에 입력값들 중 가장 큰 값을 저장
    
    if num_max == 0: # 리스트 num의 값들이 0이 되면 while문 종료
        break

    num.remove(num_max)

    if num[0] ** 2 + num[1] ** 2 == num_max ** 2: # 피타고라스 정리가 만족하는가
        print('right')
    else:
        print('wrong')    