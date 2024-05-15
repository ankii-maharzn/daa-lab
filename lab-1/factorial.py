def factorial(n):
    if n <= 1:
        return 1

    print("n: ", n)
    x = n * factorial(n-1)
    print("x: ", x)
    return x
    

num = 5
print(f"Factorial of {num} is {factorial(num)}")


"""
Time Complexity:
O(n)
"""