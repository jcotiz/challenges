"""
A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name. They are now trying out various combinations of company names and logos based on this condition. Given a string , which is the company name in lowercase letters, your task is to find the top three most common characters in the string.

Print the three most common characters along with their occurrence count.
Sort in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.
For example, according to the conditions described above,

 would have it's logo with the letters .

Input Format

A single line of input containing the string .

Constraints

 has at least  distinct characters
Output Format

Print the three most common characters along with their occurrence count each on a separate line.
Sort output in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.

Sample Input 0

aabbbccde
Sample Output 0

b 3
a 2
c 2
Explanation 0


Here, b occurs  times. It is printed first.
Both a and c occur  times. So, a is printed in the second line and c in the third line because a comes before c in the alphabet.

Note: The string  has at least  distinct characters.
"""

from collections import Counter

r = Counter()
letters = []
l = 0





if __name__ == '__main__':
    s = input()
    
    for letter in s:
        r[letter] += 1
        
    l = len(r)

    
    for letter, times in r.items():
        letters.append((letter, times))
            
            
        
    letters = sorted(letters, key=lambda x: (-x[1], x[0]))
    letters = letters[:3]
    
    for result in letters:
        print(f"{result[0]} {result[1]}")