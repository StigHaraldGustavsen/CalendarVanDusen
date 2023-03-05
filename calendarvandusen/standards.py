Most_common_type = {
    'TCR':3851,
    'R0':100,
    'A':3.9083e-3,
    'B':-5.755e-7,
    'C':-4.183e-12,
    'note':'most common RTDs, can also have R0 of 1000'
    }

standards = {
    "IEC-751":Most_common_type,
    "DIN 43760":Most_common_type,
    "BS 1904":Most_common_type,
    "ASTM-E1137":Most_common_type,
    "EN-60751":Most_common_type,
    "IEC-60751":Most_common_type,
    "Low-cost-RTDs":{
        'TCR':3750,
        'R0':1000,
        'A':3.81e-3,
        'B':-6.02e-7,
        'C':-6.0e-12,
        'note':'low cost RTDs'
    },
    'JISC-1604-1997':{
        'TCR':3916,
        'R0':100,
        'A':3.9739e-3,
        'B':-5.870e-7,
        'C':-4.4e-12,
        'note':'Used most in japan'
    },
    'US Industrial Standard D-100 American':{
        'TCR':3920,
        'R0':100,
        'A':3.9787e-3,
        'B':-5.8686e-7,
        'C':-4.167e-12,
        'note':'low cost RTD'
    },
    'US Industrial Standard American':{
        'TCR':3911,
        'R0':100,
        'A':3.9692e-3,
        'B':-5.8495e-7,
        'C':-4.233-12,
        'note':'low cost RTD'
    },
    'ITS-90':{
        'TCR':3928,
        'R0':100,
        'A':3.9888e-3,
        'B':-5.915e-7,
        'C':-3.85-12,
        'note':''
    }
}

# referance National Instruments 
# https://www.ni.com/docs/en-US/bundle/ni-daqmx/page/measfunds/rtdtypes.html

