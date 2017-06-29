import json
import os.path
import urllib.request


class JsonData:

    def __init__(self, file_name, settings):
        self.settings = settings
        self.__get_data(file_name)

    def __get_data(self, file_name):
        json_file = os.path.join('currency_data', file_name+'.json')
        try:
            with open(json_file) as data_file:  # open json file
                self.data = json.load(data_file)  # load data from json
        except:
            print("Seems like some of the data is missing. Downloading data.")
            try:
                self.__download_file(file_name)  # in case of missing file, download it
            except:
                print("Downloading data has failed.")  # if download failed, print statement and raise exception
                raise
            try:
                with open(json_file) as data_file:
                    self.data = json.load(data_file)  # load data from json
            except:
                print("Couldn't retrieve the data.")
                raise

    def __download_file(self, date):  # function downloads data for set date using api key from settings
        try:
            url = "https://openexchangerates.org/api/historical/"+date+".json?app_id="+self.settings.api_key
            urllib.request.urlretrieve(url, os.path.join('currency_data', date+'.json'))
        except:
            raise
