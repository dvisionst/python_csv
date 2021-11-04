import pandas as pd

pair_number = range(1, 12)
pair_letter = ('a', 'b')


class Results:

    def __init__(self):
        self.data = pd.read_csv("vbox_results_all_runs2.csv")
        self.high_index = []
        self.low_index = []
        self.good_pairs_i = []
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

    def high_run_pull(self):
        i = 0
        while i < len(self.data.Run):
            if self.data.iloc[i][self.high_dict['high'][0]] > 0:
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

    def tuple_creation_ideal(self):
        i = 0
        if len(self.high_index) == len(self.low_index):
            while i < len(self.low_index):
                norm_high = self.high_index[i]
                norm_low = self.low_index[i]
                if self.data.iloc[norm_high].Heading == self.data.iloc[norm_low].Heading:
                    self.good_pairs_i.append(norm_high)
                    self.good_pairs_i.append(norm_low)
                i += 1
            return self.good_pairs_i
        elif len(self.high_index) != len(self.low_index):
            return False

    def odd_run_fix(self):
        i = 0
        k = 1
        if len(self.high_index) % 2 != 0:
            while k < len(self.high_index):
                if self.data.iloc[self.high_index[i]].Heading != self.data.iloc[self.high_index[k]].Heading:
                    i += 1
                    k += 1
                elif self.data.iloc[self.high_index[i]].Heading == self.data.iloc[self.high_index[k]].Heading:
                    return self.high_index, k, 10

        elif len(self.low_index) % 2 != 0:
            while k < len(self.low_index):
                if self.data.iloc[self.low_index[i]].Heading != self.data.iloc[self.low_index[k]].Heading:
                    i += 1
                    k += 1
                elif self.data.iloc[self.low_index[i]].Heading == self.data.iloc[self.low_index[k]].Heading:
                    return self.low_index, k, 0
















