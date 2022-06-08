import pandas as pd
import statistics as st

pair_number = range(1, 12)
pair_letter = ('a', 'b')


class Results:

    def __init__(self):
        self.data = pd.read_csv("vbox_runs_IN.csv")
        self.high_index = []
        self.low_index = []
        self.all_s_gate_t = []
        self.high_dict = {
            "high": [
                '135 - 125 (s)',
                '125 - 115 (s)',
                '115 - 105 (s)',
                '105 - 95 (s)',
                '95 - 85 (s)',
                '85 - 75 (s)',
                '75 - 65 (s)',
                '65 - 55 (s)'
            ]
        }
        self.low_dict = {
            "low": [
                '65 - 55 (s)',
                '55 - 45 (s)',
                '45 - 35 (s)',
                '35 - 25 (s)',
                '25 - 15 (s)'
            ]
        }
        self.single_dict = {
            "high": [
                '135 - 125 (s)',
                '125 - 115 (s)',
                '115 - 105 (s)',
                '105 - 95 (s)',
                '95 - 85 (s)',
                '85 - 75 (s)',
                '75 - 65 (s)',
                '65 - 55 (s)',
                '55 - 45 (s)',
                '45 - 35 (s)',
                '35 - 25 (s)',
                '25 - 15 (s)'

            ]
        }
        self.loop_count = 0
        self.p_values_out = []
        self.high_sum = 0
        self.overlap_values = []
        self.low_sum = 0
        self.columns = {}
        self.pair_stamp_a = []
        self.pair_stamp_b = []
        self.time_stamp_m = []
        self.time_stamp_s = []
        self.c_leg_a = []
        self.c_leg_b = []

    def loop_index(self):
        self.loop_count = len(self.high_index) / 2
        return self.loop_count

    def high_run_pull(self, test_type):
        i = 0
        if test_type:
            t = 0
        else:
            t = 1
        while i < len(self.data.Run):
            if self.data.iloc[i][self.high_dict['high'][t]] > 0:
                self.high_index.append(i)
            i += 1
        return self.high_index

    def low_run_pull(self):
        i = 0
        while i < len(self.data.Run):
            if self.data.iloc[i][self.low_dict['low'][-1]] > 0:
                self.low_index.append(i)
            i += 1
        return self.low_index

    def output_pairs_list(self):
        for item in range(0, int(self.loop_count) * 2):
            new_blank = []
            self.p_values_out.append(new_blank)
        return self.p_values_out

    def top_vel_accume(self):
        i = 0
        while i < self.loop_count * 2:
            self.p_values_out[i].append(0)
            total = 0
            k = 0
            while k < 7:
                self.high_sum = self.data.iloc[self.high_index[i]][self.high_dict["high"][k]]
                total += round(self.high_sum, 3)
                self.p_values_out[i].append(total)
                k += 1
            i += 1
        return self.p_values_out

    def transition_value(self):
        i = 0
        self.overlap_values.clear()
        while i < len(self.p_values_out):
            last_sum = self.p_values_out[i][-1]
            self.overlap_values.append(last_sum)
            i += 1
        return self.overlap_values

    def mid_ave_accume(self):
        i = 0
        self.transition_value()
        while i < self.loop_count * 2:
            k = 7
            j = 0
            total = self.overlap_values[i]
            while k < 8:
                h_v = self.data.iloc[self.high_index[i]][self.high_dict["high"][k]]
                l_v = self.data.iloc[self.low_index[i]][self.low_dict["low"][j]]
                data_tup = (h_v, l_v)
                overlap_average = st.harmonic_mean(data_tup)
                total += round(overlap_average, 3)
                self.p_values_out[i].append(total)
                k += 1
                j += 1
            j += 1
            i += 1
        return self.p_values_out

    def low_vel_accume(self):
        i = 0
        self.transition_value()
        while i < self.loop_count * 2:
            total = self.overlap_values[i]
            k = 1
            while k < 5:
                self.low_sum = self.data.iloc[self.low_index[i]][self.low_dict["low"][k]]
                total += round(self.low_sum, 3)
                self.p_values_out[i].append(total)
                k += 1
            i += 1
        return self.p_values_out

    def top_vel_single(self):
        i = 0

        while i < self.loop_count * 2:
            self.p_values_out[i].append(0)
            total = 0
            k = 0
            while k < 12:
                self.high_sum = self.data.iloc[self.high_index[i]][self.single_dict["high"][k]]
                total += round(self.high_sum, 3)
                self.p_values_out[i].append(total)
                k += 1
            i += 1

        return self.p_values_out

    def separator(self):
        m = 0
        while m < 2:
            n = 0
            while n < len(self.p_values_out):
                self.p_values_out[n].append(" ")
                n += 1
            m += 1

    def add_leg_stamps(self, time_list):
        self.separator()
        j = 0
        while j < len(time_list):
            k = 0
            str_con = ""
            while k < len(time_list[j]):
                if len(time_list[j]) < 6:
                    if k == 1 or k == 3:
                        str_con += ":" + time_list[j][k]
                    else:
                        str_con += time_list[j][k]
                    k += 1

                else:
                    if k == 2 or k == 4:
                        str_con += ":" + time_list[j][k]
                    else:
                        str_con += time_list[j][k]
                    k += 1
            self.time_stamp_m.append(str_con)
            j += 1
        self.multiple_stamps(self.time_stamp_m)

    def multiple_stamps(self, new_list):
        i = 0
        while i < len(new_list):
            self.pair_stamp_a.append(new_list[i])
            self.pair_stamp_a.append(new_list[i + 1])
            self.pair_stamp_a.append(new_list[i + 2])
            self.pair_stamp_a.append(new_list[i + 3])
            i += 8
        j = 4
        while j < len(new_list):
            self.pair_stamp_b.append(new_list[j])
            self.pair_stamp_b.append(new_list[j + 1])
            self.pair_stamp_b.append(new_list[j + 2])
            self.pair_stamp_b.append(new_list[j + 3])
            j += 8
        i = 0
        k = 0
        while i < len(self.p_values_out):
            self.p_values_out[i].append(self.pair_stamp_a[k])
            self.p_values_out[i].append(self.pair_stamp_a[k + 1])
            self.p_values_out[i].append(self.pair_stamp_b[k])
            self.p_values_out[i].append(self.pair_stamp_b[k + 1])
            i += 1
            k += 2
        self.separator()
        return self.p_values_out

    def add_leg_stamps_single(self, time_list):
        self.separator()
        j = 0
        while j < len(time_list):
            k = 0
            str_con = ""
            while k < len(time_list[j]):
                if len(time_list[j]) < 6:
                    if k == 1 or k == 3:
                        str_con += ":" + time_list[j][k]
                    else:
                        str_con += time_list[j][k]
                    k += 1

                else:
                    if k == 2 or k == 4:
                        str_con += ":" + time_list[j][k]
                    else:
                        str_con += time_list[j][k]
                    k += 1
            self.time_stamp_s.append(str_con)
            j += 1
        self.single_stamp(self.time_stamp_s)

    def single_stamp(self, new_list):
        i = 0
        while i < len(new_list):
            self.pair_stamp_a.append(new_list[i])
            self.pair_stamp_a.append(new_list[i + 1])

            i += 2
        i = 0
        k = 0
        j = 1
        while i < len(self.p_values_out):
            self.p_values_out[i].append(self.pair_stamp_a[k])
            self.p_values_out[i].append(self.pair_stamp_a[j])
            i += 1
            k += 2
            j += 2
        self.separator()

        return self.p_values_out

    def w_run_analysis(self):
        self.high_sum = []
        self.low_sum = []
        i = 0
        while i < self.loop_count * 2:
            self.p_values_out[i].append(0)
            total = 0
            k = 0
            while k < 8:
                self.high_sum = self.data.iloc[self.high_index[i]][self.high_dict["high"][k]]
                total = round(self.high_sum, 3)
                self.p_values_out[i].append(total)
                k += 1
            i += 1
        self.separator()
        i = 0
        while i < self.loop_count * 2:
            self.p_values_out[i].append(0)
            total = 0
            k = 0
            while k < 5:
                self.low_sum = self.data.iloc[self.low_index[i]][self.low_dict["low"][k]]
                total = self.low_sum
                self.p_values_out[i].append(total)
                k += 1
            i += 1

        return self.p_values_out

    def w_run_analysis_s(self):
        self.high_sum = []
        i = 0
        while i < self.loop_count * 2:
            self.p_values_out[i].append(0)
            total = 0
            k = 0

            while k < 12:
                self.high_sum = self.data.iloc[self.high_index[i]][self.single_dict["high"][k]]
                total = round(self.high_sum, 3)
                self.p_values_out[i].append(total)
                k += 1
            i += 1

        return self.p_values_out

    def final_dataframe(self):
        pair_legs = range(1, int(self.loop_count) + 1)
        i = 0
        pairs_dict_keys = []
        while i < len(pair_legs):
            lead_p = str(pair_legs[i])
            first_key = lead_p + 'a'
            second_key = lead_p + 'b'
            pairs_dict_keys.append(first_key)
            pairs_dict_keys.append(second_key)
            i += 1
        j = 0
        while j < len(self.p_values_out):
            self.columns.update({pairs_dict_keys[j]: self.p_values_out[j]})
            j += 1
        return self.columns

    def accuracy_percentage(self):
        self.separator()
        i = 0
        while i < len(self.p_values_out):
            first_numerator = self.p_values_out[i][29]
            second_numerator = self.p_values_out[i][33]
            percentage = round(abs((first_numerator - second_numerator) / first_numerator) * 100, 2)
            self.p_values_out[i].append("%")
            self.p_values_out[i].append(percentage)
            i += 1
        return self.p_values_out

    def begining_time(self, some_string):
        l_char = some_string[-2:]
        num_char = int(l_char)
        new_char = num_char + 1
        if num_char == 60:
            num_char = int(some_string[-4])
            new_char = num_char + 1
            new_string = f"{some_string[0:-4]}{new_char}:01"
        elif num_char == 59:
            num_char = int(some_string[-4])
            new_char = num_char + 1
            new_string = f"{some_string[0:-4]}{new_char}:00"
        elif len(str(new_char)) < 2:
            new_string = f"{some_string[0:-1]}{str(new_char)}"
        else:
            new_string = f"{some_string[0:-2]}{str(new_char)}"
        return new_string

    def ending_time(self, some_string):
        l_char = some_string[-2::]
        num_char = int(l_char)
        new_char = num_char - 1
        if num_char == 0:
            num_char = int(some_string[-4])
            new_char = num_char - 1
            new_string = f"{some_string[0:-4]}{new_char}:59"
        elif num_char == 1:
            new_string = f"{some_string[0:-3]}{new_char}:00"
        elif len(str(new_char)) < 2:
            new_string = f"{some_string[0:-1]}{str(new_char)}"
        else:
            new_string = f"{some_string[0:-2]}{str(new_char)}"
        return new_string

    def corrected_time_s(self, weather_list):
        self.separator()
        i = 0
        new = []
        while i < len(self.pair_stamp_a):
            if self.pair_stamp_a[i] in weather_list:
                new.append(self.pair_stamp_a[i])
                i += 1
            else:
                if i % 2 == 0:
                    new.append(self.begining_time(self.pair_stamp_a[i]))
                    i += 1
                else:
                    new.append(self.ending_time(self.pair_stamp_a[i]))
                    i += 1

        self.pair_stamp_a.clear()
        self.single_stamp(new)

    def corrected_time_m(self, weather_list):
        self.separator()
        i = 0
        while i < len(self.pair_stamp_a):
            if self.pair_stamp_a[i] in weather_list:
                self.c_leg_a.append(self.pair_stamp_a[i])
                i += 1
            else:
                if i % 2 == 0:
                    self.c_leg_a.append(self.begining_time(self.pair_stamp_a[i]))
                    i += 1
                else:
                    self.c_leg_a.append(self.ending_time(self.pair_stamp_a[i]))
                    i += 1
        i = 0
        while i < len(self.pair_stamp_b):
            if self.pair_stamp_a[i] in weather_list:
                self.c_leg_b.append(self.pair_stamp_b[i])
                i += 1
            else:
                if i % 2 == 0:
                    self.c_leg_b.append(self.begining_time(self.pair_stamp_b[i]))
                    i += 1
                else:
                    self.c_leg_b.append(self.ending_time(self.pair_stamp_b[i]))
                    i += 1

    def second_loop(self, weather_list, test_type):
        if test_type == "y":
            self.corrected_time_m(weather_list)
            self.pair_stamp_a.clear()
            self.pair_stamp_b.clear()
            self.pair_stamp_a = [item for item in self.c_leg_a]
            self.pair_stamp_b = [item for item in self.c_leg_b]
            self.c_leg_a.clear()
            self.c_leg_b.clear()
            self.corrected_time_m(weather_list)
            self.pair_stamp_a.clear()
            self.pair_stamp_b.clear()
            self.c_leg_a.extend(self.c_leg_b)
            self.c_leg_a.sort()
            self.multiple_stamps(self.c_leg_a)
        elif test_type == "n":
            self.corrected_time_s(weather_list)
            self.pair_stamp_a.clear()
            self.pair_stamp_a = [item for item in self.c_leg_a]
            self.c_leg_a.clear()
            self.corrected_time_s(weather_list)
            self.pair_stamp_a.clear()
            self.c_leg_a.sort()
            self.single_stamp(self.c_leg_a)
