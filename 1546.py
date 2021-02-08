# 2021. 02. 08. 월
# 1546번

# 새로운 평균구하기 : 과목점수/최대점수 * 100
# 과목수 n개 입력 -> 과목 점수 입력 -> 평균출력

sub = int(input())
sub_score = list(map(float, input().split()))
sub_max = max(sub_score)
sub_sum = 0

for j in range(sub):
    sub_score[j] = (sub_score[j] / sub_max) * 100
    sub_sum += sub_score[j]

print(sub_sum/sub)   
