'''
Counting Vowels
Description:
You have been given a string by the user. Write a program that counts and prints the number of vowels (a, e, i, o, u) in the given string.
Extension: print out how many of each vowel occurs.
'''

def count_vowels(word):
    vowels = {'a':0, 'e':0, 'i':0 , 'o':0, 'u':0}
    
    for char in word:
        if char in vowels:
            vowels[char] +=1
    return vowels

if __name__ == '__main__':
    word = input('Enter a word: ').lower()
    vowels = count_vowels(word)
    
    print(f'There are {sum(vowels.values())} vowels in {word}')
    for k,v in vowels.items():
        if v != 0:  # optional
            print(f'{k} appears {v} times in {word}')