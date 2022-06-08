# This class is used for the raw VBOX data collected during the coastdown. It creates a Dataframe that allows the
# main program to search for key timestamp values using the start and stop velocities during coastdown.

import pandas


class Vbox:

    def __init__(self):
        self.data = pandas.read_csv("coast_data_IN.csv", low_memory=False)
        self.time_c = self.data.velocity
        self.t_stamp_series = []
        self.filtered_time_list = []
        self.splits_indices = []

    def mod_times(self, high_leg_begin, high_leg_end, low_leg_begin, low_leg_end):
        leg_index = 1
        k = 0
        i = 1
        j = 10
        while j < len(self.time_c):
            while leg_index % 2 != 0 and j < len(self.time_c):
                trigger = 1
                count = 0
                while j < len(self.time_c) and count < 4:
                    if trigger % 2 != 0:
                        if self.time_c[j] < self.time_c[i] < high_leg_begin <= self.time_c[k]:
                            self.splits_indices.append(i)
                            count += 1
                            trigger += 1
                        k += 1
                        i += 1
                        j += 1
                    elif trigger % 2 == 0:
                        if self.time_c[j] < self.time_c[i] < high_leg_end <= self.time_c[k]:
                            self.splits_indices.append(i)
                            count += 1
                            trigger += 1
                        k += 1
                        i += 1
                        j += 1
                leg_index += 1
            while leg_index % 2 == 0 and j < len(self.time_c):
                trigger = 1
                count = 0
                while j < len(self.time_c) and count < 4:
                    if trigger % 2 != 0:
                        if self.time_c[j] < self.time_c[i] < low_leg_begin <= self.time_c[k]:
                            self.splits_indices.append(i)
                            count += 1
                            trigger += 1
                        k += 1
                        i += 1
                        j += 1
                    elif trigger % 2 == 0:
                        if self.time_c[j] < self.time_c[i] < low_leg_end <= self.time_c[k]:
                            self.splits_indices.append(i)
                            count += 1
                            trigger += 1
                        k += 1
                        i += 1
                        j += 1
                leg_index += 1
        return self.splits_indices

    def mod_times_single(self, starting_velocity, ending_velocity):
        k = 0
        i = 1
        j = 10

        trigger = 1
        while j < len(self.time_c):

            if trigger % 2 != 0:
                if self.time_c[j] < self.time_c[i] < starting_velocity <= self.time_c[k]:
                    self.splits_indices.append(i)
                    trigger += 1
                k += 1
                i += 1
                j += 1
            elif trigger % 2 == 0:

                if self.time_c[j] < self.time_c[i] < ending_velocity <= self.time_c[k]:
                    self.splits_indices.append(i)
                    trigger += 1
                k += 1
                i += 1
                j += 1
        return self.splits_indices

    def time_stamp(self, index_list):
        i = 0
        while i < len(index_list):
            temp_var = self.data.iloc[index_list[i]].time
            self.filtered_time_list.append(temp_var)
            i += 1
        return self.filtered_time_list
