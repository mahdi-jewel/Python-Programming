print('Enter a word: ')
word = input()
word = word.casefold()
reverse_word = word[::-1]
if word == reverse_word:
    print('Wow! This is a palindrome.')
else:
    print('LOL, This is not a palindrome.')