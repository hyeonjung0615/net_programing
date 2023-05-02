# class MyComplex:
#     def __init__(self, real_1, imaginary_1, real_2, imaginary_2):
#         self.real_1 = real_1
#         self.imaginary_1 = imaginary_1
#         self.real_2 = real_2
#         self.imaginary_2 = imaginary_2
#         # 인스턴스 변수 초기화

#     def mul(slef):
#         # (a+bi) * (c+di)
#         real = (slef.real_1 * slef.real_2)  - ( slef.imaginary_1 * slef.imaginary_2)
#         print(real)
#         imaginary = (slef.real_1 * slef.imaginary_2) + (slef.real_2 * slef.imaginary_1 )
#         print(imaginary)
#         result = f'{real} {imaginary}i'
#         return result


# r = MyComplex(3, -4, -5 , 2)
# print(r)

# # (a+bi) * (c+di)
# # real =  (a * c) - (b * d) 
# #         (a * c) - (b * d) + (a*d + c*b)*i



# class MyComplex:
#     def __init__(self, real, imaginary):
#         self.real = real
#         self.imaginary = imaginary

# def Calculator(complex1, complex2):
#     a = complex1.real
#     b = complex1.imaginary
#     c = complex2.real
#     d = complex2.imaginary
#     real_cal = a*c - b*d
#     imag_cal = a*d + b*c
#     result = f'{real_cal} + {imag_cal}i' 
#     return  result

# complex_1 = MyComplex(3, -4)
# complex_2 = MyComplex(-5,2)
# print(Calculator(complex_1, complex_2))
# print('\n\n')



class MyComplex:
    def __init__(self,i,j,k,z):
        self.real_1 = i
        self.imaginary_1 = j
        self.real_2 = k
        self.imaginary_2 = z
        
    def multiply(self):
        self.result_1 = (self.real_1*self.real_2) -1*(self.imaginary_1*self.imaginary_2)
        self.result_2 = (self.real_1*self.imaginary_2 + self.imaginary_1*self.real_2)
        if self.result_2 >= 0 :
            self.result_2 = '+'+str(self.result_2)
        self.sum = str(self.result_1)+str(self.result_2)+'i'
        return self.sum
    
p1 = MyComplex(3,-4,-5,2)
print(p1.multiply())

'''
위 코드는 MyComplex라는 클래스를 정의하고, 두 개의 복소수를 곱하는 multiply 메소드를 구현한 예시 코드입니다.

MyComplex 클래스는 __init__ 메소드를 통해 두 개의 복소수를 초기화합니다. 
i와 j는 첫 번째 복소수의 실수부와 허수부를 나타내고, k와 z는 두 번째 복소수의 실수부와 허수부를 나타냅니다. 
이 초기화된 값들은 클래스의 인스턴스 변수인 self.real_1, self.imaginary_1, self.real_2, self.imaginary_2에 저장됩니다.

multiply 메소드는 두 개의 복소수를 곱한 결과를 반환합니다. 
두 복소수의 곱은 (self.real_1*self.real_2) -1*(self.imaginary_1*self.imaginary_2)로 계산됩니다. 
이 때, -1*(self.imaginary_1*self.imaginary_2)는 두 번째 복소수의 허수부에 음수를 곱해주는 부분입니다. 곱한 결과를 self.result_1에 저장합니다.

또한, 두 복소수의 곱의 허수부는 (self.real_1*self.imaginary_2 + self.imaginary_1*self.real_2)로 계산됩니다. 
이 결과를 self.result_2에 저장하고, 만약 self.result_2가 양수인 경우에는 앞에 '+'를 붙여줍니다.

마지막으로, self.result_1과 self.result_2를 문자열로 변환하여 'i'와 함께 이어붙인 후, self.sum에 저장합니다. 
이 값을 return하여 함수의 결과로 반환합니다.

위 코드에서는 MyComplex 클래스의 인스턴스 p1을 생성하고, multiply() 메소드를 호출하여 두 개의 복소수를 곱한 결과를 출력합니다. 
p1의 초기값으로는 3, -4, -5, 2가 사용되었습니다.'''