def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# 두 수 입력 받기
num1 = int(input("첫 번째 수를 입력하세요: "))
num2 = int(input("두 번째 수를 입력하세요: "))

# 큰 수와 작은 수 판별하기
if num1 >= num2:
    larger = num1
    smaller = num2
else:
    larger = num2
    smaller = num1

# 최대 공약수 구하기
result = gcd(larger, smaller)

# 최대 공약수 출력
print("두 수의 최대 공약수는 {}입니다.".format(result))
