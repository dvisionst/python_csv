TIME_CONSTANT = 7


class UtcTime:

    def __init__(self):
        self.con_az_time = []
        self.round_t = []
        self.string_t = []
        self.az_times = []

    def utc_type_conv(self, vbox_list):

        for value in vbox_list:
            self.round_t.append(round(value))
        for num_time in self.round_t:
            self.string_t.append(str(num_time))

    def az_time_list(self):
        i = 0
        while i < len(self.string_t):
            if len(self.string_t[i]) > 5:
                hour = str(self.string_t[i][0:2])
                conv_hour = int(hour) - TIME_CONSTANT
                new_az = str(conv_hour) + self.string_t[i][2::]
                self.az_times.append(new_az)

            else:
                e_hour = str(self.string_t[i][0:1])
                if int(e_hour) < 7:
                    conv_hour_e = int(e_hour) + 17
                    new_az_e = str(conv_hour_e) + self.string_t[i][1::]
                    self.az_times.append(new_az_e)
                elif int(e_hour) >= 7:
                    conv_hour_e = int(e_hour) - TIME_CONSTANT
                    new_az_e = str(conv_hour_e) + self.string_t[i][1::]
                    self.az_times.append(new_az_e)
            i += 1


















