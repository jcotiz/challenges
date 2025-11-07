"""
The included code stub will read an integer, , from STDIN.

Without using any string methods, try to print the following:


Note that "" represents the consecutive values in between.

Example

Print the string .

Input Format

The first line contains an integer .

Constraints


Output Format

Print the list of integers from  through  as a string, without spaces.

Sample Input 0

3
Sample Output 0

123
"""
if __name__ == '__main__':
    n = int(input())
    list_n = []
    zero= 0
    for i in range(n):
        zero += 1
        list_n.append(zero)
    
    result = "".join(str(n) for n in list_n)
    print(result)
