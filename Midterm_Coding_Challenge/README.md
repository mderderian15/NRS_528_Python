# Midterm Tool Challenge
## Creating a Script Tool

For the midterm, we were required to create a script tool that uses both Python and arcpy. Our code was supplemented with
example data and was written so it could be run on any PC. The main requirement for this project was that the example
data had to be manipulated three different ways. 

For my assignment, I created a shapefile from the **Colleges and Universities in RI** CSV file. I then took this shapefile 
and performed an erase analysis on it to erase any institutions that were within the Providence, RI boundary. After completeing this, 
I performed a buffer analysis on the output from the erase analysis. I put a buffer of 1000m around the remainder of the
institutions.
