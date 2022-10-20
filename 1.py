from math import remainder


def decimal_to_new_base(n, base):
    binary = ''
    while(n >= base):
        remainder = n % base
        binary += str(remainder)
        n = n // base
    return str(n) + binary[::-1]

n = int(input('Введите целое число: '))
base = int(input('Введите основание системы счисления: '))
if (base < 2):
    print('Основание системы счисления должно быть не меньше 2')
else:
    print(n, '->', decimal_to_new_base(n, base))

