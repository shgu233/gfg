class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self,n, arr):
        
        
        j=n-2
        
        a=[arr[-1]]
        maxi=arr[-1]
        while j>=0:
            if arr[j]>=maxi:
                a.insert(0,arr[j])
                maxi=arr[j]
            j-=1
        return a
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():

    T = int(input())

    while (T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]
        obj = Solution()

        A = obj.leaders(N, A)

        for i in A:
            print(i, end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends