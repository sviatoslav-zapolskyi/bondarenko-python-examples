
def compare_numbers(a, b):
    if a > b:
        return f"{a} більше {b}"
    elif a < b:
        return f"{a} менше {b}"
    else:
        return f"{a} дорівнює {b}"




l_name, f_name = input("Введіть прізвище та ім'я: ").split()

A = len(f_name)
print("A =", A)

B = len(l_name)
print("B =", B)

C = A + B
print(f"C = {A} + {B} = {C}")

print(f"Умова C > 10 {'істинна' if C > 10 else 'хибна'}, тому що {compare_numbers(C, 10)}")

if C > 10:

    print(f"C = C + 1 = {C + 1}")
    C = C + 1
else:
    print(f"C = C + A = {C + A}")
    C = C + A

i = 0
D = 0

print(f"i = {i}; D = {D}")

while True:
    print(f"D = D + C = {D} + {C} = {D + C}")
    D = D + C

    print(f"Умова i <= 3 {'істинна' if i <= 3 else 'хибна'}, тому що {compare_numbers(i, 3)}")

    if i > 3:
        break

    print(f"i = i + 1 = {i} + 1 = {i + 1}")
    i = i + 1


print(f"Кінцеве значення D = {D}")