# with open("task6.txt") as i:
#     with open("tmp", "w") as o:
#         for line in i:
#             o.write("'%s'\n" % line[:-1])

f = open("task6.txt", "r")
# hexNums = [line.strip() for line in f]

hex_val = "0x111"
int_val = int(hex_val, 16)
print(int_val)

chr_val = chr(int_val)
print(chr_val)

#for value in hexNums2:
    #print(value + " --- " + chr(int(value, 16)))

#for decimals in hexes:
    #print(chr(decimals))


