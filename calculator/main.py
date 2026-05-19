import calculator
import converter

if __name__ != '__main__':
    exit
    
print("Welcome to multi-purpose calculator!")
print("[1] Calculator")
print("[2] Converter")
print("[3] Exit")
choice = int(input("Please choose your action: "))

match choice:
    case 1:
        calc = calculator.logic()
        calc.logic()
    case 2:
        conv = converter.logic()
        conv.logic()