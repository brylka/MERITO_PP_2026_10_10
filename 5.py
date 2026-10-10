a = float(input("Podaj liczbę a: "))
b = float(input("Podaj liczbę b: "))

if a > b:
    text = f"Większa jest liczba a={a}"
elif b > a:
    text = f"Większa jest liczba b={b}"
elif a == b:
    text = f"Obie liczby są równe i wynoszą {a}"
else:
    text = "Coś nie tak!"

print(text)


