#Function that takes a list of numbers and returns True if there is at least
#a sequence of two consecutive equal elements,
#and False otherwise.

def sequenceOfTwo(x):
     '''(list)-> bool
      Returns true if there is at least one sequence
      of two consecutive equal elements, and false otherwise.
      '''
     res = False
     i = 0
     while i < len(x) - 1 and not res:
       if x[i]== x[i+1]:
            res = True
       i = i + 1
     return res

s = input("Please enter a comma-separated list of values.: ")
a = list(eval(s))
print(sequenceOfTwo(a))






