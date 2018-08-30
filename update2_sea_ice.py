"""
Created on Sat Jun 2
1D sea ice model with air temperature inputs and growing sea ice height
INTPART: ARCTIC FIELD SCHOOL

Origianl Sea ice model & variables in excel model by A. Mahoney
re-written into python by O. Baadshaug (University of Tromsoe) and J.Shates (University of Wisconsin-Madison)
"""


import numpy as np


"""Function made to recognize missing values in air temperature and return clean "data" product with NANs instead"""

def Remove_bad_values(data, missing_value,replace=np.nan):
    count=0
    for e in data:
        if e ==missing_value:# or e > 0:
            data.flat[count]=replace
        count =count+1
    return data


"""Function to actually simulate ice growth. uses thermodynamic equation
Inputs:
1) Ta_in: Temperature 
2) HS: snow depth
3) Fw: Ocean Heat Flux -> serves as residiual flux
4) Dt_days: delta time  (increment of change for each time step)


Returns the ice depth grown in that time step and the number of hours passed
"""
def Grow_Ice(Ta_in,HS,Fw,Dt_days):
    #Constants
    Dt_day=Dt_days #days
    Dt_norm=24*3600*Dt_day #s
    rho_i=900. #kg/m3
    L_i=334000. #J/kg latent heat of sea ice water
    #L_i=300000 #J/kg
    lambda_i=2.1 #W/m * K   conductivity of ice
    lambda_s=.3 #W/m * K    conductivitiy of snow

    Tf=-1.8 #C %freezing temperature of sea ice
    HS=HS #m array of height of snow above the sea ice -> leads to insolation!
     #m/m2 vertical heatflux (upward) from ocean to the ice

    Delta_T=[Dt_norm / 24*3600]


    lambda_si=[]
    Hi=[.1] #thickness of ice formed
    runtime = len(Ta_in)
    
    num = 1
    new_interval = False
    
    hours =[0]
    hour=0
    for j,i in enumerate(Ta_in):
        if i > Tf:
            if new_interval:
                hour = hour+num
            else:
                hour = hour+1
            Hi.append(Hi[-1])
            hours.append(hour)
            num = 1
            new_interval = False
            
            continue
            
        elif np.isnan(i):
            new_interval = True
            if num == 1:
                Ta_before = Ta
            num = num+1

            continue
            
        else:
            if new_interval:
                Dt_int = Dt_norm*num/2
                hour_int = int((hour)+num/2)
                num = 1        
                Ta_int = (Ta_before+i)/2    
                
                lambda_si= ((lambda_i*Hi[-1]) + (lambda_s*Hs))/(Hi[-1]+Hs)         
                DH=(Dt_int/(rho_i * L_i)) * (lambda_si*(Tf-Ta_int)/(Hi[-1]+Hs)-Fw)
                
                hours.append(hour_int)
                Hi.append(DH+Hi[-1])
        #     else:
#                 Dt = Dt_norm
#                 Ta=i #C %atmospheric temperature
            hour = hour+1
            Dt = Dt_norm
            Ta=i #C %atmospheric temperature
            new_interval = False
        Hs=HS[j]
        #Hs=0.
        #print(Hs)
        lambda_si= ((lambda_i*Hi[-1]) + (lambda_s*Hs))/(Hi[-1]+Hs)         
        DH=(Dt/(rho_i * L_i)) * (lambda_si*(Tf-Ta)/(Hi[-1]+Hs)-Fw)
        # import ipdb
        #        ipdb.set_trace()
        hours.append(hour)
        Hi.append(DH+Hi[-1])
    return Hi,hours
