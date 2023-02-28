# import time


def get_indexes(list_for_indexes, direction=1):
    '''
    :param direction: 1 direct
                     -1 reverse
    '''
    list_result = []
    j = len(list_for_indexes) - 1
    if direction == 1:
        for i in list_for_indexes:
            if i != 0:
                j += 1
            else:
                j = 0
            list_result.append(j)
    else:
        idx = len(list_for_indexes) - 1
        for item in reversed(list_for_indexes):
            if item == 0:
                j = 0
            elif j < item:
                j += 1
            elif j >= item:
                j = item
            list_for_indexes[idx] = j
            idx -= 1
        list_result = list_for_indexes

    return list_result


if __name__ == '__main__':
    n = int(input("Введите количество дач : "))
    dachas_list = [int(i) for i in input().split()]
    # start_time = time.time()
    indexes = get_indexes(dachas_list, 1)
    reversed_indexes = get_indexes(indexes, -1)
    print(reversed_indexes)
    # print("--%.3f milliseconds ---" % ((time.time() - start_time) * 1000))
