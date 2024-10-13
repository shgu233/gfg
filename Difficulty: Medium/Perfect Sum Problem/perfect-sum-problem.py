#User function Template for python3
class Solution:
	def perfectSum(self, arr, n, sum):
		# code here
		
		
		def s(ind,sum,dp):
		    if ind>=n or sum<0:
		        if sum==0:
		            return 1
		        return 0
		    if dp[ind][sum]!=-1:
		        return dp[ind][sum]
		    nt=s(ind+1,sum,dp)
		    t=0
		    if arr[ind]<=sum:
		        t=s(ind+1,sum-arr[ind],dp)
		    dp[ind][sum]=(t+nt)%((10**9)+7)
		    return dp[ind][sum]
		    
		dp=[[-1 for i in range(sum+1)] for j in range(n)]
		return s(0,sum,dp)
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n,sum = input().split()
		n,sum = int(n),int(sum)
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.perfectSum(arr,n,sum)
		print(ans)

# } Driver Code Ends