"""CSC108: Fall 2022 -- Assignment 3: Hypertension and Low Income

This code is provided solely for the personal and private use of
students taking the CSC108/CSCA08 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2022 Jacqueline Smith and David Liu
"""
from typing import TextIO
import statistics  # Note that this requires Python 3.10

ID = "id"
HT_KEY = "hypertension"
TOTAL = "total"
LOW_INCOME = "low_income"

# Indexes in the inner lists of hypertension data in CityData
# HT is an abbreviation of hypertension, NBH is an abbreviation of neighbourhood
HT_20_44 = 0
NBH_20_44 = 1
HT_45_64 = 2
NBH_45_64 = 3
HT_65_UP = 4
NBH_65_UP = 5

# columns in input files
ID_COL = 0
NBH_NAME_COL = 1
POP_COL = 2
LI_POP_COL = 3

SAMPLE_DATA = {
    "West Humber-Clairville": {
        "id": 1,
        "hypertension": [703, 13291, 3741, 9663, 3959, 5176],
        "total": 33230,
        "low_income": 5950,
    },
    "Mount Olive-Silverstone-Jamestown": {
        "id": 2,
        "hypertension": [789, 12906, 3578, 8815, 2927, 3902],
        "total": 32940,
        "low_income": 9690,
    },
    "Thistletown-Beaumond Heights": {
        "id": 3,
        "hypertension": [220, 3631, 1047, 2829, 1349, 1767],
        "total": 10365,
        "low_income": 2005,
    },
    "Rexdale-Kipling": {
        "id": 4,
        "hypertension": [201, 3669, 1134, 3229, 1393, 1854],
        "total": 10540,
        "low_income": 2140,
    },
    "Elms-Old Rexdale": {
        "id": 5,
        "hypertension": [176, 3353, 1040, 2842, 948, 1322],
        "total": 9460,
        "low_income": 2315,
    },
}

SAMPLE_DATA2 = {
    "FazeTown": {
        "id": 1,
        "hypertension": [703, 13291, 3741, 9663, 3959, 5176],
        "total": 33230,
        "low_income": 5950,
    },
    "Ancient": {
        "id": 2,
        "hypertension": [789, 12906, 3578, 8815, 2927, 3902],
        "total": 33230,
        "low_income": 9690,
    },
    "Vertigo": {
        "id": 3,
        "hypertension": [220, 3631, 1047, 2829, 1349, 1767],
        "total": 10365,
        "low_income": 2005,
    },
    "Inferno": {
        "id": 4,
        "hypertension": [201, 3669, 1134, 3229, 1393, 1854],
        "total": 10540,
        "low_income": 2140,
    },
    "Mirage": {
        "id": 5,
        "hypertension": [176, 3353, 1040, 2842, 948, 1322],
        "total": 9460,
        "low_income": 2315,
    },
}


def get_hypertension_data(nbh_data: dict, text: TextIO) -> None:
    """Modify the nbh_data so that it contains the hypertension data
    in the text. If a neighbourhood with data in the text is already in the 
    nbh_data then its hypertension data should be updated.
    Otherwise it should be added to the nbh_data with its hypertension data.
    """
    
    text.readline().strip()
    line = text.readline().strip()
    while line != '':
        ht_list = line.split(',')
        nbh_name = ht_list[NBH_NAME_COL]
        for index in range(2, len(ht_list)):
            ht_list[index] = int(ht_list[index])
        if nbh_name not in nbh_data:
            nbh_data[nbh_name] = {}
            nbh_data[nbh_name][ID] = int(ht_list[ID_COL])
            nbh_data[nbh_name][HT_KEY] = ht_list[2:len(ht_list)]
        else:
            nbh_data[nbh_name][ID] = (ht_list[ID_COL])
            nbh_data[nbh_name][HT_KEY] = ht_list[2:len(ht_list)]
        line = text.readline().strip()
    
            
def get_low_income_data(nbh_data: dict, text: TextIO) -> None:
    """Modify the nbh_data so that it contains the low income data in the text.
    If a neighbourhood with data in the text is already in the nbh_data then
    its low_income_data should be updated.
    Otherwise it should be added to the nbh_data with its low_income_data.
    """

    text.readline().strip()
    line = text.readline().strip()
    while line != '':
        li_list = line.split(',')
        nbh_name = li_list[NBH_NAME_COL]
        for index in range(2, len(li_list)):
            li_list[index] = int(li_list[index])
        if nbh_name not in nbh_data:
            nbh_data[nbh_name] = {}
            nbh_data[nbh_name][ID] = int(li_list[ID_COL])
            nbh_data[nbh_name][TOTAL] = li_list[POP_COL]
            nbh_data[nbh_name][LOW_INCOME] = li_list[LI_POP_COL]
        else:
            nbh_data[nbh_name][ID] = int(li_list[ID_COL])
            nbh_data[nbh_name][TOTAL] = li_list[POP_COL]
            nbh_data[nbh_name][LOW_INCOME] = li_list[LI_POP_COL]            
        line = text.readline().strip()

            
def get_bigger_neighbourhood(data: 'CityData', nbh1: str, nbh2: str) -> str:
    """Return nbh2 if data[nbh1]['total'] is smaller than data[nbh2]['total'],
    or nbh1 not in data while nbh2 in data. Return nbh1 otherwise.

    >>> get_bigger_neighbourhood(SAMPLE_DATA, "Nowhere", "Rexdale-Kipling")
    'Rexdale-Kipling'
    >>> get_bigger_neighbourhood(SAMPLE_DATA, "Elms-Old Rexdale", "Nowhere")
    'Elms-Old Rexdale'
    """
    if nbh1 not in data and nbh2 in data:
        return nbh2
    elif nbh1 in data and nbh2 not in data or (nbh1 and nbh2) not in data:
        return nbh1
    elif data[nbh1][TOTAL] < data[nbh2][TOTAL]:
        return nbh2    
    else:
        return nbh1


def get_hypertension_rate(ht_data: list[int]) -> float:
    """Return a float that is the sum of the value on even index of ht_data
    divided by the sum of the value on odd index of ht_data
    
    Precondition: len(ht_data) = 6
    
    >>> get_hypertension_rate([703, 13291, 3741, 9663, 3959, 5176])
    0.2987202275151084
    >>> get_hypertension_rate([789, 12906, 3578, 8815, 2927, 3902])
    0.28466612028255867
    """
    numerator = 0
    denominator = 0
    for index in range(len(ht_data)):
        if index % 2 == 0:
            numerator = numerator + ht_data[index]
        else:
            denominator = denominator + ht_data[index]
    return numerator / denominator        


def get_high_hypertension_rate(data: 'CityData', 
                               threshold: float) -> list[tuple[str, float]]:
    """Return a list of tuples with each first item of tuple is the key of data
    which its ratio is greater than threshold, each second item is the ratio.
    >>> get_high_hypertension_rate(SAMPLE_DATA, 0.3)
    [('Thistletown-Beaumond Heights', 0.31797739151574084),\
 ('Rexdale-Kipling', 0.3117001828153565)]
    >>> get_high_hypertension_rate(SAMPLE_DATA, 0.25)
    [('West Humber-Clairville', 0.2987202275151084),\
 ('Mount Olive-Silverstone-Jamestown', 0.28466612028255867),\
 ('Thistletown-Beaumond Heights', 0.31797739151574084),\
 ('Rexdale-Kipling', 0.3117001828153565),\
 ('Elms-Old Rexdale', 0.2878808035120394)]
    """

    high_ht_rate_list = []
    hypertension_list = []
    for key in data:
        hypertension_list = data[key][HT_KEY]
        ratio = get_hypertension_rate(hypertension_list)
        if ratio > threshold:
            high_ht_rate_list.append((key, ratio))
    return high_ht_rate_list


def get_ht_to_low_income_ratios(data: 'CityData') -> dict[str, float]:
    """Return a dictionary that contains each neighbourhood as key, each
    corresponding value is a float which is the ratio of the hypertension rate 
    to the low income rate for that neighbourhood.
    
    >>> get_ht_to_low_income_ratios(SAMPLE_DATA)
    {'West Humber-Clairville': 1.6683148168616895,\
 'Mount Olive-Silverstone-Jamestown': 0.9676885451091314,\
 'Thistletown-Beaumond Heights': 1.6438083107534431,\
 'Rexdale-Kipling': 1.5351962275111484,\
 'Elms-Old Rexdale': 1.1763941257986577}
    >>> get_ht_to_low_income_ratios(SAMPLE_DATA2)
    {'FazeTown': 1.6683148168616895, 'Ancient': 0.9762079646015918,\
 'Vertigo': 1.6438083107534431, 'Inferno': 1.5351962275111484,\
 'Mirage': 1.1763941257986577}
    """

    ht_to_low_income_dict = {}
    hypertension_ratio = 0.0
    low_income_ratio = 0.0
    for key in data:
        hypertension_list = data[key][HT_KEY]
        hypertension_ratio = get_hypertension_rate(hypertension_list)
        low_income_ratio = data[key][LOW_INCOME] / data[key][TOTAL]
        ratio = hypertension_ratio / low_income_ratio
        ht_to_low_income_dict[key] = ratio
    return ht_to_low_income_dict


def calculate_ht_rates_by_age_group(data: 'CityData', nbh: str) -> tuple[float, 
                                                                         float, 
                                                                         float]:
    """Return a tuple consisting three float, which each float is the
    hypertension rate for each of the three age groups in the nbh
    as a percentage in data.
    >>> calculate_ht_rates_by_age_group(SAMPLE_DATA, 'Elms-Old Rexdale')
    (5.24903071875932, 36.593947923997185, 71.70953101361573)
    >>> calculate_ht_rates_by_age_group(SAMPLE_DATA, "Rexdale-Kipling")
    (5.478331970564186, 35.119231960359244, 75.13484358144552)
    """

    age_group_percentage = ()
    ht_list = data[nbh][HT_KEY]
    percent_1st = ht_list[HT_20_44] / ht_list[NBH_20_44] * 100
    percent_2nd = ht_list[HT_45_64] / ht_list[NBH_45_64] * 100
    percent_3rd = ht_list[HT_65_UP] / ht_list[NBH_65_UP] * 100
    age_group_percentage += (percent_1st, percent_2nd, percent_3rd)
    return age_group_percentage

    
# This function is provided for use in Tasks 3 and 4. You should not change it.
def get_age_standardized_ht_rate(ndata: 'CityData', name: str) -> float:
    """Return the age standardized hypertension rate from the neighbourhood in
    ndata matching the given name.

    Precondition: name is in ndata

    >>> get_age_standardized_ht_rate(SAMPLE_DATA, 'Elms-Old Rexdale')
    24.44627521389894
    >>> get_age_standardized_ht_rate(SAMPLE_DATA, 'Rexdale-Kipling')
    24.72562462246556
    """
    rates = calculate_ht_rates_by_age_group(ndata, name)

    # These rates are normalized for only 20+ ages, using the census data
    # that our datasets are based on.
    canada_20_44 = 11_199_830 / 19_735_665  # Number of 20-44 / Number of 20+
    canada_45_64 = 5_365_865 / 19_735_665  # Number of 45-64 / Number of 20+
    canada_65_plus = 3_169_970 / 19_735_665  # Number of 65+ / Number of 20+

    return (rates[0] * canada_20_44
            + rates[1] * canada_45_64
            + rates[2] * canada_65_plus)


def get_stats_summary(data: 'CityData') -> float:
    """Return a float, which is the correlation between age standardized
    hypertension rates and low income rates across all neighbourhoods.
    >>> get_stats_summary(SAMPLE_DATA)
    0.28509539188554994
    >>> get_stats_summary(SAMPLE_DATA2)
    0.27340471828293106
    """
    
    age_standardized_ht_list = []
    low_income_r_list = []
    for key in data:
        age_standardardized_ht_rate = get_age_standardized_ht_rate(data, key)
        low_income_rate = data[key][LOW_INCOME] / data[key][TOTAL]
        age_standardized_ht_list.append(age_standardardized_ht_rate)
        low_income_r_list.append(low_income_rate)
    return statistics.correlation(age_standardized_ht_list, low_income_r_list)


def order_by_ht_rate(data: 'CityData') -> list[str]:
    """Return a list of string that is names of the neighbourhoods,
    ordered from lowest to highest age-standardized hypertension rate from data.
    >>> order_by_ht_rate(SAMPLE_DATA)
    ['Elms-Old Rexdale', 'Rexdale-Kipling', 'Thistletown-Beaumond Heights',\
 'West Humber-Clairville', 'Mount Olive-Silverstone-Jamestown']
    >>> order_by_ht_rate(SAMPLE_DATA2)
    ['Mirage', 'Inferno', 'Vertigo', 'FazeTown', 'Ancient']
    """

    age_ht_dict = {}
    ordered_list = []
    for key in data:
        rate = get_age_standardized_ht_rate(data, key)
        age_ht_dict[rate] = key
    age_ht_list = sorted(age_ht_dict.items())
    for subtuple in age_ht_list:
        ordered_list.append(subtuple[1])
    return ordered_list


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # Using the small data files
    small_data = {}

    # Add hypertension data
    ht_file = open("hypertension_data_small.csv")
    get_hypertension_data(small_data, ht_file)
    ht_file.close()

    # Add low income data
    li_file = open("low_income_small.csv")
    get_low_income_data(small_data, li_file)
    li_file.close()

    # Created dictionary should be the same as SAMPLE_DATA
    print(small_data == SAMPLE_DATA)
