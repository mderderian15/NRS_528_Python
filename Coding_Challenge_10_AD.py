# Our coding challenge this week that improves our practice with rasters from Week 10.
#
# Task 1 - Use what you have learned to process the Landsat files provided, this time, you know you are interested in
# the NVDI index which will use Bands 4 (red, aka vis) and 5 (near-infrared, aka nir) from the Landsat 8 imagery,
# see here for more info about the bands: https://www.usgs.gov/faqs/what-are-band-designations-landsat-satellites.
# Data provided are monthly (a couple are missing due to cloud coverage) during the year 2015 for the State of RI,
# and stored in the file Landsat_data_lfs.zip.
#
# Before you start, here is a suggested workflow:
#
# Extract the Landsat_data_lfs.zip file into a known location. For each month provided, you want to calculate the
# NVDI, using the equation: nvdi = (nir - vis) / (nir + vis)
# https://en.wikipedia.org/wiki/Normalized_difference_vegetation_index. Consider using the Raster Calculator Tool in
# ArcMap and using "Copy as Python Snippet" for the first calculation. The only rule is, you should run your script
# once, and generate the NVDI for ALL MONTHS provided. As part of your code submission, you should also provide a
# visualization document (e.g. an ArcMap layout in PDF format), showing the patterns for an area of RI that you find
# interesting.

# Calculating NDVI
# NIR = spectral reflectance measurements from near infrared regions (Band 5)
# VIS = spectral measurements from red/ visible region (Band 4)

import arcpy

with arcpy.EnvManager(scratchWorkspace=r"C:\NRS 528\NRS_528_Python\Coding_Challenge_10\201502"):
    output_raster = arcpy.ia.RasterCalculator(
        expression=r'( "C:\NRS 528\NRS_528_Python\Coding_Challenge_10\201502'
                   r'\LC08_L1TP_012031_20150201_20170301_01_T1_B5.tif" -  "C:\NRS '
                   r'528\NRS_528_Python\Coding_Challenge_10\201502\LC08_L1TP_012031_20150201_20170301_01_T1_B4.tif")/ '
                   r'( "C:\NRS '
                   r'528\NRS_528_Python\Coding_Challenge_10\201502\LC08_L1TP_012031_20150201_20170301_01_T1_B5.tif" + '
                   r'"C:\NRS 528\NRS_528_Python\Coding_Challenge_10\201502'
                   r'\LC08_L1TP_012031_20150201_20170301_01_T1_B4.tif")'
    )
    output_raster.save(r"C:\NRS 528\NRS_528_Python\Coding_Challenge_10\201502\RasterCalc")

with arcpy.EnvManager(scratchWorkspace=r"c:\NRS 528\nrs_528_python\coding_challenge_10"
                                       r"\nrs528_codingchallenge10_calculatendvi"
                                       r"\nrs528_codingchallenge10_calculatendvi.gdb"):
    output_raster = arcpy.ia.RasterCalculator(
        expression=r'( "C:\NRS 528\NRS_528_Python\Coding_Challenge_10\201504'
                   r'\LC08_L1TP_012031_20150422_20170301_01_T1_B5.tif"  - "C:\NRS '
                   r'528\NRS_528_Python\Coding_Challenge_10\201504\LC08_L1TP_012031_20150422_20170301_01_T1_B4.tif") '
                   r'/(  "C:\NRS '
                   r'528\NRS_528_Python\Coding_Challenge_10\201504\LC08_L1TP_012031_20150422_20170301_01_T1_B5.tif" + '
                   r'"C:\NRS 528\NRS_528_Python\Coding_Challenge_10\201504'
                   r'\LC08_L1TP_012031_20150422_20170301_01_T1_B4.tif")'
    )
    output_raster.save(r"c:\NRS 528\nrs_528_python\coding_challenge_10\nrs528_codingchallenge10_calculatendvi"
                       r"\nrs528_codingchallenge10_calculatendvi.gdb\rastercalc04")

with arcpy.EnvManager(scratchWorkspace=r"c:\NRS 528\nrs_528_python\coding_challenge_10"
                                       r"\nrs528_codingchallenge10_calculatendvi"
                                       r"\nrs528_codingchallenge10_calculatendvi.gdb"):
    output_raster = arcpy.ia.RasterCalculator(
        expression=r'( "C:\NRS 528\NRS_528_Python\Coding_Challenge_10\201505'
                   r'\LC08_L1TP_012031_20150508_20170227_01_T1_B5.tif" - "C:\NRS '
                   r'528\NRS_528_Python\Coding_Challenge_10\201505\LC08_L1TP_012031_20150508_20170227_01_T1_B4.tif") '
                   r'/ ("C:\NRS '
                   r'528\NRS_528_Python\Coding_Challenge_10\201505\LC08_L1TP_012031_20150508_20170227_01_T1_B5.tif" + '
                   r'"C:\NRS 528\NRS_528_Python\Coding_Challenge_10\201505'
                   r'\LC08_L1TP_012031_20150508_20170227_01_T1_B4.tif")'
    )
    output_raster.save(r"c:\NRS 528\nrs_528_python\coding_challenge_10\nrs528_codingchallenge10_calculatendvi"
                       r"\nrs528_codingchallenge10_calculatendvi.gdb\rastercalc05")

