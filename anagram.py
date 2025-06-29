# Check whether two strings anagram or not..
x = 'rat'
y = 'art'

is_anagram = True

if len(x) != len(y):
    is_anagram = False
else:
    for i in x:
        if x.count(i) != y.count(i):
            is_anagram = False
            break

if is_anagram:
    print("Anagram")
else:
    print('Not Anagram')