#  Название игры.
name_game = 'Крестики - нолики'

#  Приветитвие игроков.
print('>' * 10, 'Добро пожаловать в игру!!!', '<' * 10) 
print('>' * 14, name_game, '<' * 15)

#  Знакомство с игроками.
first_player = input('Давайте знакомиться! Игрок № 1, введите Ваше имя: \n')
print(f'Приятно познокомиться, {first_player}! Вы играете - крестиками и ходите первым(ой).')
second_player = input('Игрок № 2, введите Ваше имя: \n')
print(f'Приятно познокомиться, {second_player}! Вы играете - ноликами и ходите вторым(ой).')
print('Победа за тем игроком, кто первым соберет линию своих знаков по горизонтали, или по вертикали, или по одной из диогоналей.')
print("Начнём!")

#  Инициализация игрового поля
playing_field = [[' - '] * 3 for _ in range(0, 3)]

#  Вывод начального игрового поля на экран (консоль в нашем случае)
def output_playing_field(p = playing_field):
    print('   0   1   2')
    for i in range(len(playing_field)):
        print(str(i), *playing_field[i])

#  Вывод игрового поля в консоль (каждый раз, при совершении хода игроками)

def subsequent_output_playing_field(p = playing_field):    
    count = 0    #  Заводим счетчик по количеству ходов Игроками, суммарное число которых, не должно превышать количество клеток поля
    while count < 10:
        if count % 2 == 0:
            player = ' X '
        else:
            player = ' O '
        output_playing_field()
        x, y = player_input(playing_field)
        playing_field[x][y] = player
        count += 1
        if count >= 9:
            print(f'Дорогие игроки {first_player} и {second_player} - победила дружба!!! Ничья - так сказать!')
            output_playing_field()
            break
        if victory (playing_field, player):
            if player == ' X ':
                print(f'Поздравляем!!! {first_player}, Вы одержали победу!!!')
                output_playing_field()
            else:
                print(f'Поздравляем!!! {second_player}, Вы одержали победу!!!')
                output_playing_field()
            break
        

#  Условия ввода координат хода Игроками, для корректного хода игры.
def player_input(p = playing_field):
    while True:
        input_data = input('Введите координаты чисел через пробел :\n').split()

        if len(input_data) != 2:
            print('Введите две координаты хода через пробел.')
            continue

        if not(input_data[0].isdigit() and input_data[1].isdigit()):
            print('Введите пожалуйста числа.')
            continue

        x, y = map(int, input_data)              
        if not(x >= 0 and x < 3 and y >= 0 and y < 3):
            print('Вы превысили диапазон игрового поля, необходимо ввести числа согласно нумерации игрового поля.')
            continue

        if p[x][y] == ' X ' or p[x][y] == ' O ':
            print('Занято тут! Уходи скорее!')
            continue
        return x, y

#  Правила (условия) победы
def victory (p, player):
    def winning_lines(x1, x2, x3, player):
        if x1 == player and x2 == player and x3 == player:
            return True
    for i in range(3):
        if winning_lines(p[i][0], p[i][1], p[i][2], player) or \
            winning_lines(p[0][i], p[1][i], p[2][i], player) or \
            winning_lines(p[0][0], p[1][1], p[2][2], player) or \
            winning_lines(p[2][0], p[1][1], p[0][2], player):
                return True
    return False
            
#  "Запускаем нашу ракету в космос" - С Богом!!!)
subsequent_output_playing_field()