# modulelar program
import ArithmeticModule

print("inside client :",__name__)

Result = ArithmeticModule.Add(10,11)
print("Additon is :",Result)

Result = ArithmeticModule.Sub(10,11)
print("Subtraction is :",Result)

Result = ArithmeticModule.Mult(10,11)
print("Multiplicationn is :",Result)

Result = ArithmeticModule.Div(25,3)
print("division is :",Result)