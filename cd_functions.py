STRING_NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def formatting_t(some_list):
    new_list = []
    i = 1
    while i <= len(some_list):
        j = 0
        new_string = ""
        while j < len(some_list[i]):
            if some_list[i][j] in STRING_NUMBERS:
                new_string += some_list[i][j]
            j += 1

        new_list.append(new_string)
        i += 1
    return new_list


def time_to_integers(list_of_times):
    int_times = []
    for item in list_of_times:
        int_times.append(int(item))
    return int_times


def total_index_sort(start_list, stop_list):
    start_list.extend(stop_list)
    start_list.sort()
    return start_list


def weather_during_coast_full(list_of_weather_t, list_of_time_stamps):
    i = 0
    stopping = len(list_of_time_stamps) - 1
    ending = len(list_of_weather_t) - 1
    index_list = []
    while i <= ending:
        k = 0
        j = 1
        if list_of_time_stamps[k] <= list_of_weather_t[i] <= list_of_time_stamps[j]:
            i += 1
            index_list.append(i)
            continue
        elif i == ending:
            break
        else:
            p = 3
            n = 2
            m = 2
            while n < stopping:
                if list_of_weather_t[i] == list_of_weather_t[-1]:
                    print(list_of_weather_t[i], True)
                    break
                elif list_of_time_stamps[m] <= list_of_weather_t[i] <= list_of_time_stamps[p]:
                    i += 1
                    index_list.append(i)
                    continue
                else:
                    m += 2
                    p += 2
                    n += 2
        i += 1
    return index_list


def updating_pairs(odd_list, index):
    empty = []
    for item in odd_list:
        empty.append(item)
    empty.pop(index)
    return empty
