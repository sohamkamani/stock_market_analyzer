stock_market_analyzer
=====================

Simple stock market analyzer which uses the maximum sub-array property to determine the period of highest positive and negative change

To use : Replace the sample data in the text file data.txt with your own data and start by entering 'bash start.sh' on unix machines.

Description of methods
----------------------

getdata(): reads data from the data.txt file and returns the array of values

diffarray(A) : the differential of A . returns the differences between each successive value of A

max_crossing_subarray(A,low,mid,high): finds the maximum subarray that also crosses the mid index and is within low and high

def max_subarray(A,low,high): finds the maximum subarray of A

todo
----

-> find the maximum negative subarray

-> getdata() for an excel file


