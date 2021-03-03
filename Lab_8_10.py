#Pablo Perez
#1770045
word = input()
backwards = ""

for i in word[::-1]:
    backwards += i
    word1 = word.replace(" ", "")
    backwards = backwards.replace(" ", "")
if backwards == word1:
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")
