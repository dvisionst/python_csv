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



data = pd.read_csv("vbox_results_all_runs2.csv")

print(data.Heading)
print(type(data.iloc[0].Heading))
results = Results()
print(results.high_run_pull())
print(len(results.high_index))
print(results.low_run_pull())
print(len(results.low_index))



