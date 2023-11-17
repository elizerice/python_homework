num =  int(input())
country_change = True
war = str()
peace = str()
for i in range(num):
    if country_change == True:
        war = 'Евразия'
        peace = 'Остазия'
    else:
        war = 'Остазия'
        peace = 'Евразия'
    event = str(input())
    if event == 'С кем война?':
        print(war)
    if event == 'С кем мир?':
        print(peace)
    if event == 'Меняем':
        if country_change == True:
            country_change = False
        else:
            country_change = True
