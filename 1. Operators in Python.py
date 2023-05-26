#!/usr/bin/env python
# coding: utf-8

# # OPERATORS
LIST OF OPERATORS
1. Mathematical/ Arthematic -- +,-,*, /division,//double division,% modulus
2. Relational / comparison
3. Logical and or not
4. Assignment
5. Bitwise
6. Membership #last two are only in python 
7. Identity##   Ways to create vairables :
1. 9a = 5      # error a vairable can not start with int
2. a94ss = 100   #number after alphabet can be used
3. a_jdhd = 654  #symbol must be avoided as there are already defined vairables/methods in python
4. %abc = 52.25  # wrong as vairable can not start with a symbol
5. ABcd = 82   # correct no limitations on upper limit or lower limit of a vairable
6. unlimited length for creating a vairable.# TO CHECK THE TYPE type() of a vairable:
# In[12]:


a_1 ='Python'#string
print(type(a_1))

B = 7        #integer BEAWARE b= '7' is a string with inverted commas 
print(type(B))

c = 5.3      # float
print(type(c))

D__ = '5'      # it is a string and not integer
print(type(D__))

e123 = 3+5j     # complex number 
print(type(e123))

x = 1
print(type(x))

b = True
print(type(b))

c = 1.0
print(type(c))

d = "Hello"
print(type(d))

e = [1, 2, 3]
print(type(e))

f = (1, 2, 3)
print(type(f))

g = {"a": 1, "b": 2}
print(type(g))
#by default string is stored if not mentioned


# In[14]:


# to check type of a vairable using FUNCTIONS :

def type_of_variable(g):
    "This function will return type of the variable"
    try:
        print(type(g))
    except Exception as e:
        print(e)
type_of_variable(g)

1. Mathematical/ Arthematic +  -  *  /division  //double division % modulus

# In[16]:


s=10
t=3
print(s+t)
print(s/t) #normal division
print(s*t)  #multiplication
print(s//t)  # double division gives quioent before decimal
print(s%t)   # modulus ---first remainder 


# In[49]:


3**2    # power of 2  /raise to

2. Relational / comparison   >   >=   <   <=  ==   != not equal
    output is always in boolean value True or false
# In[17]:


10>=5


# In[18]:


10<=5


# In[19]:


10==5


# In[21]:


10!=5


# In[22]:


10!=5


# In[23]:


0.1+0.2 == 0.3

3.LOGICAL : True False in this normal arithmatic operation can be performed
# OUTPUT of logical operator is always TRUE AND FALSE
# In[24]:


X=True
Y=False
print(X and Y)
print(X or Y)
print(not X)
print(not Y )


# In[83]:


True + True


# In[84]:


True*True


# In[85]:


True+False


# In[86]:


True*False


# In[88]:


True/True

4.Assignment Operator  =  += -= *= /=
# In[28]:


a=3
a=a+1 
a

# a=+1 is reverse in counting
# In[29]:


a-=1
a

5.BITWISE OPERATOR  >> move right , << move left
# In[31]:


a=16
a>>1


# In[32]:


a<<5


# In[34]:


a>>2

6.MEMBERSHIP is used to verify content is availble or not in given function 
# In[35]:


s="happy new year"


# In[36]:


"app" in s


# In[38]:


"what" in s


# In[39]:


"Year" in s


# In[40]:


"python" not in s

7. IDENTITY To check whether both mentioned vairables is same or not

# In[41]:


x="python" #each index is getting checked first using AND logic
y="Python"


# In[42]:


x is y 


# In[43]:


a1='ABCxyz'
a1 is x


# In[44]:


a1 is not y


# In[45]:


a1 is not x


# In[141]:


len(s)


# In[50]:


w=  12535        # is wrong it is interger
w1= "12535"       # correct is string


# In[56]:


print(len(w))
type(w)


# In[59]:


print(len(w1))
type(w1)


# In[ ]:




