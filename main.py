import max_subarray as ms
import os
from matplotlib import pyplot as plt

def plot_data(data,n):
    plt.figure(n)
    plt.plot(data)
    

def annotate_data(x,y,text):
    plt.annotate(text, xy=(x,y), xytext=(x,y+5),arrowprops=dict(facecolor='black',shrink=0.05))

A= ms.getdata();
print A
dA = ms.diffarray(A)
l,r,tot = ms.max_crossing_subarray(dA,0,len(dA)/2,len(dA)-1)
plot_data(A,1)
annotate_data(l,A[l],'buy shares here')
annotate_data(r+1,A[r+1],'sell shares here')
plt.show()
