#User function Template for python3

class Solution:

	
	def seriesSum(self,n):
	    # code heren
	   # sum=0
	   # for i in range(n+1):
	   #     sum=sum+i
	    return round(((n*(n+1))/2))
 


#{ 
 # Driver Code Starts
                               #Initial Template for Python 3


# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n=int(input())
        ob = Solution()
        ans = ob.seriesSum(n)
        print(ans)
        tc=tc-1
# } Driver Code Ends
