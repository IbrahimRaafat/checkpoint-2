#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n=[]
for x in range(2000,3201):
    if x % 7==0 and x % 5 != 0:
        n.append(x)
print(n)        
        

