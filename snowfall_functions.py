import numpy as np

"""
Function to get snowfall depth from precip in inches
snow density is included in the function; the value is from observations taken at snow pit site

Created June 2018
J. Shates (University of Wisconsin, Madison)
""" 

def get_snowdepth(precip):
    SD=[]
    ASD=[]
    precip=precip*.0254#inches/day to m/day
    
    rho_l=1000.  #kg/m3
    rho_s=402.87077958539771 #kg/m3-> from observations. snowfall_data_processing file has array of values and calculations
    
    SD=(precip*rho_l)/rho_s

### accumulate snow depth
    aSD=[0.]
    for snow in SD:
        aSD.append(aSD[-1]+snow)
    ASD=aSD[1:]
     #returns accumulated snow depth in mm
    return ASD



    
