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

# Import operating system
import os

# Import arcpy
import arcpy

# Define base path
base_path = r"C:\NRS 528\NRS_528_Python\Final_Toolbox_Assignment"


# Define your toolbox
class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Final Toolbox"
        self.alias = ""

        # List of tool classes associated with this toolbox
        self.tools = [FinalClip, FinalSelect, FinalBuffer]


# Define your tool
class FinalSelect(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Final Select Tool"
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
        select_polygon.value = os.path.join(base_path, 'Municipalities_(1997).shp')
        params.append(select_polygon)
        select_output = arcpy.Parameter(name="select_output",
                                        displayName="Select Output",
                                        datatype="DEFeatureClass",
                                        parameterType="Required",  # Required|Optional|Derived
                                        direction="Output",  # Input|Output
                                        )
        select_output.value = os.path.join(base_path, 'Municipalities_(1997)_Select.shp')
        params.append(select_output)
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
        """The source code of the tool."""
        select_polygon = parameters[0].valueAsText
        select_output = parameters[1].valueAsText

        arcpy.Select_analysis(in_features=select_polygon,
                              out_feature_class=select_output,
                              where_clause='"NAME" = \'PROVIDENCE\'')
        return


class FinalBuffer(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Final Buffer Tool"
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
        buffer_input_polygon.value = os.path.join(base_path, 'ENV_Conservation_Lands_Local_spf.shp')
        buffer_params.append(buffer_input_polygon)
        buffer_output = arcpy.Parameter(name="buffer_output",
                                        displayName="Buffer Output",
                                        datatype="DEFeatureClass",
                                        parameterType="Required",  # Required|Optional|Derived
                                        direction="Output",  # Input|Output
                                        )
        buffer_output.value = os.path.join(base_path, 'ENV_Conservation_Lands_Local_spf_Buffer.shp')
        buffer_params.append(buffer_output)
        buffer_distance = arcpy.Parameter(name='buffer_distance',
                                          displayName='Buffer Distance',
                                          datatype='GPLinearUnit',
                                          parameterType='Required',
                                          direction='Input')
        buffer_distance.parameterDependencies = [input_polygon2.name]
        buffer_method = arcpy.Parameter(name='buffer_method',
                                        displayName='Method',
                                        datatype='GPString',
                                        parameterType='Optional',
                                        direction='Input')
        buffer_method.filter.type = "Value List"
        buffer_method.filter.list = ["PLANAR", "GEODESIC"]
        buffer_method.parameterDependencies = [input_polygon2.name]
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


class FinalClip(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Final Clip Tool"
        self.description = ""
        self.canRunInBackground = False

    def getParametersInfo(self):
        """Define parameter definitions"""
        clip_params = []
        clip_input_polygon = arcpy.Parameter(name="clip_input_polygon",
                                     displayName="Clip Input Polygon",
                                     datatype="DEFeatureClass",
                                     parameterType="Required",  # Required|Optional|Derived
                                     direction="Input",  # Input|Output
                                     )
        clip_input_polygon.value = os.path.join(base_path, 'ENV_Conservation_Lands_Local_spf_Buffer.shp')
        clip_params.append(clip_input_polygon)
        clipping_polygon = arcpy.Parameter(name='clipping_polygon',
                                           displayName='Clipping Polygon',
                                           datatype='DEFeatureClass',
                                           parameterType='Required',
                                           direction='Input')
        clipping_polygon.value = os.path.join(base_path, 'Municipalities_(1997).shp')
        clip_params.append(clipping_polygon)
        clip_output = arcpy.Parameter(name='clip_output',
                                      displayName='Clip Output',
                                      datatype='DEFeatureClass',
                                      parameterType='Required',
                                      direction='Output')
        clip_output.value = os.path.join(base_path, 'ENV_Conservation_Lands_Clip.shp')
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
        """The source code of the tool"""
        clip_input_polygon = parameters[0].valueAsText
        clipping_polygon = parameters[1].valueAsText
        clip_output = parameters[2].valueAsText

        arcpy.Clip_analysis(in_features=clip_input_polygon,
                            clip_features=clipping_polygon,
                            out_feature_class=clip_output,
                            cluster_tolerance="")
        return
