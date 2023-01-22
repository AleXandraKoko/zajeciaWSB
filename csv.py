path = 'rozliczenie.csv'
mode = 'r'
with open (path, mode) as plik_csv:
    content = plik_csv.readlines()

for i in range(len(content)):
    content[i] = content[i].replace('\n','')
    content[i] = content[i].split(';')


#2. Obliczanie sredniej wyplaty
total = 0
for i in range(1, len(content)):
#    total = total + int(content[i][1])
    total += int(content[i][1])
average = total/(len(content)-1)
print('Srednia wynosi',round(average, 2),'zlotych')
print(f'Srednia wynosi {round(average, 2)} zlotych')

#3. Obliczanie liczby kobiet na macierzynskim
total = 0

for i in range(1, len(content)):
    if  content[i][4] == 't': and content[i][3] == 'k':
        total += 1
print(total)


#slowo = 'mama.tata'
#slowo = slowo.replace('a','A',2)
#print(slowo)





# dane = 'mama.tata.pies'
# print(dane)
# dane = dane.split('.')
# print(dane)