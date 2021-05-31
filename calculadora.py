class Calculadora:
    def __init__(self, num1, num2) :
        self.a = num1
        self.b = num2
    def soma(self):
        return self.a + self.b

    def subtracao(self):
        return self.a - self.b

    def multiplacacao(self):
        return self.a * self.b

    def divisao(self):
        return self.a / self.b

contador = Calculadora(10, 5)

print(contador.soma())
print(contador.subtracao())
print(contador.multiplacacao())
print(contador.divisao())