def Fibonacci(n):
    if n<=0:
        return 0
    # First Fibonacci number is 0
    elif n==1:
        return 0
    # Second Fibonacci number is 1
    elif n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
def fib_fast(n):
    myTable = {}
    def fib_helper(n):
        if n <=0:
            return 0
        elif n==1:
            return 0
        elif n==2:
            return 1
        elif n in myTable:
            return myTable[n]
        else:
            result = fib_helper(n - 1) + fib_helper(n-2)
            myTable[n] = result
            return result
    return fib_helper(n)
