alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "Z", " ", "\n", ",", "'", ".", "!", "?"]
string = [str(alphabet.index(i)) for i in input().upper()]
code = ''
for i in string:
    code += i
print(code)
print(len(alphabet))