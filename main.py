from vbox import Vbox
from utc_time import UtcTime
import cd_functions
import weather


WLTP_HIGH_B_SPEED = 135
WLTP_HIGH_E_SPEED = 55
WLTP_LOW_B_SPEED = 85
WLTP_LOW_15_SPEED = 15
NEDC_HIGH_B_SPEED = 125
NEDC_HIGH_E_SPEED = 55
NEDC_LOW_B_SPEED = 85
NEDC_LOW_E_SPEED = 15

time_column = Vbox()
time_column.speed_conditions(WLTP_HIGH_B_SPEED, WLTP_HIGH_E_SPEED)

utc_t_obj = UtcTime()
utc_t_obj.utc_type_conv(time_column.time_stamp())
utc_t_obj.az_time_list()

main_weather_track = weather.Weather()


coast_times_str = utc_t_obj.az_times
vbox_times = []
track_weather_times = cd_functions.formatting_t(main_weather_track.time_data)
weather_str_list = []

for item in coast_times_str:
    vbox_times.append(int(item))
print(vbox_times)

for item in track_weather_times:
    weather_str_list.append(int(item))

print(weather_str_list)



# print(time_column.time_stamp())

# df = pandas.DataFrame(test_list)
# df.to_csv("SEE_huh.csv")
