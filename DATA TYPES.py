#!/usr/bin/env python
# coding: utf-8
DATA TYPES GIVEN BELOW :
1.Integer
2.String
3.Float
4.Boolean values True False
5.complex numbers
6.Set
7.List
8.Tuple
9.Dictionary

10.TYPE function is used to check type
# In[5]:


s="Welcome coders"
type(s)


# In[6]:


p="Python is EASY"
type(p)


# In[13]:


w=15.56
type(w)
# same type(15.56)


# In[12]:


type(15.56)

COMPLES numbers is a=6+7j real number is 6 and img num is 7j
# In[18]:


a=5+3j
type(a)


# In[19]:


a.imag   #to check imag number in equation


# In[20]:


a.real   #to check real number in equation


# # LIST 
List can have all data types integers ,string, float, boolean and complex number
# In[31]:


l=['jyothi',150,23.36,True,7+5j]


# In[32]:


l


# In[33]:


type(l)


# In[34]:


len(l)


# In[71]:


tuple(l) #convert


# # TUPLE
bracket used for tuple () what kind of data can be stored in tuple
1. diff bet LIST and TUPLE changes can be made into the list but not in tuple  data like blood group,finger print , adhar card number are stored in tuple so that they can not be changes later on.
2. INDEXING is present
3.Tuple can be converted into list
# In[47]:


t=(12,23.02,True,100,"jyo")


# In[48]:


t


# In[70]:


list(t) #conversion


# In[49]:


len(t)


# In[40]:


t=(5)  #this is not a tuple it is tuple created here type if t is int and not tuple
type(t)


# In[41]:


t=("jyo")
type(t)


# In[42]:


#one data with tuple can be created by adding , single coma after first data
t=("jyo",)
type(t)


# In[44]:


t=("jyo",256) #type tuple with two data
type(t)


# # SET
1.s={} int float string complex boolean
2. NO indexing in SET 
3. set take ONLY unquie data repeated data is not shown again
4. data is automaticalyy sorted like first int complex then at last string will be displayed
5.{} same for dict also but blank set can not created blank dic is possible
# In[67]:


s={12.3,56,1,12,True,'false',False,5+6j,12.3,56,True,'false',False,5+6j} #one false is string 


# In[68]:


s #repeated data is not displayed in set


# In[65]:


type(s)


# In[69]:


len(s)


# In[80]:


#interview ques
s1="jyothiABChande"
#from above string only unquie data needed as some alphabets are repeated
set(s1) # this gives only unquie output


# # DICTIONARY
# 
{'key':'value'} key name has to be unqiue but value can be same
1.d={} same for dict also but blank set={} can not created blank dic is possible\
2.Tuple and list can be created in thE dictionary
# In[87]:


d={} # blank dic can be created  but blank sset is not possible
type(d)


# In[88]:


s={}
type(s) #where s is set


# In[85]:


d=[]
type(d)


# In[86]:


d=()
type(d)


# In[111]:


d={'key':'value','name':'JYOTHI','contact':97658,'boolean':True ,'tax':15.2,'l':[1,1,52],'t':(2,1)}
d 


# In[100]:


type(d)


# In[103]:


len(d)


# In[108]:


d1={'s':{1,2,5},'name':'JYOTHI','name1':'JYOTHI'}
d1


# In[114]:


list(d1)


# In[113]:


list(d) #dictionary can not be converted into list or tuple or set only shows keys


# In[ ]:




