path = 'C:\\Users\\vdi-student\\Desktop\\zajeciaWSB\\rozliczenie.csv'
mode = 'r'
with open (path, mode) as plik_csv:
    content = plik_csv.readline()

print(type(content))
print(len(content))
print(content)
print(content[4])

for i in range(len(content)):
    content[i] = content[i].split(':')
print(content)

# dane = 'mama.tata.pies'
# print(dane)
# dane = dane.split('.')
# print(dane)