# Midterm Tool Challenge
# In this assignment, you are instructed to produce a small script tool that takes advantage of arcpy and Python.
# You will need to provide example data, and the code should run on all PC's.
# The tool needs to manipulate a dataset across three different processes,
# for example, extracting, modifying and exporting data. The exact workflow is entirely up to yourself.
# You are expected to take 3-4 hours on this coding assignment, and you should deposit your code and example files
# within a Github repository for feedback and grading.
#
# The criteria are:
#
# Cleanliness of code (10 points)
# Functionality (10 points)
# Appropriate use of documentation (10 points)
# Depth of processing operation (10 points)
# In addition, you must provide example data and minimize the amount of editing a user must make
# in order for the program to run (10 points).

# convert csv file to shapefile

import arcpy

arcpy.env.workspace = r'C:\NRS 528\NRS_528_Python\Midterm_Coding_Challenge'
arcpy.env.overwriteOutput = True

# name values in the environment workspace

in_Table = r'Colleges_and_Universities_in_RI_CSV.csv'
x_coords = 'x'
y_coords = 'y'
z_coords = ''
out_Layer = 'Colleges_and_Universities'
saved_Layer = r'Colleges_and_Universities_in_RI.shp'

# set the spatial reference
spRef = arcpy.SpatialReference(4326) # 4326 = WGS 1984
lyr = arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef, z_coords,)

# print the count of the number of records in file
print(arcpy.GetCount_management(lyr))

# check correct coordinate system has been applied
desc = arcpy.Describe(lyr)
print(desc)
print(desc.spatialReference.name)

# save to a layer file
arcpy.CopyFeatures_management(lyr, saved_Layer)

if arcpy.Exists(saved_Layer):
    print("Created " + saved_Layer + " successfully!")

# visualize the file by dragging the shapfile into ArcGIS Pro
# NOTE: file was created successfully

# apply Buffer tool to Colleges_and_Universities_in_RI_CSV

import os

# set base path to limit changes made between each user
base_path = r'C:\NRS 528\NRS_528_Python\Midterm_Coding_Challenge'

# name features for erase analysis
in_features = os.path.join(base_path, 'Colleges_and_Universities_in_RI.shp')
erase_features = os.path.join(base_path, 'Providence_Boundary.shp')
out_feature_class = os.path.join(base_path, 'Colleges_and_Universities_in_RI_Erase.shp')
arcpy.Erase_analysis(in_features, erase_features, out_feature_class)


# name features for buffer analysis
input_features = os.path.join(base_path, 'Colleges_and_Universities_in_RI_Erase.shp')
output_features = os.path.join(base_path, 'Colleges_and_Universities_in_RI_Buffer.shp')
buffer_distance = "1000 meter"
line_side = "FULL"
line_end_type = "ROUND"
dissolve_option = "#"
dissolve_field = "#"
method = "GEODESIC"
arcpy.Buffer_analysis(input_features, output_features, buffer_distance, line_side, line_end_type, dissolve_option, dissolve_field, method)

# Print to make sure buffer file exists
if arcpy.Exists(output_features):
    print("Created Colleges_and_Universities_in_RI_Buffer successfully!")

