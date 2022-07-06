def task(array):
    '''Поиск в строке индекса, где происходит смена числа'''

    array = [i for i in array]
    start_symb = array[0]
    index = 1
    for i in range(1, len(array)):
        if array[i] != start_symb:
            return index
        else:
            index += 1
    return 'Не было изменения первого числа'

print(task('1111111111111100'))