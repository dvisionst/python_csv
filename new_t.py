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

    def wind_speed_array(self):
        for item in self.data.WSPD_MAX:
            self.wind_speed.append(item)
        return self.wind_speed

    def wind_dir_array(self):
        for item in self.data.WNDDIR:
            self.wind_direction.append(item)
        return self.wind_direction

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

    def cross_wind(self):
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
        i = 0




