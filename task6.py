from secret import *

# secret_number is the value used to rotate the ascii value of
# so if secret number is 9, the ascii value of I = 82, 9 up from 73
# since we know that IKT449{} has to be there, we can convert the output
# in task6.txt to it's corresponding int value and from there
# subtract the int value given with the ascii value of I which
# will give us the secret number we're looking for.
# hex value: 0xb4 = 180, ascii value for I = 73, 180 - 73 = 107
# secret_number used to encrypt the output = 107
secret_number = 107
flag = "IKT449{}"

enc = []
for i in flag:
    enc.append(hex(ord(i)+secret_number))
    secret_number += 1

for e in enc:
    print(e)