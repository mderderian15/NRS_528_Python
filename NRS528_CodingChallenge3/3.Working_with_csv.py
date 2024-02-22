# Using the Atmospheric Carbon Dioxide Dry Air Mole Fractions from quasi-continuous daily measurements
# at Mauna Loa, Hawaii dataset, obtained from here (https://github.com/datasets/co2-ppm-daily/tree/master/data).
#
# Using Python (csv) calculate the following:
#
# Annual average for each year in the dataset.
# Minimum, maximum and average for the entire dataset.
# Seasonal average if Spring (March, April, May), Summer (June, July, August), Autumn (September, October, November)
# and Winter (December, January, February).
#extract mopnth -- month = row[0].split('-')[1]

# Calculate the anomaly for each value in the dataset relative to the mean for the entire time series.

# import csv file
import csv

date_list, value_list = [], []

# Establish date list
with open("co2_ppm_daily.csv") as co2_csv:
    next(co2_csv)
    for row in csv.reader(co2_csv):
        year = row[0].split('-')[0]
        if year not in date_list:
            date_list.append(year)


average_co2_per_year_dict = {}
for year in date_list:
    with open("co2_ppm_daily.csv") as co2_csv:

        average_co2_per_year = []

        next(co2_csv)
        for row in csv.reader(co2_csv):
            if row[0].split('-')[0] == year:
                average_co2_per_year.append(float(row[1]))

        average_co2_per_year_dict[year] = sum(average_co2_per_year) / len(average_co2_per_year)

print(average_co2_per_year_dict)

# Min, max, mean
dataset_values = []

with open("co2_ppm_daily.csv") as co2_csv:
    next(co2_csv)
    for row in csv.reader(co2_csv):
        dataset_values.append(float(row[1]))

dataset_min = min(dataset_values)
dataset_max = max(dataset_values)
dataset_mean = sum(dataset_values) / len(dataset_values)

print(dataset_min)
print(dataset_max)
print(dataset_mean)

# calculate the average CO2 value for every year in the dataset
#
# average_co2_per_year = 0
# average_co2_per_year_dict = {}
#
# for d in date_list:
#     with open("co2_ppm_daily.csv") as co2_csv:
#         for row in csv.reader(co2_csv):
#             if row[0] == d:
#                 average_co2_per_year += int(float(row[1]))
#
#     average_co2_per_year_dict[d] = average_co2_per_year
#     average_co2_per_year = 0
#
# print(average_co2_per_year_dict)
#
#
#
#
#
#
#
#
#
