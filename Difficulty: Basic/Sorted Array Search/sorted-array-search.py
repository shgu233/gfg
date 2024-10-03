#User function Template for python3

class Solution:
    ##Complete this function
    def searchInSorted(self,arr, N, K):
        #Your code here
        
        s=0
        e=N-1
        m=(s+e)//2
        
        
        while s<=e:
           
            m=(s+e)//2
            if K>arr[m]:
                s=m+1
                
            elif K<arr[m]:
                e=e-1
                
            elif K==arr[m]:
                return 1
                
        return -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        NK = input().strip().split()
        N = int(NK[0])
        K = int(NK[1])
        A = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.searchInSorted(A, N, K))

# } Driver Code Ends