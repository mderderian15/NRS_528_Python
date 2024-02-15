# Using the Atmospheric Carbon Dioxide Dry Air Mole Fractions from quasi-continuous daily measurements
# at Mauna Loa, Hawaii dataset, obtained from here (https://github.com/datasets/co2-ppm-daily/tree/master/data).
#
# Using Python (csv) calculate the following:
#
# Annual average for each year in the dataset.
# Minimum, maximum and average for the entire dataset.
# Seasonal average if Spring (March, April, May), Summer (June, July, August), Autumn (September, October, November)
# and Winter (December, January, February).
# Calculate the anomaly for each value in the dataset relative to the mean for the entire time series.

# import csv file
import csv

date_list, value_list = [], []

# calculate the average CO2 value for every year in the dataset

average_co2_per_year = 0
average_co2_per_year_dict = {}

for d in date_list:
    with open("co2_ppm_daily.csv") as co2_csv:
        for row in csv.reader(co2_csv):
            if row[0] == d:
                average_co2_per_year += int(float(row[1]))

    average_co2_per_year_dict[d] = average_co2_per_year
    average_co2_per_year = 0

print(average_co2_per_year_dict)









