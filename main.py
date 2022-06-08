# The goal of this program is to process coastdown data and weather data jointly for any coastdown test.
# It takes 4 csv data files, 2 of which are weather data files. The other 2 are data files from the VBOX used
# during the test. This program outputs up to 3 files. One file is the one second weather data for only the times in
# which the vehicle is coasting. The other file is has the cumulative times of the speed gates, the
# timestamps, and just the speed gates. The third file may or may not be an output, it depends on if the test passed
# the weather requirements. If the test fails, the file is outputted with the parameter that failed along with the
# timestamps where the failure occurred.
# This program can process single or split runs, and WLTP or NEDC speed conditions.

from vbox import Vbox
from utc_time import UtcTime
from weather import Weather
from results import Results
from wcheck import Wcheck
import cd_functions as cd
import pandas as pd


HIGH_E_SPEED = 55
LOW_B_SPEED = 65
LOW_E_SPEED = 15

test_runs = input("Was this test done with Split Runs? Type 'y' for YES, Type 'n' for NO:  \n").lower()
coast_down_processor_on = True
test_type = input("For WLTP test press 'w', for NEDC press 'n': \n").lower()

# if test_runs == "y":
#     overlap_runs = input("For three overlaps press '3', for a single overlap press '1':  \n").lower()
#     if overlap_runs == "3":
#
#         overlaps = True
#     else:
#         LOW_B_SPEED = 65
#         overlaps = False

if test_type == 'w':
    HIGH_B_SPEED = 135
else:
    HIGH_B_SPEED = 125

while coast_down_processor_on:

    if test_runs == "y":
        # This next block of code creates uses two list of indices one of the high start velocities and one of the
        # low stop velocities. Using these two lists, they are arranged and a new list of timestamps is created.
        vbox_high = Vbox()
        all_runs_indices = vbox_high.mod_times(high_leg_begin=HIGH_B_SPEED, high_leg_end=HIGH_E_SPEED,
                                               low_leg_begin=LOW_B_SPEED, low_leg_end=LOW_E_SPEED)
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
        df.to_csv("weather_during_coast_OUT.csv")
        results = Results()
        if test_type == 'w':
            results.high_run_pull(test_type=True)
            results.low_run_pull()
            results.loop_index()
            results.output_pairs_list()
            results.top_vel_accume()
            results.mid_ave_accume()
            results.low_vel_accume()
            results.add_leg_stamps(coast_times_str)
            results.w_run_analysis()
            results.accuracy_percentage()
            results.second_loop(weather.current_string_stamps, test_type=test_runs)
            results.final_dataframe()
            df = pd.DataFrame(results.columns)
            df.to_csv("cumulative_times_results_OUT.csv")
        elif test_type != "w":
            results.high_run_pull(test_type=False)
            results.low_run_pull()
            results.loop_index()
            results.output_pairs_list()
            results.top_vel_accume()
            results.mid_ave_accume()
            results.low_vel_accume()
            results.add_leg_stamps(coast_times_str)
            results.w_run_analysis()
            results.accuracy_percentage()
            results.second_loop(weather.current_string_stamps, test_type=test_type)
            results.final_dataframe()
            df = pd.DataFrame(results.columns)
            df.to_csv("cumulative_times_results_OUT.csv")

        coast_down_processor_on = False

    elif test_runs == "n":
        vbox_high = Vbox()
        all_runs_indices = vbox_high.mod_times_single(starting_velocity=HIGH_B_SPEED, ending_velocity=LOW_E_SPEED)
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
        df.to_csv("weather_during_coast_OUT.csv")

        results = Results()
        if test_type == 'w':
            results.high_run_pull(test_type=True)
            results.loop_index()
            results.output_pairs_list()
            results.top_vel_single()
            results.add_leg_stamps_single(coast_times_str)
            results.w_run_analysis_s()
            results.accuracy_percentage()
            results.second_loop(weather.current_string_stamps, test_type=test_type)
            results.final_dataframe()
            df = pd.DataFrame(results.columns)
            df.to_csv("cumulative_times_results_OUT.csv")
        elif test_type != "w":
            results.high_run_pull(test_type=False)
            results.loop_index()
            results.output_pairs_list()
            results.top_vel_single(test_type=False)
            results.add_leg_stamps_single(coast_times_str)
            results.w_run_analysis_s()
            results.accuracy_percentage()
            results.second_loop(weather.current_string_stamps, test_type=test_type)
            results.final_dataframe()
            df = pd.DataFrame(results.columns)
            df.to_csv("cumulative_times_results_OUT.csv")
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

new_straightaway_column = {"STRAIGHT": track_weather}
t_df = pd.DataFrame(new_straightaway_column)
data1 = pd.read_csv("weather_during_coast_OUT.csv")
data1.insert(loc=11, column="Straightaway", value=track_weather)
data1.to_csv("weather_during_coast_OUT.csv")

wc = Wcheck()
wc.wind()
wc.two_ave()
wc.five_ave()
wc.cross_w()
failure = wc.pass_fail()

if failure != []:
    df = pd.DataFrame(failure)
    df.to_csv("weather_failures_OUT.csv")
    print("The Coastdown test fails due to weather, for more information open up 'weather_failures.csv' file.")

print("The program has completed, you can now view the results in two csv files\n")
print("Those files are: 'weather_during_coast' & 'cumulative_times_results'\n")
