def logic() -> None:
    while True:
        print("\n[1] Fahrenheit to Celcius")
        print("[2] Celcius to Fahrenheit")
        choice = int(input("Please select conversion: "))
        
        match choice:
            case 1:
                celcius()
            case 2:
                fahrenheit
            
def celcius() -> None:
    fahrenheit = float(input("\nFahrenheit: "))
    celcius = (fahrenheit - 32) * (5 / 9)
    print(f"Celcius: {celcius}")
    
def fahrenheit() -> None:
    celcius = float(input("\nCelcius: "))
    fahrenheit = (celcius * (9 / 5)) + 32
    print(f"Fahrenheit: {fahrenheit}")
    