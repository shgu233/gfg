#User function Template for python3

class Solution:
    def isSubSequence(self, A, B):
        
        
        
        
        i=0
        
        for  j in range(len(B)):
            if i<len(A) and B[j]==A[i]:
                i+=1
                
        return i==len(A)
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        A,B = input().split()
        ob = Solution()
        if ob.isSubSequence(A,B):
            print(1)
        else:
            print(0)

# } Driver Code Ends