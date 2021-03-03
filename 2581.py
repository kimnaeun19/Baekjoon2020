# 2021. 03. 03. 수
# 2581번
# 자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 
# 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.

m = int(input())
n = int(input())

nums =[]

for i in range(m, n + 1):     # 첫 입력값과 두번째 입력값 사이만 진행
    count = 0                 # 나눠지는 횟수,
    for j in range(1, i+1):             
        if i % j == 0:
            count += 1                  # 나뉘면 count증가
            if count > 2:               # 2보다 크면 소수가 아님
                break
    if count == 2:                      # 소수
        nums.append(i)
if len(nums) != 0:              # 소수리스트에 값이 있다면 밑의 값을 출력
    print(sum(nums))
    print(nums[0])
else:                           # 소수가 하나도 없다면
    print('-1')