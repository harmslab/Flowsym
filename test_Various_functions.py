# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 11:29:28 2020

@author: Michael
"""


import pytest
import Various_functions as vf
import pandas as pd
import numpy as np



def test_create_controls():
    """
    test the create controls function to make sure that we created
    all of our control dataframes correctly
    """
    
    greens, reds = vf.create_controls(10,['green','red'])  # Params for test function
    
    assert len(greens) == 10   # Did we output dataframe of correct size?
    assert type(reds) == type(pd.DataFrame())   # Did we output an actual dataframe object?
    assert list(greens.columns) == ['Wavelength','Excitation Efficiency', 'Emission Efficiency']  # Did we make the right columns?
    
    # Check to make sure wavelengths are equal
    for index, val in greens.iterrows():
        assert val['Wavelength'] == reds['Wavelength'][index]
        assert val['Excitation Efficiency'] != reds['Excitation Efficiency'][index]
        assert val['Emission Efficiency'] != reds['Emission Efficiency'][index]
        
    # Make sure all excitation or emission efficiencies are the same in a given dataframe
    assert greens['Excitation Efficiency'][0] == greens['Excitation Efficiency'][np.random.choice(range(1,len(greens)))]
    assert reds['Emission Efficiency'][0] == reds['Emission Efficiency'][np.random.choice(range(1,len(reds)))]
    
    
    
    
def test_create_sample():
    """
    test the create sample function to make sure we made our sample dataframe correctly
    """
    sample = vf.create_sample(10,['blue','green','NIR']) # Params for test function
    
    assert len(sample) == 10   # Is dataframe correct size from input step?
    assert type(sample) == type(pd.DataFrame())   # Did we actually output a dataframe?
    assert list(sample.columns) == ['Wavelength','Excitation Efficiency','Emission Efficiency','Copy number']  # Are these the columns?
    
    # Check to make sure excitation wavelengths aren't the same as emission
    for index, val in sample.iterrows():
        assert val['Excitation Efficiency'] != val['Emission Efficiency']



# Now that we've tested the create sample function, make a fixture for following function tests
@pytest.fixture()
def sample():
    dataframe = vf.create_sample(100)
    
    return dataframe

# Now that we've tested the create controls function, make a fixture for following function tests
@pytest.fixture()
def controls():
    blue,green,red,far_red,NIR,IR = vf.create_controls(100)
    
    return blue,green,red,far_red,NIR,IR



def test_measure(sample):
    
    measured = vf.measure(sample)
    
    assert len(list(measured.columns)) == 6
    assert type(measured) == type(pd.DataFrame())
    
    
    
