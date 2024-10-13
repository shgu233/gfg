#User function Template for python3

# Tree Node
# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None

class Solution:
    
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        # Vector to store the result
        ans = []
        
        # Check if the tree is empty
        if not root:
            return ans
        
        # Map to store the top view nodes
        # based on their vertical positions
        mpp = {}
        
        # Queue for BFS traversal, each element
        # is a pair containing node 
        # and its vertical position
        q = deque([(root, 0)])
        
        # Push the root node with its vertical
        # position (0) into the queue
        while q:
            # Retrieve the node and its vertical
            # position from the front of the queue
            node, line = q.popleft()
            
            # If the vertical position is not already
            # in the map, add the node's data to the map
            if line not in mpp:
                mpp[line] = node.data
            
            # Process left child
            if node.left:
                # Push the left child with a decreased
                # vertical position into the queue
                q.append((node.left, line - 1))
            
            # Process right child
            if node.right:
                # Push the right child with an increased
                # vertical position into the queue
                q.append((node.right, line + 1))
        
        # Transfer values from the
        # map to the result vector
        for value in sorted(mpp.items()):
            ans.append(value[1])
        
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        ob= Solution()
        
        res = ob.topView(root)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends