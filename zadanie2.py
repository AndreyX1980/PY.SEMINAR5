# игра с конфетами

from random import *
import os


privetstvie = ('Привет!\n'
                'Это игра "2021 конфета"\n'
                'Сначала правила:\n'
                'Перед вами 2021 конфета, вы берете их по очереди,\n'
                'за один раз можно взять не больше 28 конфет.\n'
                'Выигрывает тот, кто последним ходом заберет все конфеты.\n')
print(privetstvie)

message = ['твоя очередь', 'бери больше', 'твой ход', 'твой выбор']


def player_vs_player():
    vsego_konfet = 2021
    max_take = 28
    count = 0
    player_1 = input('\nИмя первого игрока?: ')
    player_2 = input('\nИмя второго игрока?: ')

    print(f'\nИтак, {player_1} и  {player_2}  начнем !\n')
    print('\nЖеребьевка!\n')

    x = randint(1, 2)
    if x == 1:
        lucky = player_1
        loser = player_2
    else:
        lucky = player_2
        loser = player_1
    print(f'Поздравляю {lucky} ты ходишь первым !')

    while vsego_konfet > 0:
        if count == 0:
            step = int(input(f'\n{choice(message)} {lucky} = '))
            if step > vsego_konfet or step > max_take:
                step = int(input(
                    f'\nПеребор, можно взять только {max_take} конфет {lucky}, попробуй еще раз: '))
            vsego_konfet = vsego_konfet - step
        if vsego_konfet > 0:
            print(f'\nосталось {vsego_konfet}')
            count = 1
        else:
            print('Конфеты закончились!')

        if count == 1:
            step = int(input(f'\n{choice(message)}, {loser} '))
            if step > vsego_konfet or step > max_take:
                step = int(input(
                    f'\nНе жадничай можно взять только {max_take} конфет {loser}, попробуй еще раз: '))
            vsego_konfet = vsego_konfet - step
        if vsego_konfet > 0:
            print(f'\nна кону еще {vsego_konfet}')
            count = 0
        else:
            print('Всё, конфеты закончились!')

    if count == 1:
        print(f'{loser} ПОБЕДИЛ')
    if count == 0:
        print(f'{lucky} ПОБЕДИЛ')


player_vs_player()


def player_vs_bot():
    vsego_konfet = 2021
    max_take = 28
    player_1 = input('\nКак тебя зовут?: ')
    player_2 = 'Компьютер'
    players = [player_1, player_2]
    print(f'\nНу чтож {player_1} и  {player_2} да начнется игра !\n')
    print('\nДля начала опеределим кто первый начнет игру.\n')

    lucky = randint(-1, 0)

    print(f'Поздравляю {players[lucky+1]} ты ходишь первым !')

    while vsego_konfet > 0:
        lucky += 1

        if players[lucky % 2] == 'Компьютер':
            print(
                f'\nХодит {players[lucky%2]} \nНа кону {vsego_konfet}. \n{choice(message)}: ')

            if vsego_konfet < 29:
                step = vsego_konfet
            else:
                delenie = vsego_konfet//28
                step = vsego_konfet - ((delenie*max_take)+1)
                if step == -1:
                    step = max_take -1
                if step == 0:
                    step = max_take
            while step > 28 or step < 1:
                step = randint(1,28)
            print(step)
        else:
            step = int(input(f'\nНу чтож ходи,  {players[lucky%2]} \nНа кону {vsego_konfet} {choice(message)}:  '))
            while step > max_take or step > vsego_konfet:
                step = int(input(f'\nЗа один ход можно взять {max_take} конфет, попробуй еще раз: '))
        vsego_konfet = vsego_konfet - step

    print(f'На кону осталось {vsego_konfet} \nПобедил {players[lucky%2]}')

player_vs_bot()