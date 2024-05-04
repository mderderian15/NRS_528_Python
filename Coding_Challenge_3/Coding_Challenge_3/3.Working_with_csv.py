# Using the Atmospheric Carbon Dioxide Dry Air Mole Fractions from quasi-continuous daily measurements
# at Mauna Loa, Hawaii dataset, obtained from here (https://github.com/datasets/co2-ppm-daily/tree/master/data).
#
# Using Python (csv) calculate the following:
#
# Annual average for each year in the dataset.
# Minimum, maximum and average for the entire dataset.
# Seasonal average of Spring (March, April, May), Summer (June, July, August), Autumn (September, October, November)
# and Winter (December, January, February).
# Calculate the anomaly for each value in the dataset relative to the mean for the entire time series.

# import csv file
import csv

# Create lists for annual average for each year in the dataset.
date_list, value_list = [], []

# Establish date list
with open("co2_ppm_daily.csv") as co2_csv:
    next(co2_csv)
    for row in csv.reader(co2_csv):
        year = row[0].split('-')[0]
        if year not in date_list:
            date_list.append(year)

print(date_list)

# Create dictionary for average CO2
average_co2_per_year_dict = {}

# Open CSV file 
for year in date_list: # For every year in the date list
    with open("co2_ppm_daily.csv") as co2_csv:

        average_co2_per_year = []

        next(co2_csv)
        for row in csv.reader(co2_csv):
            if row[0].split('-')[0] == year:
                average_co2_per_year.append(float(row[1]))

        average_co2_per_year_dict[year] = sum(average_co2_per_year) / len(average_co2_per_year)

print(average_co2_per_year_dict)

# Minimum, maximum and average for the entire dataset.

dataset_values = []

with open("co2_ppm_daily.csv") as co2_csv:
    next(co2_csv)
    for row in csv.reader(co2_csv):
        dataset_values.append(float(row[1]))

# Find minimum, maximum, and averages of the dataset
dataset_min = min(dataset_values)
dataset_max = max(dataset_values)
dataset_mean = sum(dataset_values) / len(dataset_values)

print("Minimum: " + str(dataset_min))
print("Maximum: " + str(dataset_max))
print("Mean: " + str(dataset_mean))

# Seasonal average of Spring (March, April, May), Summer (June, July, August), Autumn (September, October, November)
# and Winter (December, January, February).

# extract month: month = row[0].split('-')[1]

# Create empty seasonal lists
spring_list = []
summer_list = []
autumn_list = []
winter_list = []

with open("co2_ppm_daily.csv") as co2_csv:
    next(co2_csv)
    for row in csv.reader(co2_csv):
        month = row[0].split('-')[1] # Split the date by the hyphens in the CSV file...The month is the second number split by the hyphens

        if month in ['03', '04', '05']: # If date contains 03 04 or 05 for month append it to the spring list
            spring_list.append(float(row[1]))

        if month in ['06', '07', '08']: # If date contains 06 07 or 08 for month append it to the summer list
            summer_list.append(float(row[1]))

        if month in ['09', '10', '11']: # If date contains 09 10 or 11 for months append it to the fall list
            autumn_list.append(float(row[1]))

        if month in ['12', '01', '02']: # If date contains 12 01 or 02 for month append it to the winter list
            winter_list.append(float(row[1]))


# Calclulate averages for each season
spring_average = sum(spring_list) / len(spring_list)
summer_average = sum(summer_list) / len(summer_list)
autumn_average = sum(autumn_list) / len(autumn_list)
winter_average = sum(winter_list) / len(winter_list)
#
# Print averages for each season
print(spring_average)
print(summer_average)
print(autumn_average)
print(winter_average)

# Calculate the anomaly for each value in the dataset relative to the mean for the entire time series.
# anomaly is the average of the entire dataset for each individual observation and subtract the average and index 0

anomaly = 0
with open("co2_ppm_daily.csv") as co2_csv:
    next(co2_csv)
    for row in csv.reader(co2_csv):
        anomaly = float(row[1]) - float(dataset_mean)
        print("The anomaly for " + row[0] + " is " + str(anomaly) + ".")
