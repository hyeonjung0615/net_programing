# 단어 입력 받기
word = input("Your word: ")

# 문자 'a'의 인덱스 찾기
a_index = word.find('a')

# 문자열 분리하기
first_part = word[:a_index+1]
second_part = word[a_index+1:]

# 결과 출력
print(first_part)
print(second_part)
