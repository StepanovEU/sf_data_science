"""Игра угадай число - Домашнее задание
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def game_core_v3(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    max_number = 100
    min_number = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)
        
        if predict_number > number: # предполагаемое число больше предположенного
            max_number = predict_number - 1
            predict_number = (max_number + min_number) // 2
            
        if predict_number < number: # предполагаемое число меньше предположенного
            min_number = predict_number +1
            predict_number = (max_number + min_number) // 2
            
        else:
            break # выход из цикла если угадали число

    return count


def score_game(game_core_v3) -> int:
    """

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    random_array = np.random.randint(1, 101, size=(1000))  

    for number in random_array:
        count_ls.append(game_core_v3(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    
    score_game(game_core_v3)
