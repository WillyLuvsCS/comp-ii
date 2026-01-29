def sequenceMax(x):
     '''(list)-> int
     This function takes a list of numbers and returns the length
     of the longest sequence of consecutive equal elements. 
     '''
     i = 0
     maxL = 1
     while i < len(x)-1 :
        tempL = 1
        while  i < len(x)-1 and x[i] == x[i+1]:
           tempL = tempL + 1
           i = i + 1
        if tempL > maxL:
           maxL = tempL  
        i = i + 1   
     return maxL

s = input("Please enter a comma-separated list of value: ")
a = list(eval(s))
print(sequenceMax(a))





