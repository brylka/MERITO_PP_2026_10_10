a = float(input("Podaj liczbę a: "))
b = float(input("Podaj liczbę b: "))

if a > b:
    print(f"Większa jest liczba a={a}")
elif b > a:
    print(f"Większa jest liczba b={b}")
elif a == b:
    print(f"Obie liczby są równe i wynoszą {a}")
else:
    print("Coś nie tak!")
print("Koniec")


