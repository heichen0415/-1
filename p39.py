class Rational10:
    def __init__(self,num,den=1):
        self.num=num
        self.den=den

    def plus(self,another):
        den=self.den*another.den
        num=(self.num*another.den+self.den*another.num)
        return Rational10(num,den)

    def print(self):
        print(str(self.num)+'/'+str(self.den))

r1=Rational10(3,5)
r2=r1.plus(Rational10(7,15))
r2.print()
