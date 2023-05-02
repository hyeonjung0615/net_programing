# 초기 리스트 생성
my_list = [1, 2, 3]

# 두 번째 요소를 17로 수정
my_list[1] = 17

# 리스트에 4, 5, 6을 추가
my_list.extend([4, 5, 6])

# 첫 번째 요소 제거
my_list.pop(0)

# 리스트를 요소 오름차순 정렬하기
my_list.sort()

# 리스트를 요소 내림차순 정렬하기
my_list.sort(reverse=True)

# 인덱스 3에 25 넣기
my_list.insert(3, 25)

# 결과 출력
print("처리 후 리스트:", my_list)
