# Is Palindrome
""" Write a method is_palindrome(word) that takes in a string word 
and returns the true if the word is a palindrome, false otherwise. 
A palindrome is a word that is spelled the same forwards and backwards. """

word = input("Enter a word: ")

if(word == word[::-1]):
      print("This word is a palindrome")
else:
      print("This word is not a palindrome")
