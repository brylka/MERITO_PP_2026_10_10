while True:
    text = input("Podaj słowo: ").lower().replace(" ", "")
    if text == text[::-1]:
        print("Palindrom")
    else:
        print("NIE palnidrom")