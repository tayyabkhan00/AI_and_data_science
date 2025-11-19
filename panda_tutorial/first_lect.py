import numpy as np
import pandas as pd

dic1={
    "name":["khalid","harry","tony","noah"],
    "region":["antartica","kolkata","lucknow","bareilly"],
    "marks":[81,72,89,69]
}
df=pd.DataFrame(dic1)
print(df.to_string(index=False))
#print(df.to_csv('abc.csv'))
print(df.head(2))
print(df.describe())
