a = 123
b = -123
print(a, b)

fa = 12.345
fb = -3.14
fexpA = 4.24E3
fexpB = 4.24E-3

print(f'float number example: {fa}, {fb}, {fexpA}, {fexpB}')

# 8진수 practice
octA = 0o1777
print(octA)

# 16진수 (HexaDecimal)
hexA = 0x1FF24
print(f'{hexA:d}, {hexA:0x}, {hexA:f},\n{hexA:1.4f}')

# floating Point Example
num = 0.0
for idx in range(0, 100):
    num += 0.1
print(num)
print(f'{num:.18f}')

tmp = 0.1 + 100
print(tmp)
print(f'{tmp:.18f}')
