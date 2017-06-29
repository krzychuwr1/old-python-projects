import configparser


class Settings:

    def __init__(self, file_name):
        self.file_name = file_name
        self.__read_config()

    def __read_config(self):  # function reading config file
        try:
            config = configparser.ConfigParser()
            config.read(self.file_name)
        except Exception as e:
            raise RuntimeError("Couldn't open config.ini") from e

        try:
            self.api_key = config['OpenExchangeRates Settings']['api_key']
        except Exception as e:
            raise RuntimeError("Couldn't find api key in config.ini") from e

        """
        Get time settings from config file
        """
        try:
            self.range_start = config['Time Settings']['range_start']
            self.frequency = config['Time Settings']['frequency']
            self.range_end = config['Time Settings']['range_end']
        except Exception as e:
            raise RuntimeError("Couldn't find Time Settings in config.ini file") from e

        """
        Get currencies from config gile
        """
        try:
            currencies_string = config['Currency Data Settings']['currencies']
            self.currencies_list = [currency.strip() for currency in currencies_string.split(',')]
        except Exception as e:
            raise RuntimeError("Couldn't find Currency Data Settings in config.ini file") from e

        """
        Get the list of planets and attributes from config file
        """
        try:
            planets_string = config['Astronomy Data Settings']['planets']
            self.planets_list = [planet.strip() for planet in planets_string.split(',')]
            attributes_string = config['Astronomy Data Settings']['attributes']
            self.attributes_list = [attribute.strip() for attribute in attributes_string.split(',')]
        except Exception as e:
            raise RuntimeError("Couldn't find Astronomy Data Settings in config.ini file") from e

        """
        Get the list of output files
        """
        try:
            self.output_files_list = [file.strip() for file in config['Plot Settings']['output_files'].split(', ')]
            self.how_many_files = len(self.output_files_list)
        except Exception as e:
            raise RuntimeError("Couldn't find Plot Settings in config.ini file") from e
