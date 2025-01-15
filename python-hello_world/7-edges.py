#!/usr/bin/python3

"""
This script extracts specific parts of the string "School" and prints them:
- The first 3 letters of the string.
- The last 2 letters of the string.
- The middle part of the string (excluding the first and last characters).
"""

word = "Holberton"

print(f"First 3 letters: {word[:3]}")
print(f"Last 2 letters: {word[-2:]}")
print(f"Middle word: {word[1:-1]}")
