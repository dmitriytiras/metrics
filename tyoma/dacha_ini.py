def get_indexes(list_for_indexes, direction=1):
    '''
    :param list_for_indexes:
    :param direction: 1 direct
                     -1 reverse
    :return: result
    '''
    list_result = []
    j = len(list_for_indexes)
    if direction == 1:
        for i in list_for_indexes:
            if i != 0:
                j += 1
            else:
                j = 0
            list_result.append(j)
    else:
        idx = len(list_for_indexes) - 1
        k = 0
        for item in reversed(list_for_indexes):
            if item == 0:
                k = 1
            if item != 0 and k > 0:
                if k > item:
                    k = item
                list_for_indexes[idx] = k
                k += 1
            idx -= 1
        list_result = list_for_indexes
    return list_result


if __name__ == '__main__':
    n = int(input("Введите количество дач : "))
    dachas_list = [int(i) for i in input().split()]
    indexes = get_indexes(dachas_list, 1)
    reversed_indexes = get_indexes(indexes, -1)
    print(reversed_indexes)