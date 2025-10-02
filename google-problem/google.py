"""
Given a string s and an array of strings words, return the number of words [i] that is a subsequence of s.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".

Example 1:

Input: s "abcde", words = ["a", "bb", "acd", "ace"]
Output: 3
Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".
Example 2:
Input: s "dsahjpjauf", words = ["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"] 16 Output: 2"""

from collections import Counter

s = "dsahjpjauf"
words = ["ahjpjau", "ja","ahjpjjau" , "ahbwzgqnuk", "tnmlanowax"]
split_s = list(s)
words_repeat= Counter(split_s)


for word in words:
    split_word = list(word)


    check = all(letter in s for letter in split_word)

    if check:
        print("Palabra:", split_word)
        repeat = Counter(split_word)
        print("words_repeat:", words_repeat)
        print("repeat:", repeat)


        correct = all(repeat[letter] <= words_repeat.get(letter, 0) for letter in repeat)
        if correct:
            print("Correct")
        else:
            print("Incorrect")
    else:
        print("⚠️ Palabra contiene letras fuera de 's':", word)


"""
repeat = {
    "a": 2, <= 
    "b": 1,
    "c": 1,
    "d": 1,
    "e": 1
}
"""

"""step : check letra in string , step 2:   """


"""
test = "abcdee"
repeats = {c: count for letter,}

"""