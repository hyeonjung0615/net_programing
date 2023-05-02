class MyComplex:
    def __init__(self, r1, i1, r2, i2):
        # 인스턴스 변수 초기화
        self.real_1 = r1
        self.imaginary_1 = i1
        self.real_2 = r2
        self.imaginary_2 = i2

    def add(self):
        self.rrr = self.real_1 + self.real_2
        self.iii = self.imaginary_1 + self.imaginary_2
        self.result = str(self.rrr)+'+'+ str(self.iii)+'i'
        return self.result
    
    def mul(self):
        self.rrr = self.real_1 - self.real_2
        self.iii = self.imaginary_1 - self.imaginary_2
        self.result = str(self.rrr)+ str(self.iii)+'i'
        return self.result
    
add = MyComplex(2,-3,-5,4)       
print(add.add())
print(add.mul())