import pandas as pd
import cd_functions as cd
pair_number = range(1, 12)
pair_letter = ('a', 'b')

class Results:

    def __init__(self):
        self.data = pd.read_csv("vbox_results_runs.csv")
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
                '85 - 75 (s)',
                '75 - 65 (s)',
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

    def loop_index(self):
        self.loop_count = len(self.high_index)/2
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

    def top_vel_accume(self, t_type):
        i = 0

        while i < self.loop_count * 2:
            self.p_values_out[i].append(0)
            total = 0
            if t_type:
                k = 0
            else:
                k = 1
            while k < 5:

                self.high_sum = self.data.iloc[self.high_index[i]][self.high_dict["high"][k]]
                total += self.high_sum
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
            k = 5
            j = 0
            total = self.overlap_values[i]
            while k < 8:
                h_v = self.data.iloc[self.high_index[i]][self.high_dict["high"][k]]
                l_v = self.data.iloc[self.low_index[i]][self.low_dict["low"][j]]
                overlap_average = (h_v + l_v)/2
                total += overlap_average
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
            k = 3
            while k < 7:
                self.low_sum = self.data.iloc[self.low_index[i]][self.low_dict["low"][k]]
                total += self.low_sum
                self.p_values_out[i].append(total)
                k += 1
            i += 1
        return self.p_values_out

    def top_vel_single(self, test_type):
        i = 0
        while i < self.loop_count * 2:
            self.p_values_out[i].append(0)
            total = 0
            if test_type == True:
                k = 0
                stop = 13
            else:
                k = 1
                stop = 12
            while k < stop:
                self.high_sum = self.data.iloc[self.high_index[i]][self.single_dict["high"][k]]
                total += self.high_sum
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













