# УСЛОВИЯ ЗАДАНИЯ

# Компьютер загадывает целое число от 1 до 100, и нам его нужно угадать. Под «угадать» подразумевается «написать программу, которая угадывает число».
# Алгоритм учитывает информацию о том, больше или меньше случайное число нужного нам числа.
# Представлен шаблон baseline из скринкаста.


# МЕТРИКА КАЧЕСТВА
# Результаты оцениваются по среднему количеству попыток при 1000 повторений. Необходимо добиться минимального количества попыток.

# учитывая что диапазон в котором может находится число нам известен и представляет собой отрезок от 1 до 100, то можно использовать алгоритм бинарного поиска. онг будет оптимален в данных условиях
# основная идея заключается в отсечении половины вариантов при каждой попытке. т.е. если число больше угадываемого то отсекаем все числа меньше того которое было названо. называть следует число находящееся в центре промежутка.
# временная сложность алгоритма O(logn)
# память О(1)
import numpy as np
def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь
    count = 0;
    start = 1;
    end = 1000;
    middle = end / 2;
    
    while True:
      # в любом случае увеличиваем кол во попыток так как пошел новый круг
        count += 1
        if middle == number:
            return count
        if middle < number:
        # отсекаем всю правую часть - оставляем левую и пересчитываем середину.
            start = middle
            middle = int((start+end) / 2) 
        if middle > number:
        # отсекаем всю левую часть - оставляем правую и пересчитываем середину.
            end = middle
            middle = int((start + end )/ 2)
            
random_int = np.random.randint(1, 101)        
game_core_v3(random_int);        

        
      
      
    
    

