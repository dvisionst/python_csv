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



# i = 0
# stopping = len(vbox_times) - 1
# ending = len(weather_str_list) - 1
#
# # looping through the lists in order to determine if time signature occurs during coast
# # loop with embedded true condition print statements
# while i <= ending:
#     k = 0
#     j = 1
#     if vbox_times[k] <= weather_str_list[i] <= vbox_times[j]:
#         print(weather_str_list[i], True)
#         i = i + 1
#         continue
#     elif i == ending:
#         break
#     else:
#         l = 3
#         n = 2
#         m = 2
#         while n < stopping:
#             if weather_str_list[i] == weather_str_list[-1]:
#                 print(weather_str_list[i], True)
#                 break
#             elif vbox_times[m] <= weather_str_list[i] <= vbox_times[l]:
#                 print(weather_str_list[i], True)
#                 i = i + 1
#                 continue
#             else:
#                 m = m + 2
#                 l = l + 2
#                 n = n + 2
#     i = i + 1