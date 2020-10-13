import sys
num = input('Input: num = ')
try:
    num = int(num)
except:
    print('Error! Input a number in digit(s)')
    sys.exit()
numbers=[]
try:
    numbers = list(map(int, input('Input: numbers = ').strip().split(',')))
except:
    print('Error! Please input numbers in digits separated by commas.')
    sys.exit()
if num in numbers:
    print('Output:', numbers.index(num))
else:
    print(-1)
