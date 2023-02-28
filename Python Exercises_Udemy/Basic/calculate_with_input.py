"""
Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
Sample value of n is 5 
Expected Result : 615 
"""
#program for the above problem
n = int(input("Enter a number: "))
result = n + (n * 10 + n) + (n * 100 + n * 10 + n)
print("Result:", result)
#solution approach 
"""
The above program first accept an integer'n'from the user using the input() function and converts it to an integer using the int() function.
Then it computes the value of 'n+nn+nnn' using the following formula 'n+(n*10+n)+(n*100+n*10+n)'.
Finally it prints the result using the 'print()' function.
when we run this program with 'n' equals to 5, it should output'615', which is the expected result
"""
