import pandas as pd
#loading file function

def load_csv(path):
    df = pd.read_csv(path,engine='python',error_bad_lines=False, na_values=['?', None,'-','--','undefined'])
    return df