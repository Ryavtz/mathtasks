#!/usr/bin/env python
# coding: utf-8

# In[8]:


import datetime
from datetime import timedelta

def Date_2_Sum(date): 
    date = date.timetuple()
    My_year = date.tm_year
    My_month = date.tm_mon
    My_day = date.tm_mday
    return My_year // 100 + My_year % 100 + My_month + My_day

fst_day = datetime.date(1900, 1, 1)
next_day = fst_day
counter = 0
while next_day != datetime.date(1999, 12, 31):
    next_day += datetime.timedelta(days = 1)
    thedatesum = Date_2_Sum(next_day)
    if thedatesum == 68:
        print(next_day, "SUM of 68 is here")
        counter += 1
print(counter)
     


# In[ ]:




