import pandas as pd
import math
data = pd.read_csv("weather_during_coast.csv")


def five_rolling_ave_wspd(list_values, variable):
    one = list_values[variable - 4]
    two = list_values[variable - 3]
    three = list_values[variable - 2]
    four = list_values[variable - 1]
    five = list_values[variable]
    five_ave = (one + two + three + four + five)/5
    return round(five_ave, 2)


def cross_check(ave_w_list, w_dir_list):
    i = 0
    j = 4
    angle = 41.68
    x_cross = []
    while i < len(ave_w_list) or j < len(w_dir_list):
        x = w_dir_list[j]
        y = ave_w_list[i]
        z = math.sin(math.radians(x - angle))*y
        final = round(math.sqrt(z**2), 2)
        x_cross.append(final)
        i += 1
        j += 1
    return x_cross

wind_speed = []

for item in data.WSPD_MAX:
    wind_speed.append(item)
# WNDDIR
i = 4
five_sec_wspd = []
while i < len(wind_speed):
    avee = five_rolling_ave_wspd(wind_speed, i)
    five_sec_wspd.append(avee)
    i += 1

emp = []
for item in data.WNDDIR:
    emp.append(item)

xxx = cross_check(five_sec_wspd, emp)
print(xxx)
