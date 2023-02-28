from typing import List


def get_distances_to_empty_plot(house_numbers: List[int]) -> List[float]:
    distances = [0] * len(house_numbers)
    empty_plot = -1
    for plot_index, house_number in enumerate(house_numbers, start=0):
        if house_number == 0:
            if empty_plot == -1:
                distances[0:plot_index] = distances[:plot_index][::-1]
                empty_plot = plot_index
            else:
                i = max(divmod((plot_index - empty_plot - 1), 2))
                distances[plot_index - i:plot_index] = distances[
                    empty_plot + i:empty_plot:-1]
                empty_plot = plot_index
        else:
            if empty_plot >= 0:
                distances[plot_index] = plot_index - empty_plot
            else:
                distances[plot_index] = plot_index + 1
    return distances


def read_input() -> List[int]:
    _ = int(input())
    house_numbers = [int(_) for _ in input().strip().split()]
    return house_numbers


if __name__ == '_main_':
    house_numbers = read_input()
    print(*get_distances_to_empty_plot(house_numbers))