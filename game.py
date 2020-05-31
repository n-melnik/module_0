import numpy as np
number = np.random.randint(1,101)    # загадали число
print ("Загадано число от 1 до 100")


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(100))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


def game_core_v2(number):
    '''Сначала устанавливаем любое random число, сравниваем его с загаданным и, 
       в зависимости от того больше оно или меньше, устанавливаем его как больший 
       или меньший предел в функцию randint.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    min_limit = 1
    max_limit = 101
    predict = np.random.randint(min_limit,max_limit)
    while number != predict:
        count+=1
        if number > predict:
            min_limit = predict
            predict = np.random.randint(min_limit,max_limit)
        elif number < predict:
            max_limit = predict
            predict = np.random.randint(min_limit,max_limit)
    return(count) # выход из цикла, если угадали


score_game(game_core_v2)