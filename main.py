from vbox import Vbox
from utc_time import UtcTime
from weather import Weather
from results import Results
import cd_functions as cd
import pandas as pd


# Using file in FOA data V038/Data/Spec 1 - EU RLF-Low/Test9_04June

def pair_list_filter(v_obj, asc_list_indexes):
    speed_pairs_f_list = []
    odd_even_check = 0
    i = 0
    while i < len(asc_list_indexes):
        if odd_even_check % 2 == 0 and v_obj.data.iloc[asc_list_indexes[i]].velocity > 75:
            speed_pairs_f_list.append(asc_list_indexes[i])
            odd_even_check = 1
        elif odd_even_check % 2 == 1 and v_obj.data.iloc[asc_list_indexes[i]].velocity < 75:
            speed_pairs_f_list.append(asc_list_indexes[i])
            odd_even_check = 0
        i += 1
    return speed_pairs_f_list



# data = pd.read_csv("vbox_results_all_runs2.csv")
#
# print(data.Heading)
# print(type(data.iloc[0].Heading))
results = Results()
results.high_run_pull()
results.low_run_pull()

x = results.odd_run_fix()[0]
y = results.odd_run_fix()[1]
z = results.odd_run_fix()[2]

if results.tuple_creation_ideal():
    pairs_list = results.tuple_creation_ideal()
elif not results.tuple_creation_ideal():
    pairs_list = cd.updating_pairs(odd_list=x, index=y)
    print(pairs_list)
    if z > 5:
        results.high_index = pairs_list
    elif z < 5:
        results.low_index = pairs_list
cume_tup = results.tuple_creation_ideal()
print(cume_tup)
i = 0
j = 1
k = 0
total_high = 0
first_one_pair_cume = []
while i < len(cume_tup):
    while k < 5:
        high_sum = results.data.iloc[cume_tup[i]][results.high_dict["high"][k]]
        total_high += high_sum
        print(total_high)
        first_one_pair_cume.append(total_high)
        k += 1
    i += 1
    break



i = 0
n = 5
m = 0

while i < 3:
    h_v = results.data.iloc[cume_tup[0]][results.high_dict["high"][n]]
    l_v = results.data.iloc[cume_tup[1]][results.low_dict["low"][m]]
    sm = h_v + l_v
    aveee = sm/2
    total_high += aveee
    print(total_high)
    first_one_pair_cume.append(total_high)
    i += 1
    n += 1
    m += 1


total_low = first_one_pair_cume[-1]
k = 3
while j < len(cume_tup):

    while k < 7:
        low_sum = results.data.iloc[cume_tup[j]][results.low_dict["low"][k]]
        total_high += low_sum
        print(total_high)
        k += 1
    i += 1
    break
