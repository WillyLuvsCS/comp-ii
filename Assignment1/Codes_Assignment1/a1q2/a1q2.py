

def divisible_Number(liste, n):
    #i = 2 # smallest possible divisor of n
    cpt = 0 # initializes the divisor counter
    for i in liste:
        if n != 0:
         if i%n == 0:
            cpt += 1
    return cpt


n = int(input("Please enter an integer : "))
ch = input("Please enter a comma-separated list of integers: ")
l1 = list(eval(ch))
print ("The number of elements divisible by", n ,"in the list is :", divisible_Number(l1, n))


