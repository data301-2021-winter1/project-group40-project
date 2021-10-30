import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns

def load_and_process(csv_file):
    df = pd.read_csv(csv_file)
    df1=(df.dropna(axis=0) 
        .sort_values("player_name")
        .reset_index(drop=True)
        )    
    return df1, df1.shape