# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 23:00:59 2026

@author: AA
"""

def analyze_text(text: str) -> dict:
    """Analyze the given text."""
    letters_count = 0
    digit_count = 0
    letters0 = {}
    letters1 = []
    max_letters_count = 0

    most_repeated_word0 = {}
    most_repeated_word1 = []
    most_word_count = 0

    longest_word = ''
    shortest_word = ''
    palindrome_count = 0
    uppercase_count = 0
    lowercase_count = 0

    word = text.split()
    words = len(word)

    if word:
        shortest_word = word[0]

    for i in word:

        if i == i[::-1]:
            palindrome_count += 1

        if len(i) > len(longest_word):
            longest_word = i

        elif len(i) < len(shortest_word):
            shortest_word = i

        for j in i:

            if j.isupper():
                uppercase_count += 1

            if j.islower():
                lowercase_count += 1

            if j.isalpha():
                letters_count += 1

                if j in letters0:
                    letters0[j] += 1
                else:
                    letters0[j] = 1

            if j.isdigit():
                digit_count += 1

    for i, j in letters0.items():

        if j > max_letters_count:
            max_letters_count = j
            letters1 = [i]

        elif j == max_letters_count:
            letters1.append(i)

    for i in word:

        if i in most_repeated_word0:
            most_repeated_word0[i] += 1
        else:
            most_repeated_word0[i] = 1

    for i, j in most_repeated_word0.items():

        if j > most_word_count:
            most_word_count = j
            most_repeated_word1 = [i]

        elif j == most_word_count:
            most_repeated_word1.append(i)

    result = {
        "word_count": words,
        "letter_count": letters_count,
        "digit_count": digit_count,
        "most_common_letter": letters1,
        "most_common_word": most_repeated_word1,
        "longest_word": longest_word,
        "shortest_word": shortest_word,
        "palindrome_count": palindrome_count,
        "uppercase": uppercase_count,
        "lowercase": lowercase_count
    }

    return result


text = input("Enter a text: ")

result = analyze_text(text)

print()
print("========== TEXT ANALYSIS ==========")
print()

print("Text Statistics")
print("----------------")
print("Words       :", result["word_count"])
print("Letters     :", result["letter_count"])
print("Digits      :", result["digit_count"])
print("Uppercase   :", result["uppercase"])
print("Lowercase   :", result["lowercase"])

print()
print("Word Analysis")
print("-------------")
print("Longest Word  :", result["longest_word"])
print("Shortest Word :", result["shortest_word"])
print("Palindromes   :", result["palindrome_count"])

print()
print("Most Common")
print("-----------")

print("Letter(s):", end=" ")
for i in result["most_common_letter"]:
    print(i, end=" ")

print()

print("Word(s)  :", end=" ")
for i in result["most_common_word"]:
    print(i, end=" ")

print()
print()
print("===================================")