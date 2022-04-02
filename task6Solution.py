secret_number = 148
letters = []
flag = []

with open("task6.txt", 'r') as file:
    for hexValue in file:
        strippedValue = hexValue.replace("\n", "")
        int_val = int(strippedValue, 16)
        letters.append(int_val)

flagRev = letters[::-1]
for v in flagRev:
    chr_val = v - secret_number
    secret_number -= 1
    chr_val2 = chr(chr_val)
    flag.append(chr_val2)

flag = flag[::-1]
print(''.join(map(str, flag)))
