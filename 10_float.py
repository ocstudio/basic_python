x = 3.3
print(x)
y = 1.1 + 2.2
print(y)
print(x == y)

y_str = format(y, ".2g")
print('str =>', y_str)
print(y_str == str(x))

'''forma matematica que es una forma mas adecuada de poder hacer las operaciones'''
#la forma de hacer una linea divisoria
print('----' * 10)

#para hacer una comparacion de forma matematica

print(y, x)

#establecer una tolerancia
tolerance = 0.00001
print(abs(x - y) < tolerance)

