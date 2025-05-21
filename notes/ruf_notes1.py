# What is precedence in python?

# So, first what is the word precedence "simple for in python expression has more then one mathematical operations
# then there is always a dilemma which expression should be excute first and which is next.in this secenario precedence plays key role"

"""
operator    operation          predence
 **         exponent           first predence
 
 %          modulus             second predence
//         integer division     (left to right)
 /          divison             
 *          multiplication          
 
 -          subtraction         third predence 
 +          addition            (left to right)"""

# (5-1)*((7+1)/(3-1))
"""
(4)*((7+1)/(3-1))
(4)*((8)/(3-1))
(4)*(8/2)
(4)*(4.0)
and = 16.0 
"""

# explain the local and global scope with suitatble examples

# defenation of loacl scope : parameters are variables are assigned inside of the function are called as locals
# defenation of global scope : parameters are variables are assigned outside of the function are called as globals

# key rule : the local variable can not be used in global scope
# example:

def spam():
    eggs = 588
    print(eggs)

# spam()
# print(eggs)

# the local variable are not ot be called in other local functions
def lcl():
    eggs = 99
    spamf()
    print(eggs)

def spamf():
    egg = 100

# lcl()

# write a python to generate the fibonaccis sequence

def find_fibonacci(input):
    n1 = 0
    n2 = 1
    l = []
    count = 0
    if input <= 0 :
        return f"Please give a positive number. {input} this number is not valied"
    
    if input == 1:
        return 1
    
    while count < input:
        l.append(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth

        count += 1

    return l

if __name__ == "__main__":
    n = -5
    result = find_fibonacci(n)
    print(result)

    

    






