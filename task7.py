from secret import *

secret_number_1 = 5
secret_number_2 = 10
flag = "IKT449{}"

enc = []
# ord() returns the unicode code from a given chr
# in this case the unicode code for each letter i
# + secret_number_1 is added together and
# appended to enc list
for i in flag:
    enc.append((ord(i) + secret_number_1))

# the list is then added to cne in reverse order
cne = enc[::-1]

cne2 = []
# range(start, stop, step)
# starts @ 0, stops @ the length
# the list (cne) with an increase
# of 2 each time
# each even number gets appended to cne2 list after each iteration
for e in range(0, len(cne), 2):
    cne2.append(cne[e])

# range(start, stop, step)
# starts @ 1, stops @ the length
# the list (cne) with an increase
# of 2 each time
# each odd number gets appended to cne2 list after each iteration
for e in range(1, len(cne), 2):
    cne2.append(cne[e])

# each number in cne2
# is subtracted from secret_number_2
for r in cne2:
    print(r - secret_number_2)


