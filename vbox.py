import pandas


class Vbox:

    def __init__(self):
        self.data = pandas.read_csv("coast_data.csv", low_memory=False)
        self.time_c = self.data.velocity
        self.v_array = []
        self.t_stamp_series = []
        self.filtered_time_list = []

    def speed_conditions(self, high_end_speed, low_end_speed):
        empty_list = []
        i = 0
        j = 1
        while j < len(self.time_c):
            if self.time_c[j] < self.time_c[i] and self.time_c[j] < high_end_speed <= self.time_c[i]:
                empty_list.append(self.time_c[j])
            elif self.time_c[j] < self.time_c[i] and self.time_c[j] < low_end_speed <= self.time_c[i]:
                empty_list.append(self.time_c[j])
            i += 1
            j += 1
            self.v_array = empty_list
        return self.v_array

    def time_stamp(self):
        i = 0
        while i < len(self.time_c):

            if self.time_c[i] in self.v_array:
                row_series = self.data.iloc[i]
                self.t_stamp_series.append(row_series)
            i += 1
        for item in self.t_stamp_series:
            self.filtered_time_list.append(item.time)
        return self.filtered_time_list
