"""
You are given a string .
 contains alphanumeric characters only.
 Your task is to sort the string  in the following manner:

All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.
Input Format

A single line of input contains the string .

Constraints

Output Format

Output the sorted string .

Sample Input

Sorting1234
Sample Output

ginortS1324
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT

def sort_string(s):
    def key_func(c):
        if c.islower():
            return (1, c)
        elif c.isupper():
            return (2, c)
        elif c.isdigit():
            d = int(c)
            return (3 if d % 2 else 4, d)
        else:
            return (5, c)
    return "".join(sorted(s, key=key_func))


i = input()
resultado = sort_string(i)
print(resultado)
