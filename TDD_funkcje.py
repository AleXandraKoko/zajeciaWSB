def przywitanie(imie, nazwisko, wiek):
    print('Siema', imie)
    if wiek >= 18:
        print('Szanowny ', nazwisko)

dict = {'imie' : 'Kamil', 'nazwisko' : 'Kowalski'}
x = input('Podja imie, nazwisko i wiek - oddziel spacją ').split()
przywitanie(x[0], x[1], int(x[2]))
przywitanie(dict['imie'], dict['nazwisko'], 22)



# pin = '1234'
# while True:
#    x = input('Wprowadz pin ')
#    if x == pin:
#        przywitanie()
#        break
# print('Kolejna instrukcja')




# x = 0
# y= 0
# while x != 'Kamil' or y == 5:
#    x = input('podaj imie')
#    y += 1
