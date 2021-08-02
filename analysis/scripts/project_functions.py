import pandas as pd
import numpy as np

def load_and_process(path):
    #Method Chain #1 loading from csv file, dropping missing value and unussed columns
    
    df = (pd.read_csv(path)
    .drop('SkinThickness', axis='columns').drop('BloodPressure', axis='columns')
    .drop('Insulin', axis='columns').dropna())
          
    #Method Chain #2 dropping unrealistic values and processing
    
    df2 = (df.drop(df[df['Age']>90].index)
    .drop(df[df['Age']<21].index).sort_values('Age'))

    return df2
    