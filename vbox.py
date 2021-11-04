import pandas


class Vbox:

    def __init__(self):
        self.data = pandas.read_csv("coast_data.csv", low_memory=False)
        self.time_c = self.data.velocity
        self.t_stamp_series = []
        self.filtered_time_list = []
        self.high_speed_indices = []
        self.low_speed_indices = []

    def start_trig_times(self, high_end_speed):
        k = 0
        i = 1
        j = 10
        while j < len(self.time_c):
            if self.time_c[j] < self.time_c[i] < high_end_speed <= self.time_c[k]:
                self.high_speed_indices.append(i)
            k += 1
            i += 1
            j += 1
        return self.high_speed_indices

    def stop_trig_times(self, low_end_speed):
        k = 0
        i = 1
        j = 10
        while j < len(self.time_c):
            if self.time_c[j] < self.time_c[i] < low_end_speed <= self.time_c[k]:
                self.low_speed_indices.append(i)
            k += 1
            i += 1
            j += 1
        return self.low_speed_indices

    def time_stamp(self, index_list):
        i = 0
        while i < len(index_list):
            temp_var = self.data.iloc[index_list[i]].time
            self.filtered_time_list.append(temp_var)
            i += 1
        return self.filtered_time_list



