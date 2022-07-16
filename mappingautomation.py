# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 14:33:53 2021

@author: samhith
"""

import numpy as np
import pandas as pd

#import  for fdc_final
ds=pd.read_csv('E:/Cognetry labs/Datasets/fdc/fdc_final.csv')
ds.shape
ds.columns = ('cat','v1','v2','v3','v4','v5','v6','v7')
ds.info()
        
df=pd.DataFrame({'category_id':ds['cat']})
cat=pd.DataFrame({'v1':ds['v1'],'v2':ds['v2'],'v3':ds['v3'],'v4':ds['v4'],'v5':ds['v5'],'v6':ds['v6'],'v7':ds['v7']})
df['categories']= cat["v1"].astype(str) +"|"+ cat["v2"].astype(str) +"|"+ cat["v3"].astype(str) +"|"+ cat["v4"].astype(str) +"|"+ cat["v5"].astype(str)+"|"+ cat["v6"].astype(str) +"|"+ cat["v7"].astype(str)

x1 = df.set_index('category_id').categories.str.split(r'|', expand=True).stack().reset_index(level=1, drop=True).to_frame('foodGroup_description');  pd.get_dummies(x1,columns=['foodGroup_description']).groupby(level=0).sum()
del df['categories']
df2= pd.merge(df,x1,on='category_id')
df2['category_id']=df2['category_id'].str.lower().str.replace(' ', '')
df2['foodGroup_description']=df2['foodGroup_description'].str.lower().str.replace(' ', '')
df2.columns=['ci','fgd']
df2.head(10)




ds1=pd.read_csv('E:/Cognetry labs/Datasets/Copy of final_branded_food_hits.csv')
ds1.info() 
x2=ds1.iloc[:,[3,12]]
fdc_df=pd.DataFrame(x2)
fdc_df['foodGroup_description']=fdc_df['foodGroup_description'].str.lower().str.replace(' ', '')

s=pd.DataFrame(fdc_df).sample(n=1000)
s.columns=['fd','fgd']
s["category"]=""
r=np.array(s['fd'])

for i in r:
    k=list(s["fgd"].loc[s['fd']==i].iloc)[0]
    l=list(df2['ci'].loc[df2['fgd']==k].iloc)
    if(l!=[]):
        s.loc[s.fd ==i , "category"]=l[0]
 
s.to_csv('E:/Cognetry labs/Datasets/sample.csv',index=True) 