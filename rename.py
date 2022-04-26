# -*- coding: utf-8 -*-
"""
@author: Andy
"""

#%%
import os
from uuid import uuid4
import pandas as pd
#%%

folder = " FILE PATH HERE"

#%%
oldNames = []
newNames = []
for  filename in os.listdir(folder):
    src = filename  
    dst = f"{uuid4()}.csv"
    os.rename(src, dst)
    oldNames.append(filename)
    newNames.append(dst)
    
#%%

df = pd.DataFrame(list(zip(oldNames, newNames)),
               columns =['oldNames', 'newNames'])

#%%
df.to_csv("fileNames.csv", index=False)