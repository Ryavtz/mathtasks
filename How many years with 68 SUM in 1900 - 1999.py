#!/usr/bin/env python
# coding: utf-8

# In[5]:


import datetime
from datetime import timedelta

def Date_2_Sum(m_date): 
    m_date = m_date.timetuple()
    My_year = m_date.tm_year
    My_month = m_date.tm_mon
    My_day = m_date.tm_mday
    a = My_year // 100
    b = My_year % 100
    Sum = a + b + My_month + My_day
    return Sum

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




