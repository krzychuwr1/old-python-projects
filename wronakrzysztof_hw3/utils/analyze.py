from utils import get_json
import pandas
import ephem
import collections


# creates 2 DataFrames, one contains currency data, another astronomy Data
def create_data_frames(settings):

    #  Create planets dictionary and list of all combinations of planets and attributes
    try:
        planets_dict = {}
        astronomy_columns_list = []
        for planet in settings.planets_list:
            planets_dict[planet] = getattr(ephem, planet)()
            for attribute in settings.attributes_list:
                astronomy_columns_list.append(planet+' '+attribute)
    except Exception as e:
        raise RuntimeError("Couldn't find some of planets in pyephem. Possible error in config.ini") from e

    # Create dates index for pandas DataFrame
    try:
        dates = pandas.date_range(start=settings.range_start, end=settings.range_end, freq=settings.frequency)
        dates = dates.strftime("%Y-%m-%d")
    except Exception as e:
        raise RuntimeError("Couldn't create dates index, year format in config.ini is probably wrong.",
                           "Correct format is YYYY-MM-DD") from e

    #  Prepare empty pandas DataFrames
    currency_dataframe = pandas.DataFrame(index=dates, columns=settings.currencies_list).astype('float64')
    astronomy_dataframe = pandas.DataFrame(index=dates, columns=astronomy_columns_list).astype('float64')

    for day in dates:

        # Get data from json files
        try:
            temp_json = get_json.JsonData(day, settings)
        except Exception as e:
            raise RuntimeError("Couldn't retrieve some json files. Check internet connection, " +
                               "Date range. Also there's a monthly limit of 1000 json files download") from e

        # Add currency data to currency DataFrame
        try:
            for currency in settings.currencies_list:
                    currency_dataframe[currency][day] = temp_json.data['rates'][currency]
        except Exception as e:
            raise RuntimeError("Couldn't retrieve some currency data from json files."
                               "Check config.ini currencies. ") from e

        # Add planets attributes data to astronomy DataFrame
        try:
            for planet_name, planet_object in planets_dict.items():
                planet_object.compute(day)
                for attribute in settings.attributes_list:
                    astronomy_dataframe[planet_name+' '+attribute][day] = getattr(planet_object, attribute)
        except Exception as e:
            raise RuntimeError("Couldn't retrieve some currency data from json files.",
                               "Check config.ini currencies. ") from e

    #  Function returns a dictionary containing two result DataFrames
    return {'astronomy': astronomy_dataframe, 'currency': currency_dataframe}


#  Creates how_many DataFrames with best found correlations, and puts them in list of dictionaries.
#  A Dictionary contains also name of currency, name of planet and attribute and how big was the correlation
def get_top(currency_data, astronomy_data, how_many):
    tops = collections.deque(maxlen=how_many)
    for currency_column in list(currency_data.columns.values):  # this loop gets how_many best correlations
        for astronomy_column in list(astronomy_data.columns.values):
            correlation = currency_data[currency_column].corr(astronomy_data[astronomy_column])
            if len(tops) < how_many or abs(tops[how_many-1]['corr']) <= abs(correlation):
                tops.appendleft({'corr': correlation, 'astro': astronomy_column, 'curr': currency_column})

    tops = sorted(tops, key=lambda k: abs(k['corr']), reverse=True)  # sort result deque by correlations
    results = []
    for top in tops:  # this loop creates DataFrames with results
        d = {top['astro']: astronomy_data[top['astro']], top['curr']: currency_data[top['curr']]}
        data_frame = pandas.DataFrame(data=d, index=astronomy_data.index.tolist())
        results.append({'DataFrame': data_frame, 'curr': top['curr'], 'astro': top['astro'], 'corr': top['corr']})
    return results
