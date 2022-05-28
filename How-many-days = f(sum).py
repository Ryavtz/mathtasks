#!/usr/bin/env python
# coding: utf-8

# In[9]:


import datetime
from datetime import timedelta
import matplotlib.pyplot as plt
import numpy as np

def Date_2_Sum(date): 
    date = date.timetuple()
    My_year = date.tm_year
    My_month = date.tm_mon
    My_day = date.tm_mday
    return My_year // 100 + My_year % 100 + My_month + My_day

fst_day = datetime.date(1900, 1, 1)
last_day = datetime.date(1999, 12, 31)
next_day = fst_day
fst_year = fst_day.timetuple().tm_year
My_dict = {}

min_sum = Date_2_Sum(fst_day)
max_sum = Date_2_Sum(last_day)
for x in range(min_sum, max_sum):
    My_dict[x] = 0

while next_day != datetime.date(1999, 12, 31):
    thedatesum = Date_2_Sum(next_day)
    My_dict.update({thedatesum: My_dict.get(thedatesum) + 1})
    next_day += datetime.timedelta(days = 1)
    
print(min_sum, max_sum)
print(My_dict)

data_y = list(My_dict.values())
data_x = list(My_dict.keys())
array_x = np.array(data_x)
array_y = np.array(data_y)

plt.bar(array_x, array_y)
plt.show()


# In[ ]:




