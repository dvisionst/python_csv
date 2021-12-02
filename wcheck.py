import pandas as pd
import math

FIVE_LIMIT = 5
TWO_LIMIT = 2
CROSS_LIMIT = 2


class Wcheck:

    def __init__(self):
        self.data = pd.read_csv("weather_during_coast.csv")
        self.five_r_ave = [0, 0, 0, 0]
        self.two_r_ave = [0]
        self.cross_wind = [0, 0, 0, 0]
        self.wind_speed = []
        self.wind_direction = []
        self.time = self.data.Time
        self.temp = self.data.AMBIENT
        self.fail = []

    def wind(self):
        for item in self.data.WSPD_MAX:
            self.wind_speed.append(item)
        for item in self.data.WNDDIR:
            self.wind_direction.append(item)
        return self.wind_speed, self.wind_direction

    def two_ave(self):
        i = 1
        while i < len(self.wind_speed):
            one = self.wind_speed[i - 1]
            two = self.wind_speed[i]
            two_ave = (one + two) / 2
            average = round(two_ave, 2)
            self.two_r_ave.append(average)
            i += 1
        return self.two_r_ave

    def five_ave(self):
        i = 4
        while i < len(self.wind_speed):
            one = self.wind_speed[i - 4]
            two = self.wind_speed[i - 3]
            three = self.wind_speed[i - 2]
            four = self.wind_speed[i - 1]
            five = self.wind_speed[i]
            ave = (one + two + three + four + five) / 5
            average = round(ave, 2)
            self.five_r_ave.append(average)
            i += 1
        return self.five_r_ave

    def cross_w(self):
        i = 4
        angle = 41.68
        while i < len(self.five_r_ave):
            x = self.wind_direction[i]
            y = self.five_r_ave[i]
            z = math.sin(math.radians(x - angle)) * y
            final = round(math.sqrt(z ** 2), 2)
            self.cross_wind.append(final)
            i += 1
        return self.cross_wind

    def pass_fail(self):
        i = 1
        max_2r_wind_fail = []
        while i < len(self.two_r_ave):
            if self.two_r_ave[i] > 8:
                time_stamp = self.time[i]
                max_2r_wind_fail.append(time_stamp)
                i += 1
            else:
                i += 1
        max_wind_2 = {"2s_max_fail": max_2r_wind_fail}
        self.fail.append(max_wind_2)
        
        j = 4
        max_5r_wind_fail = []
        while j < len(self.five_r_ave):
            if self.five_r_ave[j] > 5:
                t_stamp = self.time[j]
                max_5r_wind_fail.append(t_stamp)
                j += 1
            else:
                j += 1
        max_wind_5 = {"5s_max_fail": max_5r_wind_fail}
        self.fail.append(max_wind_5)

        k = 4
        cross_wind_fail = []
        while k < len(self.cross_wind):
            if self.cross_wind[k] > 2:
                time = self.time[k]
                cross_wind_fail.append(time)
                k += 1
            else:
                k += 1
        cross_fail = {"cross wind fail": cross_wind_fail}
        self.fail.append(cross_fail)

        starting_temp = self.temp[0]
        ending_temp = self.temp[-1]
        temp_difference = abs(ending_temp - starting_temp)
        if temp_difference > 5:
            temp_difference_fail = "temperature failure due to difference more than 5 degrees"
            self.fail.append(temp_difference_fail)
        return self.fail








