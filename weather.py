import pandas as pd


class Weather:

    def __init__(self):
        self.track_data = pd.read_csv("track_weather.csv")
        self.time_data = self.track_data.Time[1::]
        self.one_s_data = ""
        self.clean_track = []
        self.clean_one = []






