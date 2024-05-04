# Final Toolbox Challenge
# In your final assignment for this course, you should create a Python Toolbox that contains a minimum of
# three simple tools for undertaking geoprocessing and file management operations.
# These tools can be discrete or part of a larger workflow.
# However, the caveats are that you should create a "single file" toolbox (no includes, or external file tools)
# and you should aim to not exceed 2000 lines of code in its entirety (but if you do, no worries).
# You should document the toolbox using GitHub README.md and provide example data for running each of your tools.
# Grading and feedback will focus on: 1) Does the toolbox install, and the tools run successfully?
# 2) cleanliness of code, 3) functionality and depth of processing operation, and 4) appropriate use of documentation.
# Plus, 5) provide example data that allows me to test your tools.
#
# The criteria are:
#
# Does the toolbox install and run? (25 points)
# Cleanliness of code (25 points)
# Functionality and depth of processing (25 points)
# Appropriate use of documentation (15 points)
# In addition, you must provide example data (10 points).

# Import arcpy
import arcpy


# Define your toolbox
class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Conservation Lands in Providence Toolbox"
        self.alias = ""

        # List of tool classes associated with this toolbox
        self.tools = [FinalClip, FinalSelect, FinalBuffer]


# Define the Select tool
class FinalSelect(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Select Providence Tool" # Describe what the tool is doing
        self.description = ""
        self.canRunInBackground = False

    # Define parameters of tool
    def getParameterInfo(self):
        """Define parameter definitions"""
        select_params = []
        select_polygon = arcpy.Parameter(name="select_polygon",
                                         displayName="Select Input Polygon",
                                         datatype="DEFeatureClass",
                                         parameterType="Required",  # Required|Optional|Derived
                                         direction="Input",  # Input|Output
                                         )
        # Polygon value is the shapefile you want to select from
        select_polygon.value = (r"C:\NRS 528\NRS_528_Python\Final_Toolbox_Assignment\Municipalities "
                                r"Data\Municipalities_(1997).shp")
        select_params.append(select_polygon)
        select_output = arcpy.Parameter(name="select_output",
                                        displayName="Select Output",
                                        datatype="DEFeatureClass",
                                        parameterType="Required",  # Required|Optional|Derived
                                        direction="Output",  # Input|Output
                                        )
        # Select output is the selection you want to make
        select_output.value = (r"C:\NRS 528\NRS_528_Python\Final_Toolbox_Assignment\Municipalities "
                               r"Data\Municipalities_(1997)_Select_Prov.shp")
        select_params.append(select_output)
        return select_params

    def isLicensed(self):
        """Set whether tool is licensed to execute"""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal validation is performed.
        This method is called whenever a parameter has been changed"""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool parameter.
        This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        def describe_shp(select_polygon):
            if arcpy.Exists(select_polygon):
                desc = arcpy.Describe(select_polygon)
                print("Describing: " + str(select_polygon))
                if desc.shapeType == "Polygon":
                    print("Shape Type: " + desc.shapeType)

                else:
                    print("Shape type is not Polygon")
            else:
                print("Data not found, please check file path")
            describe_shp(select_polygon)
        """The source code of the tool."""
        select_polygon = parameters[0].valueAsText
        select_output = parameters[1].valueAsText

        # Create the Select analysis
        arcpy.Select_analysis(in_features=select_polygon,
                              out_feature_class=select_output,
                              where_clause='"NAME" = \'PROVIDENCE\'')
        return


# Define the Buffer tool
class FinalBuffer(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Conservation Land Buffer Tool" # Describe what the tool is doing
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        buffer_params = []
        buffer_input_polygon = arcpy.Parameter(name="buffer_input_polygon",
                                               displayName="Buffer Input Polygon",
                                               datatype="DEFeatureClass",
                                               parameterType="Required",  # Required|Optional|Derived
                                               direction="Input",  # Input|Output
                                               )
        buffer_input_polygon.value = (r"C:\NRS 528\NRS_528_Python\Final_Toolbox_Assignment\Conservation "
                                      r"Lands Data\ENV_Conservation_Lands_Local_spf.shp")
        buffer_params.append(buffer_input_polygon)
        buffer_output = arcpy.Parameter(name="buffer_output",
                                        displayName="Buffer Output",
                                        datatype="DEFeatureClass",
                                        parameterType="Required",  # Required|Optional|Derived
                                        direction="Output",  # Input|Output
                                        )
        buffer_output.value = (r"C:\NRS 528\NRS_528_Python\Final_Toolbox_Assignment\Conservation Lands "
                               r"Data\ENV_Conservation_Lands_Local_spf_Buffer.shp")
        buffer_params.append(buffer_output)
        buffer_distance = arcpy.Parameter(name='buffer_distance',
                                          displayName='Buffer Distance',
                                          datatype='GPLinearUnit',
                                          parameterType='Required',
                                          direction='Input')
        buffer_distance.parameterDependencies = [buffer_input_polygon.name]
        buffer_method = arcpy.Parameter(name='buffer_method',
                                        displayName='Method',
                                        datatype='GPString',
                                        parameterType='Optional',
                                        direction='Input')
        buffer_method.filter.type = "Value List"
        buffer_method.filter.list = ["PLANAR", "GEODESIC"]
        buffer_method.parameterDependencies = [buffer_input_polygon.name]
        return buffer_params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal validation is performed.
        This method is called whenever a parameter has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool parameter.
        This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        def describe_shp(buffer_input_polygon):
            if arcpy.Exists(buffer_input_polygon):
                desc = arcpy.Describe(buffer_input_polygon)
                print("Describing: " + str(buffer_input_polygon))
                if desc.shapeType == "Line":
                    print("Shape Type: " + desc.shapeType)

                else:
                    print("Shape type is not Line")
            else:
                print("Data not found, please check file path")
            describe_shp(buffer_input_polygon)
        """The source code of the tool"""
        buffer_input_polygon = parameters[0].valueAsText
        buffer_output = parameters[1].valueAsText
        buffer_distance = parameters[2].valueAsText
        buffer_method = parameters[3].valueAsText

        arcpy.Buffer_analysis(in_features=buffer_input_polygon,
                              out_feature_class=buffer_output,
                              buffer_distance_or_field=buffer_distance,
                              method=buffer_method)
        return


# Define the Clip tool
class FinalClip(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Clip Conservation Land to Providence Tool" # Describe what the tool is doing
        self.description = ""
        self.canRunInBackground = False

    def getParametersInfo(self):
        """Define parameter definitions"""
        clip_params = []
        # Clip input polygon is the polygon you want to clip
        clip_input_polygon = arcpy.Parameter(name="clip_input_polygon",
                                     displayName="Clip Input Polygon",
                                     datatype="DEFeatureClass",
                                     parameterType="Required",  # Required|Optional|Derived
                                     direction="Input",  # Input|Output
                                     )
        clip_input_polygon.value = (r"C:\NRS 528\NRS_528_Python\Final_Toolbox_Assignment\Conservation Lands "
                                    r"Data\ENV_Conservation_Lands_Local_spf_Buffer.shp")
        clip_params.append(clip_input_polygon)
        clipping_polygon = arcpy.Parameter(name='clipping_polygon',
                                           displayName='Clipping Polygon',
                                           datatype='DEFeatureClass',
                                           parameterType='Required',
                                           direction='Input')
        # Clipping polygon is the polygon you want the input clipped to
        clipping_polygon.value = (r"C:\NRS 528\NRS_528_Python\Final_Toolbox_Assignment\Municipalities "
                                  r"Data\Municipalities_(1997)_Select_Prov.shp")
        clip_params.append(clipping_polygon)
        clip_output = arcpy.Parameter(name='clip_output',
                                      displayName='Clip Output',
                                      datatype='DEFeatureClass',
                                      parameterType='Required',
                                      direction='Output')
        # Clip output is the input polygon (Conservation Lands) clipped to the Providence boundary
        clip_output.value = (r"C:\NRS 528\NRS_528_Python\Final_Toolbox_Assignment\Conservation Lands "
                             r"Data\ENV_Conservation_Lands_Clip.shp")
        clip_params.append(clip_output)
        return clip_params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        def describe_spref(clipping_polygon):
            if arcpy.Exists(clipping_polygon):
                desc = arcpy.Describe(clipping_polygon)
                print("Describing: " + str(clipping_polygon))
                if desc.spatialReference == "WGS 84":
                    print("Spatial Reference: " + desc.spatialReference)

                else:
                    print("Spatial Reference is not WGS 84")

            else:
                print("Data not found, please check file path")

            describe_spref(clipping_polygon)
        """The source code of the tool"""
        clip_input_polygon = parameters[0].valueAsText
        clipping_polygon = parameters[1].valueAsText
        clip_output = parameters[2].valueAsText

        # Create the clip analysis
        arcpy.Clip_analysis(in_features=clip_input_polygon,
                            clip_features=clipping_polygon,
                            out_feature_class=clip_output,
                            cluster_tolerance="")
        return
