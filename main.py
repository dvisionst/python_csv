from vbox import Vbox
from utc_time import UtcTime
from weather import Weather
from results import Results
import cd_functions as cd
import pandas as pd


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


HIGH_E_SPEED = 55
LOW_B_SPEED = 85
LOW_E_SPEED = 15

test_runs = input("Was this test done with Split Runs? Type 'y' for YES, Type 'n' for NO:  \n").lower()
coast_down_processor_on = True
test_type = input("For WLTP test press 'w', for NEDC press 'n': \n").lower()
if test_type == 'w':
    HIGH_B_SPEED = 135
else:
    HIGH_B_SPEED = 125

while coast_down_processor_on:

    if test_runs == "y":
        vbox_high = Vbox()
        h_pair_start_array = vbox_high.start_trig_times(high_end_speed=HIGH_B_SPEED)
        h_pair_stop_array = vbox_high.stop_trig_times(low_end_speed=HIGH_E_SPEED)
        sorted_high_list = cd.total_index_sort(start_list=h_pair_start_array, stop_list=h_pair_stop_array)
        filtered_h_pair_indices = pair_list_filter(vbox_high, sorted_high_list)

        vbox_low = Vbox()
        l_pair_start_array = vbox_low.start_trig_times(high_end_speed=LOW_B_SPEED)
        l_pair_end_array = vbox_low.stop_trig_times(low_end_speed=LOW_E_SPEED)
        sorted_low_list = cd.total_index_sort(start_list=l_pair_start_array, stop_list=l_pair_end_array)
        filtered_l_pair_indices = pair_list_filter(vbox_low, sorted_low_list)

        filtered_h_pair_indices.extend(filtered_l_pair_indices)
        filtered_h_pair_indices.sort()
        all_runs_indices = filtered_h_pair_indices
        time_stamps_raw = vbox_high.time_stamp(all_runs_indices)

        utc = UtcTime()
        utc.utc_type_conv(time_stamps_raw)
        utc.az_time_list()
        coast_times_str = utc.az_times
        coast_times = cd.time_to_integers(coast_times_str)

        weather = Weather()
        weather_times_str = cd.formatting_t(weather.time_data)
        coast_weather_times_int = cd.time_to_integers(weather_times_str)
        c_weather_ind = cd.weather_during_coast_full(list_of_weather_t=coast_weather_times_int,
                                                     list_of_time_stamps=coast_times)

        final_list = weather.final_output(c_weather_ind)
        weather.pressure_conv()
        kpa_metric_pressure = weather.pressure_output()
        kpa_metric_pressure.insert(0, "kPa")
        new_pressure_column = {"BAROM": kpa_metric_pressure}
        new_df = pd.DataFrame(new_pressure_column)
        df = pd.DataFrame(final_list)
        df.update(new_df)
        df.to_csv("weather_during_coast.csv")

        results = Results()
        if test_type == 'w':
            results.high_run_pull(test_type=True)
            results.low_run_pull()
            results.loop_index()
            results.output_pairs_list()
            results.top_vel_accume(t_type=True)
            results.mid_ave_accume()
            results.low_vel_accume()
            results.final_dataframe()
            df = pd.DataFrame(results.columns)
            df.to_csv("cumulative_times_results.csv")
        elif test_type != "w":
            results.high_run_pull(test_type=False)
            results.low_run_pull()
            results.loop_index()
            results.output_pairs_list()
            results.top_vel_accume(t_type=False)
            results.mid_ave_accume()
            results.low_vel_accume()
            results.final_dataframe()
            df = pd.DataFrame(results.columns)
            df.to_csv("cumulative_times_results.csv")

        coast_down_processor_on = False

    elif test_runs == "n":
        vbox_high = Vbox()
        h_pair_start_array = vbox_high.start_trig_times(high_end_speed=HIGH_B_SPEED)
        h_pair_stop_array = vbox_high.stop_trig_times(low_end_speed=LOW_E_SPEED)
        sorted_high_list = cd.total_index_sort(start_list=h_pair_start_array, stop_list=h_pair_stop_array)
        filtered_h_pair_indices = pair_list_filter(vbox_high, sorted_high_list)

        all_runs_indices = filtered_h_pair_indices
        time_stamps_raw = vbox_high.time_stamp(all_runs_indices)

        utc = UtcTime()
        utc.utc_type_conv(time_stamps_raw)
        utc.az_time_list()
        coast_times_str = utc.az_times
        coast_times = cd.time_to_integers(coast_times_str)

        weather = Weather()
        weather_times_str = cd.formatting_t(weather.time_data)
        coast_weather_times_int = cd.time_to_integers(weather_times_str)
        c_weather_ind = cd.weather_during_coast_full(list_of_weather_t=coast_weather_times_int,
                                                     list_of_time_stamps=coast_times)

        final_list = weather.final_output(c_weather_ind)
        weather.pressure_conv()
        kpa_metric_pressure = weather.pressure_output()
        kpa_metric_pressure.insert(0, "kPa")
        new_pressure_column = {"BAROM": kpa_metric_pressure}
        new_df = pd.DataFrame(new_pressure_column)
        df = pd.DataFrame(final_list)
        df.update(new_df)
        df.to_csv("weather_during_coast.csv")

        results = Results()
        if test_type == 'w':
            results.high_run_pull(test_type=True)
            results.loop_index()
            results.output_pairs_list()
            results.top_vel_single(test_type=True)
            results.final_dataframe()
            df = pd.DataFrame(results.columns)
            df.to_csv("cumulative_times_results.csv")
        elif test_type != "w":
            results.high_run_pull(test_type=False)
            results.loop_index()
            results.output_pairs_list()
            results.top_vel_single(test_type=False)
            results.final_dataframe()
            df = pd.DataFrame(results.columns)
            df.to_csv("cumulative_times_results.csv")

        coast_down_processor_on = False

    else:
        re_start = input("That was an invalid input, pres 'y' to try again.\n").lower()
        if re_start == 'y':
            test_runs = input("Was this test done with Split Runs? Type 'y' for YES, Type 'n' for NO:  \n").lower()
        else:
            print("You have terminated the Coastdown Processor.")
            coast_down_processor_on = False

weather = Weather()
weather.track_w_list_con()
weather.coast_w_list_con()
weather.filtered_straight()
track_weather = weather.new_straight_column()
data1 = pd.read_csv("weather_during_coast.csv")
data1.insert(loc=11, column="Straightaway", value=track_weather)
data1.to_csv("weather_during_coast.csv")

print("The program has completed, you can now view the results in two csv files\n")
print("Those files are: 'weather_during_coast' & 'cumulative_times_results'\n")
