
from ctypes import cdll
libc = cdll.LoadLibrary('msvcrt.dll')
libc.printf(b'hello world!\n')

listTmp = [1, 2, 3, 4, 5, 6, 7]
print(f'{len(listTmp)}')

for idx in listTmp:
    libc.printf(b"%d ", idx)

