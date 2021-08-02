import pandas as pd
import numpy as np

def load_and_process(path):
    #Method Chain #1 loading from csv file, dropping missing value and unussed columns
    
    df = (pd.read_csv(path)
    .drop('SkinThickness', axis='columns').drop('BloodPressure', axis='columns')
    .drop('Glucose', axis='columns').dropna())
          
    df = df.reindex()
        
    #Method Chain #2 dropping unrealistic values and processing
    
    df2 = (df.drop(df[df['Age']>95].index)
           .drop(df[df['Age']<21].index)
           .drop(df[df['BMI'] == 0].index)
           .sort_values('Age'))
    
    df2 = df2.reindex()
    
    df3 = (df2.drop(df2[df2['Insulin'] == 0].index)).reindex()

   
    return df3
    