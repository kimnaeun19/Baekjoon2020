# 2021. 02. 24. 수
# 1157번
# 알파벳 대소문자로 된 단어가 주어지면, 
# 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 
# 단, 대문자와 소문자를 구분하지 않는다.

s = input().upper() # 입력받은 문자열 -> 대문자화
unique_s = list(set(s)) # 입력받은 s에서 중복값 제거

cnt_s = [] # s에서 같은 알파벳 갯수 카운트해서 저장

for i in unique_s :
    cnt = s.count(i)
    cnt_s.append(cnt)  # count 숫자를 리스트에 append

if cnt_s.count(max(cnt_s)) > 1 :  # count 숫자 최대값이 중복되면
    print('?')
else :
    max_index = cnt_s.index(max(cnt_s))  # count 숫자 최대값 인덱스(위치)
    print(unique_s[max_index])

# if문
# cnt_s에서 최댓값의 갯수를 찾아서 그 값이 중복되면(1보다 크면) ? 를 출력 
# else문
# if문을 만족하지 않으면 else문으로 들어와서 최댓값을 찾아 출력   