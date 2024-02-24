#####
# Step 1 - Executing and reporting tool outputs
#####

# Part a - convert CSV to shapefile

# Help on Tool: http://desktop.arcgis.com/en/arcmap/10.3/tools/data-management-toolbox/make-xy-event-layer.htm.
# Using the data Step_1_Lionfish.csv, we will use arcpy to convert this to a shapefile.

# import arcpy
# # Set your workspace to the directory where you are storing your files
# arcpy.env.workspace = r"C:\NRS 528\NRS_528_Python\pythonProject\Class_5"
# arcpy.env.overwriteOutput = True
# in_Table = r"Step_1_Lionfish.csv"
# x_coords = "X"
# y_coords = "Y"
# z_coords = ""
# out_Layer = "lionfish" # in memory file. Not added to hard drive
# saved_Layer = r"Step_1_Lionfish_Output.shp"
# # everything up to this point is just naming values in the workspace, so we can perform the analysis
# # Set the spatial reference
# spRef = arcpy.SpatialReference(4326)  # 4326 == WGS 1984
# # actual analysis performed when naming lyr
# lyr = arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef, z_coords)
#
# # Print the total rows
# print(arcpy.GetCount_management(lyr)) # tells you how many rows in your dataset
#
# # Save to a layer file
# arcpy.CopyFeatures_management(lyr, saved_Layer)
#
# if arcpy.Exists(saved_Layer): # arcpy.Exists makes sure the file created from analysis exists
#     print("Created file successfully!")


# Tasks - Using the file provided "Step_1_Deep_Coral.csv", undertake the following: Hint: spatial
# reference is the same as above, i.e. WGS 1984.

##### 1. Convert the file to a shapefile.

import arcpy
arcpy.env.workspace = r'C:\NRS 528\NRS_528_Python\pythonProject\Class_5'
arcpy.env.overwriteOutput = True
# name values in the environment workspace
in_Table = r'Step_1_Deep_Coral.csv'
x_coords = 'decimalLongitude'
y_coords = 'decimalLatitude'
z_coords = ''
out_Layer = 'DeepCoral'
saved_Layer = r'Step_1_Deep_Coral_Output.shp'
# set the spatial reference
spRef = arcpy.SpatialReference(4326)
lyr = arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef, z_coords,)

##### 2. Print the count of the number of records in the file. (Hint: see above!)
# https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/get-count.htm

print(arcpy.GetCount_management(lyr))

##### 3. Check the correct coordinate system has been applied (Hint: see last week!)

desc = arcpy.Describe(lyr)
print(desc)
print(desc.spatialReference.name)

# Save to a layer file
arcpy.CopyFeatures_management(lyr, saved_Layer)

if arcpy.Exists(saved_Layer): # arcpy.Exists makes sure the file created from analysis exists
    print("Created file successfully!")
##### 4. Visualize the file in ArcPro by dragging it into the program.

