question_1 = input('Вы находитесь в пещере на развилке. Вы можете пойти "налево", "направо" или "прямо". Введите одно из слов в кавычках для выбора.')
if question_1 == 'налево':
    question_2 = input('Вы направились налево. Через некоторое время вы видите две двери. куда вы пойдете?')
    if question_2 == 'налево':
        print('Зря вы пошли налево! Оказалось, что вы потревожили гигантского червя! Бегите!')
    else: print('Пойдя напрво, через длительное время вы увидели свет в конце тонеля. Это оказалась комната полная золота!!!')
elif question_1 == 'направо':
    print('Оказалось, что справа был тупик. Вы заблудились')
elif question_1 == 'прямо':
    print('Вы долго шли прямо. Через время вы увидели перед собой еще 2 двери')
    question_2 = input('Пойти направо или налево?')
    if question_2 == 'направо':
        print('К сожалению, пойдя направо, вы отправились прямиком в логово кровожадного дракона. Вам его не победить')
    else:
        print('Пойдя налево, вы услышали громкий храп из соседнего помещения. Как хорошо, что вы туда не пошли! В конце пути вы видите выход!')
else:
    print('некорректный ответ')