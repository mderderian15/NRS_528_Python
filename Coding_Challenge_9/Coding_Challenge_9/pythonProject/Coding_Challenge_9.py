# In this coding challenge,
# your objective is to utilize the arcpy.da module to undertake some basic partitioning of your dataset.
# In this coding challenge, I want you to work with the Forest Health Works dataset from RI GIS
# (I have provided this as a downloadable ZIP file in this repository).
#
# Using the arcpy.da module (yes, there are other ways and better tools to do this),
# I want you to extract all sites that have a photo of the invasive species (Field: PHOTO) into a new Shapefile,
# and do some basic counts of the dataset. In summary, please addressing the following:
#
# Count how many individual records have photos, and how many do not (2 numbers), print the results.
#
# Count how many unique species there are in the dataset, print the result.
#
# Generate two shapefiles, one with photos and the other without.

###Count how many individual records have photos, and how many do not (2 numbers), print the results.

# Step 1 import arcpy

import arcpy
import os

# Set base path

base_path = r'C:\NRS 528\NRS_528_Python\Coding_Challenge_9\RIGIS_Website_Forest_Data'

# Step 2 Declare input shapefile
in_shape = os.path.join(base_path, 'RI_Forest_Health_Works_Project__Points.shp')

# Step 3 Declare fields
field_names = 'photo'
field_value = 'y'

# Step 4 create expression
whereClause = """{} = '{}'""".format(arcpy.AddFieldDelimiters(in_shape, field_names),field_value)

count = 0
with arcpy.da.SearchCursor(in_shape, field_names, whereClause) as rows:
    for row in rows:
        count += 1


print(count)
no_photos = 3188 - count
print(no_photos)

###Count how many unique species there are in the dataset, print the result.

tree_list = []

with arcpy.da.SearchCursor(os.path.join(base_path, 'RI_Forest_Health_Works_Project__Points.shp'), ['Species']) as cursor:
    for row in cursor:
        if row[0] not in tree_list:
            tree_list.append(row[0])

print(len(tree_list))

# Generate two shapefiles, one with photos and the other without.

arcpy.env.workspace = base_path
arcpy.env.overwriteOutput = True

# Shapefile with photos
in_features = 'RI_Forest_Health_Works_Project__Points.shp'
out_feature_class = (os.path.join(base_path, 'RI_Forest_Select_Photos.shp'))
where_clause = '"photo" = \'y\''

arcpy.Select_analysis(in_features, out_feature_class, where_clause)

# Shapefile without photos
in_features2 = 'RI_Forest_Health_Works_Project__Points.shp'
out_feature_class2 = (os.path.join(base_path, 'RI_Forest_Select_NO_Photos.shp'))
where_clause2 = '"photo" = \'\''

arcpy.Select_analysis(in_features2, out_feature_class2, where_clause2)

