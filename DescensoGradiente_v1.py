#!/usr/bin/env python
# coding: utf-8

# In[71]:


__author__ = "Marcelo Gallegos"


# In[72]:


import numpy as np
import matplotlib.pyplot as plt
#from sympy import *
get_ipython().run_line_magic('matplotlib', 'inline')


# Funcion

# In[73]:


function = lambda x: (x ** 3)-(3 *(x ** 2))+7


# In[74]:


#1000 valores, equidistantes, entre a y b.
a = -1
b = 3
#x = Symbol('x')

x = np.linspace(a,b,500)


# In[75]:


#Plot
plt.plot(x, function(x))
plt.show()


# Derivate function

# In[76]:


def deriv(x):
    x_deriv = 3* (x**2) - (6 * (x)) #Derivación manual
    #x_deriv = function.diff(x)
    return x_deriv


# Step function

# In[77]:


def step(x_new, x_prev, precision, l_r):
    x_list, y_list = [x_new], [function(x_new)]
    iteracion = 0
    while abs(x_new - x_prev) > precision:
        x_prev = x_new
        d_x = - deriv(x_prev)
        x_new = x_prev + (l_r * d_x)
        x_list.append(x_new)
        y_list.append(function(x_new))
        iteracion = iteracion+1
        print("Iteracion: ", iteracion,"\nValor X: ",x_new)
    
    print ("\nRESULTADO:_____")
    print ("Minimo local en: " + str(x_new))
    print ("Numero de iteraciones: ", iteracion)
    
    plt.subplot(1,2,2)
    plt.scatter(x_list,y_list,c="g")
    plt.plot(x_list,y_list,c="g")
    plt.plot(x,function(x), c="r")
    plt.title("Descenso de gradiente")
    plt.show()

    plt.subplot(1,2,1)
    plt.scatter(x_list,y_list,c="g")
    plt.plot(x_list,y_list,c="g")
    plt.plot(x,function(x), c="r")
    plt.xlim([1.0,2.1])
    plt.title("Zona crítica")
    plt.show()


# In[78]:


step(0.5, 0, 0.001, 0.05)


# In[ ]:




