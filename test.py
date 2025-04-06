from t1 import convertir_a_decimal

print(convertir_a_decimal(1010, 'BIN'))
print(convertir_a_decimal(1011, 'BIN'))
print(convertir_a_decimal(101010, 'BIN'))
print(convertir_a_decimal(0, 'BIN'))
print(convertir_a_decimal(1, 'BIN'))
print(convertir_a_decimal('11111111', 'BIN'))

print(convertir_a_decimal(10, 'OCT')) # 8
print(convertir_a_decimal(17, 'OCT')) # 15
print(convertir_a_decimal(123, 'OCT')) # 83
print(convertir_a_decimal('777', 'OCT')) # 511
print(convertir_a_decimal(0, 'OCT')) # 0
print(convertir_a_decimal(77, 'OCT')) # 63

print(convertir_a_decimal('A', 'HEX')) # 10
print(convertir_a_decimal('1F', 'HEX')) # 31
print(convertir_a_decimal('A1', 'HEX')) # 161
print(convertir_a_decimal('ABC', 'HEX')) # 2748
print(convertir_a_decimal('FF', 'HEX')) # 255
print(convertir_a_decimal('0', 'HEX')) # 0
print(convertir_a_decimal('123456', 'HEX')) # 1193046
