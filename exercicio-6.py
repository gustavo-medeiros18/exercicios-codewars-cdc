def century(year):
    first_digits = year // 100
    last_digits = year % 100

    century = first_digits

    if last_digits > 0:
        century += 1

    return century

print(century(1705))
print(century(1900))
print(century(1601))
print(century(2000))
print(century(2742))
print(century(89))
print(century(356))
print(century(20500))
print(century(20512))
print(century(1))