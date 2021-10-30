import pandas as pd
import numpy as np


def unprocessed(csv_file):
    df = pd.read_csv(csv_file)
    return df

def select(df, col):
    return df[col]

def specify(df, col, s):
    return df.loc[df[col] == s]


def load_and_process(data):

    # Method Chain 1 (Load data and deal with missing data)

    df1 = (
        pd.read_csv(data)
          .rename(columns={"pace_impact": "pi"})
          .loc[lambda x: x['raptor_box_offense']>0]
          .sort_values("raptor_box_offense", ascending=False)
          .reset_index(drop=True)
          .loc[:, ["player_name","raptor_box_offense", "raptor_box_defense", "pi"]]            
          # etc...   
      )

    # Method Chain 2 (Create new columns, drop others, and do processing)

    df2 = (
          df1
          .assign(victory=lambda x: np.where((x.raptor_box_offense > x.raptor_box_defense), 1, 0))          
      )

    # Make sure to return the latest dataframe

    return df2 

# turn pace_impact to pi
#only select the data with a raptor offense>0
#Victory means offense > deffense value (=1) offense < deffense (=0)




