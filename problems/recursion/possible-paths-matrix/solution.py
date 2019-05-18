def numberOfPaths(m, n): 
        # not zero because we're starting at len(m) or len(n)
        if(m == 1 or n == 1): 
            return 1
    
    # If diagonal movements are allowed 
    # then the last addition 
    # is required. 
        return numberOfPaths(m-1, n) + numberOfPaths(m, n-1) 


# Driver program to test above function  
m = 3
n = 3
print(numberOfPaths(m, n)) 