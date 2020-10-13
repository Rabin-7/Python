haystack = input('Input: haystack = ')
needle = input('Input: needle = ')

if needle in haystack:
    for i in range(len(haystack)):
        if needle in haystack[i:i+len(needle)]:
            print('Output:',i)
else:
    print(-1)
