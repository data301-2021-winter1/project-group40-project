import pandas as pd
import numpy as np

def select(df, col):
    return df[col]

def specify(df, col, s):
    return df.loc[df[col] == s]