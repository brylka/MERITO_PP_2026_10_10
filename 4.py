# a = 10
# print(a)
# #a = a + 5
# # a = a ** 3
# a **= 3
# print(a)

# a = 5
# b = 5
# print(a > b)
# Operatory porównania:
# == równe
# != różne
# > większe
# >= większe lub równe
# < mniejsze
# <= mniejsze, lub równe

# a = 4
# b = 5
# c = 6
#
# print(a > b and c > a)

# text = "Python"
# print("e" not in text)

# #       01234567890123456
# text = "Python-to-fajny język!"
# print(text)
# print(text[7:15]) # od - do-1: to-fajny
# print(text[:6])   # od początku - do-1: Python
# print(text[3:11:2]) # od - do-1 co: hnt-
# print(text[10]) # dokładny znak na pozycji
# print(text[::-1])
#       01234567
text = "  Bartosz bryniarski  "
print(text.upper())
print(text.lower())
print(text.strip())
print(text.title())
print(text.replace("Bartosz", "Paweł"))
print(text.count("r"))
print(text.find(" "))
print(text.strip().startswith("Bar"))
print(text.endswith("ski  "))