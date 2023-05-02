class MyComplex:
    def __init__(self, real_1, imaginary_1, real_2, imaginary_2):
        self.real_1 = real_1
        self.imaginary_1 = imaginary_1
        self.real_2 = real_2
        self.imaginary_2 = imaginary_2

    def multiply(self):
        real_result = self.real_1 * self.real_2 - self.imaginary_1 * self.imaginary_2
        imaginary_result = self.real_1 * self.imaginary_2 + self.imaginary_1 * self.real_2
        return f"{real_result} + {imaginary_result}i"


# 복소수 a와 b를 객체로 생성
a = MyComplex(3, -4, -5, 2)
b = MyComplex(-5, 2, 3, -4)

# a와 b를 곱셈 연산하여 결과 출력
result = a.multiply()
print(f"a * b = {result}")
