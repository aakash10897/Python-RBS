#!/usr/bin/env python
# coding: utf-8

# In[12]:


operator=str()
operator=input('Enter the operation that you want to perform: ')
flag=bool()
flag=True;
result=float()
a=input("Enter first operand: ")
while flag:
    if a.isnumeric():
        flag=False
        break
    print('A cannot be a string')
    a=input("Enter first operand: ")

flag=True
b=input('Enter second operand')
while flag:
    if b.isnumeric():
        flag=False
        break
    print('Enter a number not a string')
    b=input("Enter first operand: ")

a=int(a)
b=int(b)
    
if operator=='+':
    result=a+b
elif operator=='-':
    if a-b>=0:
        result=a-b
    else:
        result=b-a
elif operator=='*':
    result=a*b
elif operator=='/':
    result=a/b
    
print(result)


# In[ ]:





# In[ ]:




