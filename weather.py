import pandas as pd


class Weather:

    def __init__(self):
        self.one_sec_data = pd.read_csv("one_weather.csv")
        self.track_data = pd.read_csv("track_weather.csv")
        self.coast_f_data = pd.read_csv("weather_during_coast.csv")
        self.time_data = self.one_sec_data.Time[1::]
        self.m_bar = self.one_sec_data.BAROM[1::]
        self.one_s_data = ""
        self.clean_track = []
        self.clean_one = []
        self.pressure = []
        self.final_list = []
        self.t_weather = []
        self.c_weather = []
        self.f_straight_list = []
        self.new_column_straight = []

    def final_output(self, index_list):
        i = 0

        while i < len(index_list):
            x = self.one_sec_data.iloc[index_list[i]]
            self.final_list.append(x)
            i += 1

        return self.final_list

    def pressure_conv(self):
        for item in self.m_bar:
            temp_var = float(item)
            self.pressure.append(temp_var)

    def pressure_output(self):
        i = 0
        while i < len(self.pressure):
            self.pressure[i] = self.pressure[i] / 10
            i += 1
        return self.pressure

    def track_w_list_con(self):
        i = 1
        while i < len(self.track_data.Time):
            str_time = self.track_data.iloc[i].Time
            self.t_weather.append(str_time)
            i += 1
        new_list = []
        j = 0
        while j < len(self.t_weather):
            k = 0
            str_con = ""
            while k < len(self.t_weather[j]):
                if self.t_weather[j][k] != ":":
                    str_con += self.t_weather[j][k]
                    k += 1
                else:
                    k += 1
                if k == len(self.t_weather[j]):
                    new_list.append(str_con)
            j += 1
        self.t_weather.clear()
        for item in new_list:
            self.t_weather.append(int(item))
        return self.t_weather

    def coast_w_list_con(self):
        i = 0
        while i < len(self.coast_f_data.Time):
            str_time = self.coast_f_data.iloc[i].Time
            self.c_weather.append(str_time)
            i += 1
        new_list = []
        j = 0
        while j < len(self.c_weather):
            k = 0
            str_con = ""
            while k < len(self.c_weather[j]):
                if self.c_weather[j][k] != ":":
                    str_con += self.c_weather[j][k]
                    k += 1
                else:
                    k += 1
                if k == len(self.c_weather[j]):
                    new_list.append(str_con)
            j += 1
        self.c_weather.clear()
        for item in new_list:
            self.c_weather.append(int(item))
        return self.c_weather

    def filtered_straight(self):
        i = 0
        while i < len(self.c_weather):
            j = 0
            k = 1
            while k < len(self.t_weather) and i < len(self.c_weather):
                if self.c_weather[i] == self.t_weather[k]:
                    self.f_straight_list.append(k)
                    i += 1
                elif self.t_weather[j] < self.c_weather[i] <= self.t_weather[k]:
                    self.f_straight_list.append(j)
                    i += 1
                else:
                    j += 1
                    k += 1
        return self.f_straight_list

    def new_straight_column(self):
        i = 0
        while i < len(self.f_straight_list):
            temp_var = self.track_data.iloc[self.f_straight_list[i]].Straight
            self.new_column_straight.append(temp_var)
            i += 1
        return self.new_column_straight
