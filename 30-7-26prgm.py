#!/usr/bin/env python
# coding: utf-8

# In[15]:


import numpy as np
a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
print("array a=\n",a)
print("array b=\n",b)
print("addition=\n",a+b)
print("substraction=\n",a-b)
print("multiplication=\n",a*b)
print("matrix multiplication=\n",np.dot(a,b))
print("transpose of a=\n",np.transpose(a))
print("transpose of b=\n",np.transpose(b))


# In[19]:


#with SVD
import numpy as np
#create a simple matrix
x=np.array([[1,2,3],[4,5,6],[7,8,9]])

#performSVd
U,S,VT=np.linalg.svd(x)

n_components=2
X_reconstruct=np.dot(U[:,:n_components],np.dot(np.diag(S[:n_components]),VT[:n_components,:]))
print("original matrix:")
print(x)
print("\nReconstructed Matrix(withreduced diamension):")
print(X_reconstruct)


# In[9]:


import matplotlib.pyplot as plt
x=[3,5,6,8]
y=[1,3,5,7]
z=[2,4,3,5]
plt.plot(x,y)
plt.plot(x,z)
plt.title("graph")
plt.xlabel("horizontal")
plt.ylabel("vertical")


# In[39]:


import matplotlib.pyplot as plt
subject=["maths","english","physics","chemistry"]
mark=[10,10,20,20]
plt.bar(subject,mark)
plt.scatter(subject,mark)
plt.hist(mark)
plt.legend()
plt.title("grade")
plt.xlabel("subject")
plt.ylabel("marks"))


# In[40]:


import matplotlib.pyplot as plt
subject=["maths","english","physics","chemistry"]
mark=[10,50,20,60]
plt.pie(mark,labels=subject)
plt.title("pie")


# In[45]:


import matplotlib.pyplot as plt
x=[1,2,6,18]
y=[3,10,12,20]
plt.plot(x,y,"r:o")


# In[60]:


import matplotlib.pyplot as plt
import numpy as np
x=np.array([1,2,3,5])
y=np.array([3,8,1,10])
plt.subplot(1,2,1)
plt.plot(x,y)
a=np.array([1,2,7,9])
b=np.array([3,8,6,10])
plt.subplot(1,2,2)
plt.plot(a,b)
plt.show()


# In[ ]:




