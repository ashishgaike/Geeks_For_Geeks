#User function Template for python3
class Solution:
    #Function to return list containing first n fibonacci numbers.
    def printFibb(self,n):
        l=[]
        a,b=0,1
        l.append(b)
        for i in range(0,n-1):
            c=a+b
            a=b
            b=c
            l.append(c)
        return l
