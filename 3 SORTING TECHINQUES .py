#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1 ----inbuilt [SORT] function 
a=[10,90,20,30]
print(a)
a.sort()
print(a)


# In[ ]:


#2 ----> inbuilt [SORTED] function 
a=[10,20,23,4,54,3]
print(a)
b=sorted(a)
print(b)


# In[ ]:


#3--------> BUBBLE SORT 
def bubble_sort(num): 
    for i in range(len(num)-1,0,-1): 
        for j in range(i): 
            if num[j]>num[j+1]: 
                num[j],num[j+1]=num[j+1],num[j]
num=[10,20,3,20,33,2,2]
print(num)
bubble_sort(num)
print(num)


# In[ ]:


#4 --------> SELECTION SORTING 
num=[10,2,30,40,34]
print("Before Sorting: ")
print(num)
for i in range(len(num)): 
    min_val=min(num[i:])
    min_index=num.index(min_val,i)
    num[i],num[min_index]=num[min_index],num[i] 
print("After sorting: ")
print(num)


# In[1]:


#MERGE SORTING 
def mergesort(list1):
    if len(list1)>1: 
        mid=len(list1)//2 
        left_list=list1[:mid]
        right_list=list1[mid:]
        mergesort(left_list)
        mergesort(right_list)
        i=0 
        j=0 
        k=0 
        while i<len(left_list) and j<len(right_list): 
            if left_list[i]<right_list[j]: 
                list1[k]=left_list[i]
                i=i+1 
                k=k+1 
            else: 
                list1[k]=right_list[j]
                j=j+1 
                k=k+1 
        while i<len(left_list):
            i=i+1 
            k=k+1 
        while j<len(right_list):
            j=j+1 
            k=k+1 
num=int(input())
list1=[int(input()) for x in range(num)]
print("Before Sorting: ")
print(list1)
mergesort(list1)
print("After sorting: ")
print(list1)


# In[ ]:


a="aChirstamasTree"
b=""
for i in a: 
    if i.isupper(): 
        b+="-"+i.lower()
    else: 
        b+=i
print(b)


# In[ ]:


n=int(input())
a=str(n)
if a==a[::-1]: 
    print("palindrome")
else: 
    print("Not palindrome")


# In[9]:





# In[ ]:


num=[10,90,]

