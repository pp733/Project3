"""Testing Addition"""

import pandas as pd
#import time
from calc import log
import logging
import os
from calc.calculations.addition import Addition

dirname = os.path.dirname(os.path.realpath(__file__))

def test_calculation_addition():
    """testing addition method with csv inputs"""
    fileName = 'CSVFiles/Addition.csv'
    inputFile = os.path.join(fileName)
    df = pd.read_csv(inputFile)
    for x, y in df.iterrows():
        sum = (y.Value_1, y.Value_2)
        record = x
        addition = Addition.create(sum)
        log.logging_data(inputFile, "addition", record)
        #log.logging_data(time, inputFile, "addition", record)
        assert addition.get_result() == df['Result'][x]