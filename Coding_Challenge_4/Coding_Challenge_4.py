# using erase analysis in arcpy to erase natural heritage areas from the town of N. Kingstown

# import arcpy and operating system
import arcpy
import os

base_path = r'C:\NRS 528'

# name features that are required to run erase analysis in ArcGIS Pro
in_features = os.path.join(base_path, 'BIO_Natural_Heritage_Areas_2023.shp')
erase_features = os.path.join(base_path, 'North_Kingstown_Boundary.shp')
out_feature_class = os.path.join(base_path, 'BIO_Natural_Heritage_Areas_2023_Erase.shp')

# coding the erase command
# putting the features names in the exact order I would put them in on ArcGIS Pro
arcpy.Erase_analysis(in_features, erase_features, out_feature_class)

# in_features is the shape file that we want to erase part of
# erase_features is the shape file we are erasing the input features from
# out_feature_class is the name of the new shape file that is created after the analysis is completed
