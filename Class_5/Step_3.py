#####
# Step 3 - Executing multiple tools - and automating most of it
#####

# We will use the exact same approach to generate a heatmap from a CSV file, but this time
# You will have to automate the extraction of start extent, opposite corner etc for the fishnet
# generation. I have given hints, but everything you are using here has been shown in last week's
# and this week's session.

# Using Step_3_Cepphus_grylle.csv:

# 1. Convert Step_3_Cepphus_grylle.csv to a shapefile.

# import arcpy and create your workspace
import arcpy
arcpy.env.workspace = r'C:\NRS 528\NRS_528_Python\pythonProject\Class_5'
arcpy.env.overwriteOutput = True

# name values in the environment workspace
in_Table = r'Step_3_Cepphus_grylle.csv'
x_coords = 'lon'
y_coords = 'lat'
z_coords = ''
out_Layer = 'Cepphus_grylle'
saved_Layer = r'Step_3_Cepphus_Grylle_Output.shp'
# set the spatial reference
spRef = arcpy.SpatialReference(4326)
lyr = arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef, z_coords,)

# Save to a layer file
arcpy.CopyFeatures_management(lyr, saved_Layer)

if arcpy.Exists(saved_Layer): # arcpy.Exists makes sure the file created from analysis exists
    print("Created file successfully!")

# # 2. Extract the Extent, i.e. XMin, XMax, YMin, YMax of the generated Cepphus_grylle shapefile.
desc = arcpy.Describe(lyr)

XMin = desc.extent.XMin
YMin = desc.extent.YMin
XMax = desc.extent.XMax
YMax = desc.extent.YMax

print(desc)
print('XMin: ' + str(XMin))
print('XMax: ' + str(XMax))
print('YMin: ' + str(YMin))
print('YMax:' + str(YMax))

# 3. Generate a fishnet, but this time define the originCoordinate, yAxisCoordinate and oppositeCorner
# using the extracted extent from above. Hint: Formatting of the coordinate is important when generating
# the Fishnet, you must present it as: "-176.87 -41", note the space inbetween, and the fact that the
# entire thing is a string. Hint use: cellSizes of 0.25 degrees.

outFeatureClass = 'Step_3_Fishnet.shp'
# define XMin YMin XMax YMax



# Set the origin of the fishnet
# origin coordinate should have XMin, YMin
originCoordinate = str(XMin) + ' ' + str(YMin)
# Left bottom of our point data # first value is longitude (x)
# second value is latitude (y)
yAxisCoordinate = str(XMin) + ' ' + str(YMin + 1)  # This sets the orientation on the y-axis, so we head north
cellSizeWidth = '0.25'  # 0.25 degrees
cellSizeHeight = '0.25'
numRows = ""  # Leave blank, as we have set cellSize
numColumns = ""  # Leave blank, as we have set cellSize
oppositeCorner = str(XMax) + ' ' + str(YMax)  # i.e. max x and max y coordinate
labels = "NO_LABELS"
templateExtent = "#"  # No need to use, as we have set yAxisCoordinate and oppositeCorner
geometryType = "POLYGON"  # Create a polygon, could be POLYLINE

arcpy.CreateFishnet_management(outFeatureClass, originCoordinate, yAxisCoordinate,
                               cellSizeWidth, cellSizeHeight, numRows, numColumns,
                               oppositeCorner, labels, templateExtent, geometryType)

# 4. Undertake a Spatial Join to join the fishnet to the observed points.

target_features = "Step_3_Fishnet.shp"
join_features = "Step_3_Cepphus_grylle_Output.shp"
out_feature_class = "Step_3_Cepphus_grylle_HeatMap.shp"
join_operation = "JOIN_ONE_TO_ONE"
join_type = "KEEP_ALL" # this will keep all the polygons even if there is no deep coral point inside it
field_mapping = ""
match_option = "INTERSECT"
search_radius = ""
distance_field_name = ""

arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class,
                           join_operation, join_type, field_mapping, match_option,
                           search_radius, distance_field_name)
# you don't need a copy features management tool because this tool saves the file to your hard drive

# 5. Check that the heatmap is created and delete the intermediate files (e.g. species shapefile and fishnet). Hint:
# arcpy.Delete_management()..

in_data1 = outFeatureClass
in_data2 = 'Step_3_Cepphus_Grylle_Output.shp'
in_data3 = 'Step_3_Cepphus_grylle_HeatMap.shp'
arcpy.Delete_management(in_data1)
arcpy.Delete_management(in_data2)
arcpy.Delete_management(in_data3)

# 6. Visualize in ArcGIS Pro

# # Hint: To stop your script failing due to unable to overwriteOutput error, use the overwriteOutput environment setting:
# import arcpy
# arcpy.env.overwriteOutput = True  # If you get "already exists error" even when True, ensure file is not open in
# # ArcGIS Pro or an other program such as Excel.

