# 1부터 1000까지의 숫자의 각 자리수의 합을 구하는 함수
def get_digit_sum(num):
    digit_sum = 0
    for s in str(num):
        digit_sum += int(s)
    return digit_sum

# 1부터 1000까지의 숫자의 각 자리수의 합을 모두 구하기
total_digit_sum = 0
for num in range(1, 1001):
    digit_sum = get_digit_sum(num)
    total_digit_sum += digit_sum

# 결과 출력
print("1부터 1000까지의 숫자의 각 자리수의 합:", total_digit_sum)






# 위 코드는 for 루프를 사용하여 1부터 1000까지의 숫자를 반복적으로 생성하고, get_digit_sum() 함수를 호출하여 각 숫자의 각 자리수의 합을 구한 후, 
# total_digit_sum 변수에 누적하여 더하는 방식으로 구현되었습니다. 
# 최종적으로 total_digit_sum에는 1부터 1000까지의 숫자의 각 자리수의 합이 저장되고, 
# 결과는 이를 출력하여 확인할 수 있습니다.