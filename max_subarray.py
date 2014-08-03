import os

def getdata():
    datafile=open('data.txt','r')
    data=[];
    for line in datafile:
        data.append(int(line))
    datafile.close();
    return data

def diffarray(A):
    diff =[]
    for i in range(1,len(A)):
        diff.append(A[i]-A[i-1])
    return(diff)

def max_crossing_subarray(A,low,mid,high):
    tot=0
    l_sum = -float("inf")
    r_sum = -float("inf")
    l_index=mid
    r_index=mid+1
    for i in xrange(mid,low-1,-1):
        tot = tot + A[i] ;
        if(tot>l_sum):
            l_sum = tot
            l_index=i
    tot = 0
    for i in xrange(mid+1,high+1):
        tot = tot + A[i]
        if(tot > r_sum):
            r_sum = tot
            r_index=i
    return l_index,r_index,l_sum+r_sum


def max_subarray(A,low,high):
    if(low == high):
        return low,high,A[low]
    else:
        mid = (low + high ) /2 ;
        l_min,l_max,l_sum = max_subarray(A,low,mid)
        r_min,r_max,r_sum = max_subarray(A,mid+1,high)
        c_min,c_max,c_sum = max_crossing_subarray(A,low,mid,high)
        max_sum = max(l_sum,r_sum,c_sum)
        if(max_sum==l_sum):
            return l_min,l_max,l_sum
        elif(max_sum == r_sum):
            return r_min , r_max , r_sum
        else:
            return c_min,c_max,c_sum
        
    