with arcpy.EnvManager(scratchWorkspace=r"c:\NRS 528\nrs_528_python\coding_challenge_10"
                                       r"\nrs528_codingchallenge10_calculatendvi"
                                       r"\nrs528_codingchallenge10_calculatendvi.gdb"):
    output_raster = arcpy.ia.RasterCalculator(
        expression=r'( "C:\NRS 528\NRS_528_Python\Coding_Challenge_10\201507'
                   r'\LC08_L1TP_012031_20150711_20170226_01_T1_B5.tif" - "C:\NRS '
                   r'528\NRS_528_Python\Coding_Challenge_10\201507\LC08_L1TP_012031_20150711_20170226_01_T1_B4.tif") '
                   r'/( "C:\NRS '
                   r'528\NRS_528_Python\Coding_Challenge_10\201507\LC08_L1TP_012031_20150711_20170226_01_T1_B5.tif" + '
                   r'"C:\NRS 528\NRS_528_Python\Coding_Challenge_10\201507'
                   r'\LC08_L1TP_012031_20150711_20170226_01_T1_B4.tif")'
    )
    output_raster.save(r"c:\NRS 528\nrs_528_python\coding_challenge_10\nrs528_codingchallenge10_calculatendvi"
                       r"\nrs528_codingchallenge10_calculatendvi.gdb\rastercalc07")

with arcpy.EnvManager(scratchWorkspace=r"c:\NRS 528\nrs_528_python\coding_challenge_10"
                                       r"\nrs528_codingchallenge10_calculatendvi"
                                       r"\nrs528_codingchallenge10_calculatendvi.gdb"):
    output_raster = arcpy.ia.RasterCalculator(
        expression=r'( "C:\NRS 528\NRS_528_Python\Coding_Challenge_10\201510'
                   r'\LC08_L1TP_012031_20151015_20170225_01_T1_B5.tif" - "C:\NRS '
                   r'528\NRS_528_Python\Coding_Challenge_10\201510\LC08_L1TP_012031_20151015_20170225_01_T1_B4.tif") '
                   r'/( "C:\NRS '
                   r'528\NRS_528_Python\Coding_Challenge_10\201510\LC08_L1TP_012031_20151015_20170225_01_T1_B5.tif" + '
                   r'"C:\NRS 528\NRS_528_Python\Coding_Challenge_10\201510'
                   r'\LC08_L1TP_012031_20151015_20170225_01_T1_B4.tif")'
    )
    output_raster.save(r"c:\NRS 528\nrs_528_python\coding_challenge_10\nrs528_codingchallenge10_calculatendvi"
                       r"\nrs528_codingchallenge10_calculatendvi.gdb\rastercalc10")

with arcpy.EnvManager(scratchWorkspace=r"c:\NRS 528\nrs_528_python\coding_challenge_10"
                                       r"\nrs528_codingchallenge10_calculatendvi"
                                       r"\nrs528_codingchallenge10_calculatendvi.gdb"):
    output_raster = arcpy.ia.RasterCalculator(
        expression=r'( "C:\NRS 528\NRS_528_Python\Coding_Challenge_10\201511'
                   r'\LC08_L1TP_012031_20151116_20170225_01_T1_B5.tif" - "C:\NRS '
                   r'528\NRS_528_Python\Coding_Challenge_10\201511\LC08_L1TP_012031_20151116_20170225_01_T1_B4.tif") '
                   r'/( "C:\NRS '
                   r'528\NRS_528_Python\Coding_Challenge_10\201511\LC08_L1TP_012031_20151116_20170225_01_T1_B5.tif" + '
                   r'"C:\NRS 528\NRS_528_Python\Coding_Challenge_10\201511'
                   r'\LC08_L1TP_012031_20151116_20170225_01_T1_B4.tif")'
    )
    output_raster.save(r"c:\NRS 528\nrs_528_python\coding_challenge_10\nrs528_codingchallenge10_calculatendvi"
                       r"\nrs528_codingchallenge10_calculatendvi.gdb\rastercalc11")

