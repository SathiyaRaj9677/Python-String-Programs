# 1. Method Overloading:

class Calculator:
    def add(self, a, b, c=0):
        return a + b + c

calc = Calculator()

print(calc.add(3, 4))     # 7
print(calc.add(3, 4, 5))  # 12

# 2. Method Overriding:

class RBI:
    def interest_rate(self):
        print("RBI interest rate is 5%")


class SBI(RBI):
    def interest_rate(self):
        print("SBI interest rate is 6.5%")


class HDFC(RBI):
    def interest_rate(self):
        print("HDFC interest rate is 7%")


class ICICI(RBI):
    def interest_rate(self):
        print("ICICI interest rate is 6.75%")


bank = RBI()
sbi = SBI()
hdfc = HDFC()
icici = ICICI()

bank.interest_rate()
sbi.interest_rate()
hdfc.interest_rate()
icici.interest_rate()