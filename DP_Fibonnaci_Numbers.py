memo = {}
def dp_fib(n):
    if n in memo:
        return memo[n]
    elif n == 1 or n == 0:
        memo[n] = 1
        return 1
    else:
        print("I was here")
        num = dp_fib(n-1) + dp_fib(n-2)
        memo[n] = num 
        return num
    
        

def fib(n):
    if n == 1 or n == 0:
        return 1
    else:
        print("I was here")
        num = fib(n-1) + fib(n-2)
        return num
dp_fib(10)

print("HAHA")

fib(10)

print(memo)

