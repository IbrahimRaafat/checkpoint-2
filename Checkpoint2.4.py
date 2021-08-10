#!/usr/bin/env python
# coding: utf-8

# In[8]:


inp_str=input("enter one word")
inp_int=int(input("enter any number"))
char_list=[]
final_word=""
for i in inp_str:
    char_list.append(i)
char_list.pop(inp_int-1)     
print("This is your word after removing letter number",str(inp_int), "is:",final_word.join(char_list))


# In[ ]:




