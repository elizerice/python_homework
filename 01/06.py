answer_1 = input('Любите ли вы котиков?')
answer_2 = input('«Умеете ли вы программировать?')
if answer_1 == 'да' and answer_2 == 'да':
    print('У вас наверняка есть кот и ноутбук/пк!!!')
elif answer_1 == 'да' and answer_2 == 'нет':
    print('У вас лапки!')
elif answer_1 == 'нет' and answer_2 == 'да':
    print('Возможно, кошки вам чем-то не угодили..')
elif answer_1 == 'нет' and answer_2 == 'нет':
    print('Вы не программист и у вас нет кота')
else:
    print('Ошибка!')
