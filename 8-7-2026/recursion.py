#simple program :calculation factorial
def factorial(n):
    if n==1 or n==0 :
        return 1;
    return n*factorial(n-1);
    
print("Factorial of 5:",factorial(5)); 

