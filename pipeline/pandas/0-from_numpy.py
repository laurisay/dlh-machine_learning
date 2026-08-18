import pandas as pd
import string

def from_numpy(array):

    num_cols = array.shape[1]
    
    columns = list(string.ascii_uppercase[:num_cols])
    
    df = pd.DataFrame(array, columns=columns)
    
    return df
