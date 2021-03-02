print('Hola mundo')
a = 5
b = 8
print(a + b)

if a == 5:
    print('Es 5!!!!')
    print('Otra cosa')
    if b > 5:
        print('Y encima B también se cumple')
    else:
        print('bueno, b, no')
else:
    print('Es otra cosa')

print('Chau')

for i in range(1,20):
    print('A actualmente vale ' + str(a))
    if a<=150:
        print('La condición se cumple')
    else:
        print('La condición no se cumple')
    a = a * i
    
