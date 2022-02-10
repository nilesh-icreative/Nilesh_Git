string = "hello 111 Hello Aello"
vowel = 'A,E,I,O,U'

string = string.split()

x = [i for i in string if i[0] >= 'A' and i[0] <= 'Z' ]

y = [i for i in x if i[0] not in vowel]

print("String is:",y)