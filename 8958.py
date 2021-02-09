# 2021. 02. 15. 월
# 백준 8958번
# ox문제, 해당 문제의 점수는 해당 문제까지 연속하는 O의 갯수
# ox퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램 작성.

n = int(input())

for i in range(n):
    ox = str(input())
    ox_list = list(ox)
    cnt = 0
    score = 0

    for j in ox_list:
        if j == "O":
           cnt += 1
           score += cnt
        else:
           cnt = 0    

    print(score)    