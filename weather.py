import pandas as pd


class Weather:

    def __init__(self):
        self.track_data = pd.read_csv("one_weather.csv")
        self.time_data = self.track_data.Time[1::]
        self.m_bar = self.track_data.BAROM[1::]
        self.one_s_data = ""
        self.clean_track = []
        self.clean_one = []
        self.pressure = []

    def final_output(self, index_list):
        final_list = []
        i = 0
        while i < len(index_list):
            x = self.track_data.iloc[index_list[i]]
            final_list.append(x)
            i += 1
        return final_list

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
