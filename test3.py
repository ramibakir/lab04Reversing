secret_numbers = 14

value = [111,
88,
37,
87,
81,
90,
81,
97,
81,
96,
81,
90,
91,
91,
81,
90,
81,
102,
87,
88,
34,
101,
43,
38,
61,
102,
37,
37,
94,
87,
102,
97,
102,
86,
83,
102,
89,
91,
100,
87,
102,
34,
81,
94,
88,
90,
109,
38,
70,
59]

with open("task7.txt", 'r') as f:
    value = [line.strip() for line in f]

for v in value:
    print(chr(v + 14))

    # secret_number is the value used to rotate the ascii value of
    # so if secret number is 9, the ascii value of I = 82, 9 up from 73
    secret_number = 107
    flag = "IKT449{}"



