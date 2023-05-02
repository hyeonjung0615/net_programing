days = {'January':31, 'February':28, 'March':31, 'April':30, 
        'May':31, 'June':30, 'July':31, 'August':31,
        'September':30, 'October':31, 'November':30, 
        'December':31}

# 사용자로부터 월을 입력 받음
user_input = input("월을 입력하세요: ")

# 해당 월에 일수를 출력
if user_input in days:
    print("{} 월의 일수는 {}일 입니다.".format(user_input, days[user_input]))
else:
    print("해당하는 월이 없습니다.")

# 알파벳 순서로 모든 월을 출력
sorted_months = sorted(days.keys())
print("알파벳 순서로 월 출력:", sorted_months)

# 일수가 31인 월을 모두 출력
months_with_31_days = [month for month, days in days.items() if days == 31]
print("일수가 31인 월 출력:", months_with_31_days)

# 월의 일수를 기준으로 오름차순으로 (key-value) 쌍을 출력
sorted_days = sorted(days.items(), key=lambda x: x[1])
print("월의 일수를 기준으로 오름차순으로 (key-value) 쌍 출력:")
for month, days in sorted_days:
    print("{}: {}".format(month, days))

# 사용자가 월을 3자리만 입력하면 월의 일수를 출력
user_input = input("월을 3자리만 입력하세요: ")
for month, days in days.items():
    if month[:3].lower() == user_input.lower():
        print("{} 월의 일수는 {}일 입니다.".format(month, days))
