Descriptions/explanations of intpart_sea_ice_model contents:
direct questions/concerns to Julia Shates (shates@wisc.edu) and Ole Baadshaug (ole.baadshaug@uit.no)


------------------------------------------------------------------------------------------------------------------------------
Meteorological data:
saved as "pickled" files (___.p files in the folder), user can use python package "pickle" to open them.

hourly met data
in-situ hourly temperature & wind measurements: https://www.esrl.noaa.gov/gmd/dv/iadv/
site information/documentation: https://www.esrl.noaa.gov/gmd/obop/brw/

daily precip data
daily measurements in inches/day: http://climate.gi.alaska.edu/acis_data
documentation: http://www.rcc-acis.org/docs_datasets.html


snow density measurements taken at 71 17'18.8"N 156 29'34.5"W

------------------------------------------------------------------------------------------------------------------------------

Ice Growth Function saved in update2_sea_ice.py
[Hi,hours]=Grow_Ice(Ta_in,HS,Fw,Dt_days)

Inputs: 
Ta_in = temperature 

HS = snow depth height

Fw = ocean heat flux (residual)

Dt_days = number of days in growing period

Returns/outputs:
Hi = ice thickness

hours = number of hours that ice has been growing

--------------------------------------------------------------------------------------------------------------------------------
GROW_ICE.py

Run this python script and it will return a figure and the final snow depth and ice thickness from the calculation. 

--------------------------------------------------------------------------------------------------------------------------------
grow_ice_intpart_JUPYTER.ipynb

Open this file in a Jupyter notebook and grow sea ice interactively.
This file includes the distinct scenarios described in the final group presentation. 
--------------------------------------------------------------------------------------------------------------------------------
update2_sea_ice.py
snowfall_functions.py

These files contain functions necessary to run the simulation

--------------------------------------------------------------------------------------------------------------------------------